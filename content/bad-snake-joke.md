Title: Bad Snake Joke
Date: 2012-02-25 13:36
Author: Jonathan Lange (noreply@blogger.com)
Slug: bad-snake-joke

Just between you and me, I'm getting a bit bored of writing Python all
the time. It's a good language: I can write code that's functional or OO
as the case may be; it has lots of libraries; it has
[Twisted](http://twistedmatrix.com/), which is incredibly useful; it's
not *too* hard to make [a big
project](https://code.launchpad.net/+branch/launchpad) and keep it
clean. It's the least awful programming language that I know of. That
said, I'd like to do something different.  
  
I would like to play with something makes static typing rock (like
Haskell), or that has what [Rich Hickey
calls](http://www.infoq.com/presentations/Simple-Made-Easy)
"polymorphism a la carte" (again, like
[Haskell](http://book.realworldhaskell.org/read/using-typeclasses.html),
or [Clojure](http://clojure.org/Protocols)). I would like to make
something that stands a chance of feeling snappy (perhaps
[PyPy](http://pypy.org/)?), a chance to use something with richer
debugging and refactoring tools, or to get a feel for doing some serious
concurrency work outside of an event loop.  
  
But mainly, I'm just bored of Python.  
  
Also, I increasingly suspect that Python [doesn't have
legs](http://www.biblegateway.com/passage/?search=gen%203:14&version=NIV).
The Python 3 language change has increased the split between the core
developer community and people writing code in the field. Python
continues to be slow, both with start-up time and while running. The
only people who seem to care are the [PyPy](http://speed.pypy.org/)
developers, but I doubt I'll ever get to use it for commercial
development. It's tricky to write code in Python that takes advantage of
multiple cores, and even my phone has multiple cores now.  
  
When I get the chance, I'm going to do more with Haskell and Clojure in
my spare time. I'm not sure if there is something less "fringe" that I
could recommend for use at Canonical. [Go](http://golang.org/) is a
possibility, if a slightly disappointing one (interfaces are cool, but
why oh why didn't they do typeclasses?).

