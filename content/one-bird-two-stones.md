Title: One bird, two stones
Date: 2009-02-22 23:34
Author: Jonathan Lange (noreply@blogger.com)
Slug: one-bird-two-stones

[Glyph](http://glyph.twistedmatrix.com/) thinks that [interfaces are
great](http://glyph.twistedmatrix.com/2009/02/explaining-why-interfaces-are-great.html),
and he is right (although I haven't read the full post, I certainly
agree with the title).  
  
One of the natural things you can do with interfaces is this: make a new
class Bar that delegates all of the properties of IFoo to an instance of
class Foo. This is the [Decorator
pattern](http://en.wikipedia.org/wiki/Decorator_pattern) (not to be
confused with Python's decorator syntax), and is also the Bird in this
parable.  
  
We use interfaces a lot in Launchpad, and we need to Decorate classes
quite a bit. So, we wrote something to make it easy and open sourced it.
It's called [lazr.delegates](https://launchpad.net/lazr.delegates). This
is Stone One, if you like.  
  
Stone Two was actually cast first, and is called
[twisted.python.components.proxyForInterface](http://twistedmatrix.com/documents/current/api/twisted.python.components.html#proxyForInterface).
It's distributed as a part of Twisted, and solves exactly the same
problem. For those interested, here's the [Twisted
implementation](http://bazaar.launchpad.net/%7Evcs-imports/twisted/main/annotate/head%3A/twisted/python/components.py)
(scroll to line 320ish) and here's the [lazr
implementation](http://bazaar.launchpad.net/%7Elaunchpad-pqm/lazr.delegates/devel/annotate/head%3A/src/lazr/delegates/__init__.py).  
  
Both implementations are fairly simple, and yet it is perhaps a shame
that there are two of them. If anyone is at fault, it's me, since I knew
about proxyForInterface and watched lazr.delegate arrive in the
Launchpad tree without even thinking that the two might actually be the
same thing.  
  
But I wonder, is there a process bug here? Is there something Launchpad,
Twisted, Zope or Guido could have done to avoid this?

