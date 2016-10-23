---
layout: post
tags: haskell golang
date: 2016-08-16 18:30
title: Re-implementing a Golang pattern in Haskell
published: false
author: jml
---

One of the [first non-trivial things I did in
Go](https://github.com/weaveworks/scope/pull/1554) was to take some queries
we were making to a backend server and parallelize them.

This turned out to be fairly easy to do. The [Go Programming
Language](https://www.amazon.co.uk/Programming-Language-Addison-Wesley-Professional-Computing/dp/0134190440/)
book documents how to do a parallel `for` loop in section 8.5. The
[code](https://github.com/adonovan/gopl.io/blob/master/ch8/thumbnail/thumbnail_test.go#L82-L110)
looks something like this:

```golang
func makeThumbnails5(filenames []string) (thumbfiles []string, err error) {
	type item struct {
		thumbfile string
		err       error
	}

	ch := make(chan item, len(filenames))
	for _, f := range filenames {
		go func(f string) {
			var it item
			it.thumbfile, it.err = thumbnail.ImageFile(f)
			ch <- it
		}(f)
	}

	for range filenames {
		it := <-ch
		if it.err != nil {
			return nil, it.err
		}
		thumbfiles = append(thumbfiles, it.thumbfile)
	}

	return thumbfiles, nil
}
```

Because I've been getting into Haskell recently, I thought it might be
interesting to try to translate this code directly. In the following, I'm
going to assume you are familiar with Go but not familiar with Haskell.

Be warned: this is wading into the deep end. It can be fun, but it can be
scary too. It's absolutely OK if you stop, or want to try something else.

First thing we need is an equivalent of `thumbnail.ImageFile`, which is the
function we want to call in parallel. Here's the Go version:

```golang
func ImageFile(infile string) (string, error)
```

And here's a Haskell equivalent:

```haskell
imageFile :: FilePath -> IO (Either String FilePath)
```

Let's compare these before we press on with parallelization.

They are both functions that take a single parameter (a path to a file), do
some IO, and return either an error or a path to another file.

*Case* matters in Haskell, just like in Go. However, case means something very
different. In Go, `UpperCase` means public and `lowerCase` means private. In
Haskell, `UpperCase` means specific type (e.g. `String`, `FilePath`, `Either`)
and `lowerCase` means value (e.g. `imageFile`). Lower case is also used for
type variables, which we'll get to later.

Haskell, like Go, puts *return types at the end of function signatures*. Here,
`imageFile` is a function that takes a `FilePath` (an alias for `String`) and
returns a rather complicated type of thing. Let's break it down, working from
the outside in.

The `IO` bit means that the function does some I/O and returns an `Either
String FilePath`. You have to put `IO` in your return type if you want to read
& write files.

In Go, when you want to return either an error or something else, you return a
2-tuple of `(whatever, error)`, and communicate success by returning `nil` for
the error. The normal way of doing this in Haskell is to use `Either`, with
the error value going on the left, and the right value going on the right.
Haskell does not have a dedicated error type in the way Go does, so I've
arbitrarily decided to use `String` instead.

So we have a function that takes a path to a file, does some I/O, and returns
a `FilePath` if everything went well, or an error message if something went
wrong.

That's a lot to take in.

Before we try the parallel version, let's show how we do call `imageFile`
serially.

Here's the Go version:

```golang
func makeThumbnails(filenames []string) {
	for _, f := range filenames {
		if _, err := thumbnail.ImageFile(f); err != nil {
			log.Println(err)
		}
	}
}
```

And here's a Haskell version:

```haskell
import Control.Monad (forM_)

makeThumbnails :: [FilePath] -> IO ()
makeThumbnails filenames = forM_ filenames (\f -> do
  result <- imageFile f
  case result of
    Left err -> putStrLn err
    _ -> pure ())
```

It's probably best if you spend some time comparing the two versions and
trying to figure out for yourself how the Haskell version works and what all
the bits mean. When you've done that, here's a whirlwind tour of the new
Haskell syntax:

* `import` does what you might think. `Control.Monad` is the name of the
  package and `forM_` is the only symbol we import from it.
* `[FilePath]` means "a list of `FilePath`", equivalent to `[]string`
* `IO ()` means "do some I/O and don't return anything"
* When defining a function, the parameters go before the `=` and the function
  itself comes after
* Haskell doesn't use braces, and relies instead on semantic indentation.
* Haskell doesn't have a `for` loop construct in the language itself, `forM_`
  is a rough equivalent
* `\f -> ...` is equivalent to `func (f) { ... }`. It's an inline function
  definition.
* `imageFile f` calls the `imageFile` function with argument `f`. Equivalent
  to `ImageFile(f)`.
* The `<-` symbol inside a `do` block means "do the I/O and put the result (in
  this case, `Either String FilePath`) into `result`. Think of it like assignment.
* `case` in Haskell is a lot like `case` in Go: it matches on `result`
* `Left err` only matches if `imageFile` returned an error. We don't have to
  check for `nil` because if it succeeded it would be `Right value` and the
  error simply wouldn't be there for us to check
* `putStrLn` prints a string to stdout followed by newline.
* `_` matches anything and throws away whatever it was we matched
* `pure ()` in this context means "an I/O action that does nothing and returns
  nothing"

Still keen for some parallelism?

First up, let's get ourselves some channels.

Haskell has had
[channels](https://hackage.haskell.org/package/base-4.9.0.0/docs/Control-Concurrent-Chan.html)
and
[an equivalent of goroutines](https://hackage.haskell.org/package/base-4.9.0.0/docs/Control-Concurrent.html#v:forkIO)
for _ages_, but they are library features, not a language features, so we need
to import some modules.


```haskell
import Control.Concurrent (forkIO)
import qualified Control.Concurrent.Chan as Chan
```

Then, we need to define a new function corresponding to `makeThumbnails5`
above:

```haskell
makeThumbnails5 :: [FilePath] -> IO (Either String [FilePath])
```

This function will have to make a new channel, loop through the filenames,
forking off a new routine for each filename and writing the results to the
channel.

Once that's done, we want to read from the channel in the main thread until
all the files have been processed. If any of the results return an error, we
want to return an error too.


```haskell
makeThumbnails5 :: [FilePath] -> IO (Either String [FilePath])
makeThumbnails5 filenames = do
  ch <- Chan.newChan
  forM_ filenames (\f -> forkIO (do
    it <- imageFile f
    Chan.writeChan ch it))
  results <- forM filenames (\_ -> Chan.readChan ch)
  case partitionEithers results of
    (err:_, _) -> pure (Left err)
    ([], thumbfiles) -> pure (Right thumbfiles)
```

This is the almost the most literal translation of `makeThumbnails5` I could
manage.

The `item` type that's in the Go version isn't necessary here, because it's
perfectly OK in Haskell to have a channel of `Either String FilePath`.

We construct the channel with `newChan` rather than `make(chan item,
len(filenames))`. Haskell figures out the type based on what's in the rest of
the function. We don't need to specify the size of the channel, because
Haskell channels always accept writes. Since `newChan` is a function with no
parameters we call it just by referring to it, in the same way that you would
refer to a variable.

Haskell doesn't have a language construct for returning early, so the rest of
the code is a little different.

We use `forM` to loop filenames, running a function that ignores its argument
and runs `readChan` (`forM` is like `forM_`, except `forM` collects the return
values from each loop into a list and returns them). The resulting `items` is a
list of `Either String FilePath` values. Then, once we've got those, we run
`partionEithers`, which returns two lists, `([String], [FilePath])`, where the
first is the list of error messages and the second is the list of successful
thumbnail files. If the first list is empty (i.e. `[]`), then we return the
list of `thumbfiles`. If not, we return the first error.

This doesn't quite match what the Go version does, as this Haskell version
will keep reading from the channel even after it has found an error.

It's also _really_ not idiomatic Haskell, and I'd like to fix that.

But first, I want to get to thing that inspired me to write this post in the
first place.

The _Go Programming Language_ describes `makeThumbnails5` and friends as
"concurrency patterns" (p234). It's good to be a little bit suspicious of
patterns in source code, because patterns and source code are both ways of
encoding knowledge about how to do something. If you see and refer to a
pattern in code, then it's almost always worth asking if you can write the
pattern _as_ code.

`makeThumbnails5` is described as:

```
// makeThumbnails5 makes thumbnails for the specified files in parallel.
// It returns the generated file names in an arbitrary order,
// or an error if any step failed.
```

If we try to describe the pattern, we might get:

> This makes a kind of thing from the specified things in parallel. It returns
> the generated things in arbitrary order, or an error if any step failed.

What would be great is if we could put that pattern into code.

In our Haskell version, we have:

```haskell
makeThumbnails5 :: [FilePath] -> IO (Either String [FilePath])
```

Which calls out to:

```haskell
imageFile :: FilePath -> IO (Either String FilePath)
```

If we want to encode the pattern, the first thing we need to do is pass
`imageFile` into `makeThumbnails5`, so we can substitute any thumbnail-making
routine.

The new type signature would look like this:

```haskell
makeThumbnailsParallel :: (FilePath -> IO (Either String FilePath)) -> [FilePath] -> IO (Either String [FilePath])
```

But our description talks about "specified things" and "generated things", not
FilePaths. So what we need to do is replace our concrete types with type
variables, like so:

```haskell
makeThumbnailsParallel :: (a -> IO (Either e b)) -> [a] -> IO (Either e [b])
```

This looks pretty weird, but it's still saying the same thing. I've just
substituted `a` for the input `FilePath` values, `b` for the output ones, and
`e` for String.

Let's see what the code would look like, renaming the function since it
doesn't have anything to do with thumbnails any more.

```haskell
makeParallelFirstError :: (a -> IO (Either e b)) -> [a] -> IO (Either e [b])
makeParallelFirstError f xs = do
  ch <- Chan.newChan
  forM_ xs (\x -> forkIO (do
    it <- f x
    Chan.writeChan ch it))
  results <- forM xs (\_ -> Chan.readChan ch)
  case partitionEithers results of
    (err:_, _) -> pure (Left err)
    ([], ys) -> pure (Right ys)
```

All that has changed in the code is that we now pass in a function `f`, and
have given the variables terser, more generic names.

We can then write our original parallel thumbnails function as:

```haskell
makeThumbnails5 :: [FilePath] -> IO (Either String [FilePath])
makeThumbnails5 filenames = makeParallelFirstError imageFile filenames
```

This is pretty cool. We've encoded our pattern as source code, and we've given
it a name. That means that anyone looking at `makeThumbnails5` can identify
the pattern by its True Name.

Notice also that we're not doing any casting. The compiler will raise an error
if we try to call `makeThumbnails5` with anything other than a list of
`FilePath`s, or if `imageFile` starts returning something different.

It also means that if we figure out a better way of achieving the same thing,
we only have to update one piece of code.

I mentioned earlier that our implementation was not very idiomatic. We create
a channel, have a loop that generates some values, feeds them into the
channel, and then discards them, and then a *second* loop that reads from the
channel until all the values are done. Why do we even bother with the channel?
Why can't we instead just do:

```haskell
makeParallelFirstError :: (a -> IO (Either e b)) -> [a] -> IO (Either e [b])
makeParallelFirstError f xs = do
  results <- forM xs (\x -> forkIO (f x))
  case partitionEithers results of
    (err:_, _) -> pure (Left err)
    ([], ys) -> pure (Right ys)
```

And indeed, we can.

We could go much further from here. Simon Marlow has written a
[whole book](http://chimera.labs.oreilly.com/books/1230000000929) on
parallelism & concurrency in Haskell.

In summary:

* Go has some pretty cool concurrency tools
* Haskell also has some pretty cool concurrency tools
* Patterns are great, but re-usable code is better
* Code that ignores types but preserves them is very useful and re-usable


All code from the _Go Programming Language_ is by Alan Donovan, and used here
under the CC-BY-NC-SA 4.0 International license. See
https://github.com/adonovan/gopl.io for details.

