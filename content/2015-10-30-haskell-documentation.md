Title: A wish for Haskell documentation
Date: 2015-10-30

A couple of weeks ago I went to the
[Haskell eXchange in London](https://skillsmatter.com/conferences/7069-haskell-exchange-2015).
I learned a lot and had a great deal of fun while I was there, and went away
with my head spinning.

On the weekend _after_ the conference, they had a hack session on Haskell
infrastructure. I wasn't able to attend, but here's what I would have pushed
for if I'd been there: _vastly improved documentation tools_.

I'm very grateful for what's already been done by those who've worked on
haddock, cabal, hackage and so forth, and I don't want to disrespect the time
& energy they've put in. However, things could be a lot better.

I want to start by showing how Rust do their docs, to provide a point for
comparison. Then I'm going to finish by making a few concrete recommendations.

## How Rust does it

### Landing page

Let's compare [Rust's stdlib documentation](https://doc.rust-lang.org/std/)
with [Haskell's](http://hackage.haskell.org/package/base).

I know it's not quite a fair comparison, because Haskell doesn't have a
standard library per se. Bear with me for now; I'd rather focus on
documentation rather than distribution.

Here's the Rust main page:

<img src="/images/haskell-v-rust/rust-api-doc-home-page.png" alt="Rust API documentation home page" style="width: 600px; border: thin black solid;"/>

Notice that it's _better looking_ than the equivalent Haskell documentation
page. The
[Haskell Platform documentation page](https://www.haskell.org/platform/contents.html)
and [Stackage package list](https://www.stackage.org/lts-3.11) look all right,
I'll admit. But as we'll see below, whatever good impression they make is
sabotaged when you follow a link through to actual Haddock-generated
documentation.

Note further that it's _immediately searchable_. There's a nice big search bar
at the top that you can use. It even includes inline help for how to use the
keyboard to start searching.

Stackage has search, which is great, but it considers it less important than
instructions on editing `stack.yaml`. It feels as if it counts itself as a
distribution page that happens to provide links to documentation, rather than
a documentation page.

### Searching

If you search for `Option` (Rust's equivalent to `Maybe`), you get this:

<img src="/images/haskell-v-rust/rust-api-doc-search-option.png" alt="Search results for Option in Rust's API documentation" style="width: 600px; border: thin black solid;"/>

Here, there's not much different from
[Stackage's search results for Maybe](https://www.stackage.org/lts-3.11/hoogle?q=Maybe).

Both find the right thing, both have useful descriptions in the results.
Rust's is faster. Stackage's uses Hoogle, which is more powerful.

Points deducted for using the word "Hoogle", which is an uninformative inside
joke.

[Hackage's search results for Maybe](http://hackage.haskell.org/packages/search?terms=Maybe)
are hilariously bad.

Search is super important for documentation. The whole reason for going to the
docs in the first place is that you don't quite know what you're doing. A
good, readily accessible search function makes this ignorance much more
manageable.

### Documentation

Let's follow the links in the documentation.

If we go to the [first link](https://doc.rust-lang.org/std/option/index.html)
for `Option` in Rust's docs, we see this:

<img src="/images/haskell-v-rust/rust-api-doc-option-module.png" alt="Rust API documentation for std::option" style="width: 600px; border: thin black solid;"/>

Contrast this with the
[first link from Stackage](http://haddock.stackage.org/lts-3.11/base-4.8.1.0/Prelude.html#t:Maybe).

The documentation for `std::option` looks the same as the landing page. You
haven't been whisked away to a mysterious other site, you're still browsing
the docs.

Further, Rust's documentation is _still immediately searchable_. That search
box is right there, all the time.

Even more, there's _example code_ right there on the front page. There's no
example code at all in the `Maybe` docs in `Prelude`, and also none in the
[Data.Maybe](http://haddock.stackage.org/lts-3.11/base-4.8.1.0/Data-Maybe.html)
documentation.

### Authoring environment

Haddock's markup is ... idiosyncratic. That's a problem for people who are
already switching between a half-dozen other markup syntaxes, but, I'm willing
to give it a pass. Pretty much every markup is terrible.

However, Rust's built-in tools have a killer feature that I think helps to
explain why they have so many examples in so much of their documentation.

If you run `cargo test` (analogous to `cabal test`) on a normal Rust package,
it will compile any example code it can find and then run it. If it doesn't
compile, the tests fail. If it has assertions that don't hold, the tests fail.

The assertions you see in the documentation for, say,
[Option.unwrap_or](https://doc.rust-lang.org/std/option/enum.Option.html#method.unwrap_or)
(equivalent to `fromMaybe`) are actually executed whenever you run the tests
during development. This prevents examples from becoming out of date.

Also, when you build the docs locally, you get something that looks almost
exactly like the standard documentation. I picked a package at random from
[crates.io](https://crates.io) and found
[feedreader](http://red-oxide.github.io/feedreader/feedreader/index.html).

If you follow the link, you'll see that it's searchable too. You'd get that
same searchability if you were working on feedreader locally & offline.

## What Haskell can do

### Make the docs prettier

Looks matter. There are studies (citation needed) that show that aesthetics
have a significant impact on usability.

I guess that most of the Haskell community are more comfortable with types
than typography (self included), but there has to be _someone_ out there. If
not, we could have a whip-round and hire someone to make a better design.

### Put search everywhere

The reason you look at docs is because you don't know what you're doing. We
all can questions that we needed answered, but we couldn't, because we didn't
know how to phrase them. Search goes a long way to ameliorating this problem.
A fast search is even better, because you can try a few different things.

### Insist on examples

Nothing beats an example. We already have awesome type signatures. If we add
examples, we complement the abstract with the concrete. Most learning involves
bouncing from one to the other and back again. When we don't provide examples,
we are denying ourselves one of the best learning tools available.

### Emphasise the local development story

Haskell can really shine here.

Imagine a world where, even when you're hacking in a cabal sandbox, you can
browse the docs for all of packages that you have installed in that sandbox.
(`ghc-pkg` already shows this information. There's just no browseable index
page.)

Imagine if you could search them--even when you're offline--without having to
figure out how to generate a Hoogle database. Hoogle is so amazingly useful I
am boggled that don't have it right at the forefront of the developer
experience.

Imagine if when you ran `cabal docs`, your docs were built and a browser
window opened, so you could proof-read and explore and _search_ them.

Imagine if when you viewed your own docs locally, they looked shiny and pretty
and something that you could be proud of.

We have all of the pieces to make this happen. We just need some brave
volunteers to glue them all together.

## Conclusion

That's it. It's a bit of a rant, but that's because I feel strongly that this
is an area where only a little work could make Haskell much more attractive.

I wish I could promise that I was going to make this my mission, but I can't.

I've made my own small contribution to the cause with
[open-haddock](https://github.com/jml/open-haddock), a tool that opens the
local documentation for a package or module. However, I see this as a stop-gap
measure until someone builds the right tools

Beyond that, if this has inspired you to improve the Haskell documentation
toolchain, then let me know. I can't help much, but I'll chip in as best I
can.

Happy hacking!
