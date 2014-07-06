Title: testresources 0.2
Date: 2009-07-17 12:36
Author: Jonathan Lange (noreply@blogger.com)
Slug: testresources-02

At [EuroPython](http://www.europython.eu/) this year, I talked about
[unittest](http://docs.python.org/library/unittest.html) and how it's
misunderstood little module with it's own problems, and that despite its
rough exterior it really is a Good Thing.  
  
To demonstrate this, I gave examples of three pieces of software that
each extended unittest to solve the same problem: sharing expensive
resources between tests.  
  
The first two examples were Twisted's `setUpClass` / `tearDownClass` and
Zope's layers. They are terrible and you should never use them.  
  
If you really want to share expensive resources between tests, you
should use [testresources](http://pypi.python.org/pypi/testresources/).
testresources makes it easy to write tests that use resources that cost
a lot to set up and tear down (such as databases or SSH servers) without
screwing up your test isolation. [Robert
Collins](http://www.advogato.org/person/robertc/), the author, cut the
[0.2
release](http://pypi.python.org/packages/source/t/testresources/testresources-0.2.tar.gz)
today.  
  
testresources now has exactly [one known
bug](https://bugs.launchpad.net/testresources), although Rob argues that
maybe it's one unknown bug. It's down to the quantum level here: that's
how good testresources is.

