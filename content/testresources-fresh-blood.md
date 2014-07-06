Title: testresources: fresh blood
Date: 2008-08-18 01:50
Author: Jonathan Lange (noreply@blogger.com)
Slug: testresources-fresh-blood

Last weekend I spent a bunch of timing hacking on
[testresources](https://launchpad.net/testresources) with
[Rob](http://robertcollins.net/) over at
[Chris](https://launchpad.net/%7Eraof)'s place. testresources is an
extension to unittest that allows tests to specify the resources they
use declaratively, so that these resources can be cleanly shared between
tests. On Saturday, we talked a bit about direction and decided on some
goals. On Sunday, [I got
busy](https://code.launchpad.net/%7Ejml/testresources/tests-meaning-cleanup/+merge/767).  
  
The idea isn't particularly new: zope.testing has had "layers" for a
long time. The key differences between testresources and Zope layers
are:  

-   You can use more than one TestResource. You can only use one layer.
    Allowing tests to specify many resources makes it easier to use only
    the resources that you need, which in turn makes for a faster test
    suite.  
-   A test that uses testresources can be used independently of other
    testresources machinery. With layers, you pretty much need the whole
    shebang. This means that you can use testresources with trial, bzr,
    nose, tribunal or unittest.TextTestRunner.  
-   Layers have magical inheritance stuff. testresources has no magic.
-   Layers do some work in subprocesses to accommodate some setUps that
    can have no tearDown. testresources doesn't know what a process is.  

That said, I'm mainly familiar with layers from Zope 3.2—they may have
changed since then.  
  
testresources itself is somewhat old. Rob hacked up the first version
about three years ago and little has happened to it since. I've always
agreed with the approach, but have also had a few qualms about
implementation details that made me reluctant to use it or to recommend
it. Now, it's well on its way to being something that I can trust and
perhaps, love.  
  
If you are interested, check out [my
branch](https://code.launchpad.net/%7Ejml/testresources/tests-meaning-cleanup)
or at least flick through the
[TODO](http://bazaar.launchpad.net/%7Ejml/testresources/tests-meaning-cleanup/annotate/77?file_id=todo-20080817122443-kaikqdedcg57lr4v-1)
file.

