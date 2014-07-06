Title: testtools 0.9.12 out
Date: 2011-09-14 11:01
Author: Jonathan Lange (noreply@blogger.com)
Slug: testtools-0912-out

[testtools](http://pypi.python.org/pypi/testtools) 0.9.12 has just been
released!  
  
It's a huge release, this one. We normally try to release much more
frequently, but for this release I wanted to wait until [all of our
known unicode handling bugs were
fixed](https://bugs.launchpad.net/testtools/+bugs?field.tag=unicode&field.status=Fix+Released).
Today, [Martin [gz]](https://launchpad.net/~gz) finished off his [heroic
branch](https://code.launchpad.net/~gz/testtools/unprintable-assertThat-804127/+merge/72641)
to fix up
[`assertThat`](http://testtools.readthedocs.org/en/latest/for-test-authors.html#matchers),
and I figured it was time to release.  
  
In addition to all of the unicode fixes, we've really cleaned up the way
test failures are displayed. A lot of the boilerplate around the
traceback has been removed, a lot of levels of the stack are gone
(although you can get them back if you want), and `assertThat` is way
less repetitive. This all really adds up. If you're using an old
release, you want to upgrade right now. Honest.  
  
For me, this release is the one where using
[matchers](http://testtools.readthedocs.org/en/latest/for-test-authors.html#matchers)
becomes really and properly fun. As such, all of our `assertFoo` methods
are now implemented in terms of matchers.  
  
Of course, we have our usual raft of fixes, helpers and new matchers
too. The [full changelog](https://launchpad.net/testtools/0.9/0.9.12) is
on Launchpad.  
  
In addition to Martin [gz], thanks to [Christian
Kampka](https://launchpad.net/~kampka), [Robert
Collins](https://launchpad.net/~lifeless) and
[Canonical](http://canonical.com/) for making this release what it is.  
  
If you're new to testtools, it's basically a way to do serious,
[tasteful unit testing in
Python](http://testtools.readthedocs.org/en/latest/overview.html).  
  
Documentation lives at <http://testtools.readthedocs.org/en/latest/>.  
PyPI: <http://pypi.python.org/pypi/testtools>  
All development takes place on
Launchpad: <https://launchpad.net/testtools>  
Join us on \#python-testing on Freenode  
  
We don't currently have a release PPA, but we do have a [daily builds
PPA](https://launchpad.net/~testing-cabal/+archive/archive). The trunk
is kept stable using [Jenkins](http://mumak.net:8080/job/testtools/), so
it's fairly safe to use.

