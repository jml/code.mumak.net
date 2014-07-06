Title: testtools: history and future
Date: 2012-07-21 20:16
Author: Jonathan Lange (noreply@blogger.com)
Slug: testtools-history-and-future

  
Before I started [testtools](http://testtools.rtfd.org/) I was switching
regularly between [bzr](http://bazaar.canonical.com/),
[Launchpad](https://launchpad.net/launchpad) and
[Twisted](http://twistedmatrix.com/) and was sick of one excellent
testing innovation being available in one and not the other. I tried
submitting some of the improvements to Python. They were either ignored
or rejected.  
  
Also, as the maintainer of Twisted's testing framework, Trial, I had
been burned several times when the standard library would change its API
in backwards compatible ways, so I wanted something that would
encapsulate all of that once and for all.  
  
So, to provide a temporary ground between big, upstream projects that
are serious about testing and Python's standard library, I made the
project that was to become testtools. (It was originally called
pyunit3k. Sorry.).  
  
Its constraints were that it should work with Python 2.4, 2.5, 2.6, 2.7
and 3.1 (Bazaar, Launchpad & Twisted all cared about Python 2.4 at the
time), that any code in it should be allowed to go into Python without
special permission from contributors, and that it wasn't to have any
frivolous innovation, patches should be of code proven to be useful
elsewhere.  
  
Then eventually Michael Foord started maintaining Python's standard
unittest. While we haven't always seen eye-to-eye on the details, it's
definitely been a huge improvement, and Michael deserves props for doing
a job that I was unwilling to do. Releasing
[unittest2](http://pypi.python.org/pypi/unittest2/) was a great step,
and I think a good model of how any standard library maintenance should
be done.  
  
Since then, we've lightened the restraint on innovation in testtools,
and the last release was our last release to support Python 2.4 and 2.5.
The people who use it really love it, we've had plenty of contributors,
I use it on heaps of projects, and it certainly makes my job much, much
easier.  <span>Launchpad and Bazaar use it, but Twisted probably won't
ever, so that's 66% success according to my original
motivation. </span>  

<div>

I wish more people would use testtools. Actually, no, that's not right.
I wish more people would use the things in testtools. If people do that,
it makes it easier for me to contribute to their code, and makes using
their testing innovations much easier. 

</div>

<div>

As such, I'm hoping to try to get some of the most useful bits
([matchers](http://testtools.readthedocs.org/en/latest/for-test-authors.html#matchers)
first) into upstream Python. Wish me luck.

</div>
