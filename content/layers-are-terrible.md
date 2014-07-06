Title: Layers are terrible
Date: 2009-09-14 09:03
Author: Jonathan Lange (noreply@blogger.com)
Slug: layers-are-terrible

When I talk about testing frameworks, I often mention Zope layers and
say they are terrible. Some people have asked me for details on their
terror and for justification of my opinion.  
  
Here's all I've got. It's based on my experiences using layers with Zope
3.2 in Launchpad.  
  
**1. Layers have unnecessary magic**  
  
A layer can subclass another layer, which is fine. Subclassing means
that your new, derived layer rests on top of the old, base layer.  
  
When you define a derived layer though, you don't call the base layer's
methods yourself, like you would for any other Python subclass. Why not?
Because zope.testing magically up-calls the base layer's methods for
you.  
  
Yuck.  
  
The upshot is that you write non-standard Python that confuses people
not familiar with zope.testing. Also, you have no way of
<span>not</span> calling the base methods, which is unfairly
restrictive.  
  
**2. Layers are combined through inheritance**  
  
Each unit test is in a single layer. If you want a unit test to have the
set up and tear down provided by layer A *and* the set up and tear down
of layer B, you have to define a wholly new layer C that subclasses both
A and B.  
  
The layer C doesn't really mean anything other than "A and B". It
doesn't really deserve a name, but it has to have one, since it has to
be a new class.  
  
Since layers are often used to share expensive resources between tests,
you end up with a binary explosion of layer subclasses, as you move
toward needing one for every subset of available resources.  
  
This adds code and thus maintenance work, and is actually less clear
than simply declaring that a test uses layers A and B.  
  
**3. Layers are implemented badly**  
  
Layers are all about changing the way a test is run. They supplement the
run with extra work to establish a known base state for the test.  
  
If you think about it, the stuff that's required to run a test is a
property of the test.  
  
Python's `unittest` module recognizes this. One of the few public
methods of a `TestCase` object is its `run()` method. `run()` is also a
method of `TestSuite`. This means that if you want to customize the way
a test or a group of tests is run, you should override / re-implement
the `run()` method.  
  
Layers don't do this. Instead they change the way tests are gathered,
the way they are reported *and* the way they are run. This means tests
that rely on layers can only be run with the Zope test runner, and not
with nose or trial or what have you.  
  
**4. Layers solve too many problems**  
  
Layers are not simply a way of sharing expensive resources between
tests, they are also a way of using resources that cannot be torn down.  
  
The implementation does this by detecting that a layer cannot be torn
down, then spawning a new process to run the rest of the tests in.  
  
It kind of sucks to have things that cannot be torn down in process, and
it definitely sucks to conflate resource sharing with odd subprocess
management.  
  
**5. Layers are not Zopish**  
  
As far as I can tell, one of the themes of Zope 3 is small,
interchangeable pieces loosely joined together.  
  
Layers seem to be something that could have been done much better using
the Zope component architecture. Perhaps they could give `getUtility`
some practical purpose in life.  
  
**What then?**  
  
As much as I hate to say so, I don't think there's much hope for layers
as a concept. One is probably better served by replacing one's existing
layers with [testresources](https://launchpad.net/testresources). It
looks like it takes [quite a lot of work to do
so](https://bugs.edge.launchpad.net/launchpad-foundations/+bug/419691/comments/2).  
  
That's it. Five reasons and a lot of paragraphs. Please let me know if
I've made mistakes, or if newer versions of zope.testing are better.
Also, please gently correct me if I've left the path of [civility and
common courtesy](http://jcalderone.livejournal.com/47657.html).

