Title: testtools 0.9.8 released
Date: 2010-12-22 19:19
Author: Jonathan Lange (noreply@blogger.com)
Tags: testtools
Slug: testtools-098-released

The announcement is a few days late, but I thought that you'd like to
know that [testtools 0.9.8](http://pypi.python.org/pypi/testtools) has
been released.  
  
This is one of our biggest releases, we have fixed [a lot of
bugs](https://launchpad.net/testtools/0.9/0.9.8), added experimental
support for running tests inside Twisted's reactor and added a stack of
new matchers and convenience methods. It's well worth upgrading.  
  
We've also got some good stuff in the pipeline, including a full
re-working of our documentation, better error messages and still more
matchers.  
  
The "more matchers" thing is significant. More and more people are
starting to use testtools because of the way our matchers let them build
domain-specific assertions with rich, useful error messages. We continue
to get contributions for basic matchers and for new ways of combining
matchers. Also, projects like James Westby's
[soupmatchers](https://launchpad.net/soupmatchers) show just how useful
matchers can be. It makes me think that eventually matchers will become
part of the normal way that people write tests in Python.  
  
Thanks to [Robert Collins](https://launchpad.net/~lifeless), [Martin
[gz]](https://launchpad.net/~gz), [Jelmer
Vernooij](https://launchpad.net/~jelmer), [Michael
Hudson-Doyle](https://launchpad.net/~mwhudson) and [James
Westby](https://launchpad.net/~james-w) for making this our best release
ever.

