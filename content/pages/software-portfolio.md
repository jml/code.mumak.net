Title: Software Portfolio
Date: 2012-09-22 16:11
Author: Jonathan Lange (noreply@blogger.com)
Slug: software-portfolio

  
I'm a programmer. I've made and contributed to an awful lot of software
that's available on the web, mostly Open Source.  
  
This isn't a complete list of all the software I've ever worked on, but
I hope it includes everything that's around today and available for
general use.  

Software I made
---------------

### [testtools](http://pypi.python.org/pypi/testtools)

Tasteful unit testing for Python.  

### [treeshape](http://pypi.python.org/pypi/treeshape)

Creates files and directories on disk in a declarative way. Great for
testing code that does disk I/O.  

Projects I have contributed to
------------------------------

### [Twisted](http://twistedmatrix.com/)

Still the best way to do networking in Python. Twisted was first open
source project I got involved with. I learnt so much from the other
contributors.  
  
I haven't contributed much recently, but back when I was more active, I
did a lot of work on Trial, Twisted's unit testing framework.  

### [subunit](https://launchpad.net/subunit)

<div>

Protocol for streaming test results. The foundational technology for
[testrepository](https://launchpad.net/testrepository), and extremely
useful for gathering interesting data about tests.

</div>

### [testrepository](https://launchpad.net/testrepository)

<div>

Wonderful little test runner that stores past results and uses those
results to parallelize test runs in the most efficient manner.

</div>

<div>

When you use it to run tests, it shows you the delta of failures, number
of tests and time taken to run. This is a little thing, but makes a
powerful difference to the TDD cycle.

</div>

### [pkgme](http://pkgme.net/)

<div>

Make Ubuntu packages for your project automatically.

</div>

### [python-fixtures](http://pypi.python.org/pypi/fixtures)

<div>

Resources with clean up that you can compose and re-use without buying
into an entire framework.  That said, they do work exceptionally well
with [testtools](http://testtools.rtfd.org/).

</div>

### [pyflakes](http://pypi.python.org/pypi/pyflakes)

<div>

Everyone's favourite Python lint checker.

</div>

### [Bazaar](http://bazaar.canonical.com/en/)

<div>

One of the earliest distributed version control tools and in many ways
the most pleasing to use. I wrote a lot of the Launchpad integration.

</div>

### [Launchpad](https://launchpad.net/)

<div>

Huge, ridiculously ambitious open source collaboration platform: tracks
bugs, hosts code, manages translations, and builds Ubuntu.

</div>

<div>

I wrote large chunks of the code hosting system, and have messed around
lots with its testing infrastructure and the chain of tools around
building packages.

</div>

<div>

For a while, I was also the product manager. When I was, I tried to make
sense of [what Launchpad actually
is](http://launchpad.readthedocs.org/en/latest/scope.html) and [what
it's strategy
was](http://launchpad.readthedocs.org/en/latest/strategy.html).

</div>

Scraps
------

These projects aren't really scraps. They are actually all quite useful
little tools that I don't spend much time on, because they meet my needs
and they don't have many users.  

### [difftodo](https://launchpad.net/difftodo)

Neat little tool that looks at diffs of Python code, finds any comments
with XXX, FIXME or TODO and then formats them nicely.  
  
Has Emacs integration, so you can treat XXX comments like compiler
errors.  

### [bzr-damage](https://launchpad.net/bzr-damage)

How much damage is this branch going to inflict? Measured in lines of
code added.  

### [testdoc](https://launchpad.net/testdoc)

<div>

I dislike Python's
[doctest](http://docs.python.org/library/doctest.html), for reasons best
explained by Andrew Bennetts: [narrative tests are lousy
tests](http://bemusement.org/diary/2008/October/23/narrative-tests) and
[tests are code, doctests
aren't](http://bemusement.org/diary/2008/October/24/more-doctest-problems).
People kept telling me that doctests were are great way of getting
documentation for free when writing tests. So, I wrote a cheeky little
tool that analyzes Python unit test modules and turns them into readable
documentation. This is it.

</div>
