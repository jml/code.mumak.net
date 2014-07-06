Title: All the dude wanted was his rug back
Date: 2010-04-14 16:46
Author: Jonathan Lange (noreply@blogger.com)
Slug: all-dude-wanted-was-his-rug-back

All I wanted was to get [subunit](https://launchpad.net/subunit) output
from our test runner. I got it, but at a much higher price than I
expected to pay. This is my story.  

Quick and dirty, April 2009
---------------------------

It's often a good idea to try to get something working as quickly as
possible, even if the hack to get it working is a little dirty.  
  
For getting subunit output from our test runner, the *right* thing to do
is to change the `TestResult` object used by the test runner. In
Python's standard unittest and in most xUnit frameworks, `TestResult`
objects are responsible for reporting results to the user.  
  
If [zope.testing](http://pypi.python.org/pypi/zope.testing/) were
designed more in-line with other Python testing frameworks, this would
also have been the quick and easy way to do it.  
  
Sadly, zope.testing embeds quite a lot of logic necessary for the
execution of tests in its `TestResult` object, so I can't just swap it
out for one that implements the standard interface.  
  
Instead, I created a `MultiTestResult` object and added it to
[testtools](https://launchpad.net/testtools). It acts like a single test
result but dispatches to a bunch of test results.  
  
Then I did a quick and dirty thing to silence any output that
zope.testing's result object might have generated, and used
`MultiTestResult` to glue in a subunit test result. Since zope.testing
doesn't have a way of plugging in test results, I did some evil monkey
patching.  

Fix zope.testing, 5th February 2010
-----------------------------------

Now, what I *should* have done is fix zope.testing so that it had its
own way of generating subunit output cleanly.  
  
I didn't, because at the time Launchpad was using a very old version of
zope.testing. We couldn't upgrade because we were using Python 2.4 and
new Zope bits needed Python 2.5.  
  
However, eventually we got Python 2.5 support, upgraded our Zope Toolkit
bits and pieces and started using a newer version of zope.testing. Once
that happened, patching zope.testing became feasible, since I'd actually
be able to use the results of my labor.  
  
Looking at zope.testing, I would have to either disentangle the
layer-running logic from the `TestResult` code, or I would have to
implement my own “formatter”. Disentangling the layer stuff would be
way, way too much work, so I went for the formatter.  
  
A zope.testing `OutputFormatter` is an object that implements a very
big, undocumented interface and is responsible for displaying almost all
of the output that the Zope testrunner could possibly generate.  
  
To implement one, you have to implement twenty-seven methods, most of
which lack clear documentation or usage information. There are tests,
which is nice, but the tests are big integration tests, rather than unit
tests.  
  
Anyway, I implemented a subunit output formatter over the course of a
few weeks, then submitted it to the Zope community and got it landed.
Really, they are wonderful people.  
  
Next step, actually using this patch.  

Upgrade zope.testing, 13th March 2010
-------------------------------------

Upgrading zope.testing is easy enough. We use buildout, it's a simple
question of updating a version number in a configuration file, running a
few simple commands, wondering why it doesn't work, discovering it's a
local config issue, repeating two or three times and then you're done.  
  
Upgrading subunit was really hard. To explain why, I'll have to go into
some detail about the way Launchpad handles dependencies.  
  
We have three different kinds of dependencies:

1.  Source code dependencies
2.  Buildout dependencies
3.  Package dependencies

Each of them is managed differently, and updating each of them has its
own complexities. I ended up trying all of them.  

### Source code

Subunit was already included as a *source code* dependency. That means
that we had a branch with the Launchpad version of subunit, and that we
pull from that branch whenever we roll out or update our code. Kind of
like svn:externals, but managed with custom scripts.  
  
I needed to use a newer subunit than the one we already had in order to
get zope.testing subunit output working. To do that, I would have to
merge in changes from subunit trunk. Normally, that would be quite
easy.  
  
However, subunit has since upgraded its Bazaar repository format from
something old and crappy into the new, shiny and awesome 2a format. The
2a format is completely incompatible with older formats, and I cannot
merge from the new trunk into Launchpad's old subunit branch.  
  
I have no idea still how to upgrade Launchpad's old subunit branch. It's
a PQM-managed branch and I couldn't find documentation. Even if I could
upgrade the branch, I'd have no promise that the tools that our ops guys
use to rollout Launchpad would be robust in the face of a Bazaar
repository format change. The last thing I want to do is break a rollout
because I want to upgrade some developer tools.  

### Buildout

I then gave up on using source code dependencies and tried buildout,
which is our “recommended” way of handling dependencies.  
  
subunit is a tricky thing to handle with buildout. Buildout is at its
best when it's managing Python packages. subunit is not a Python
package. It's a multi-language project that builds into some binaries
and some libraries, including Python libraries. It uses autotools to do
all of this.  
  
There are ways to build autotools packages using buildout. You add the
egg for the “[cmmi](http://pypi.python.org/pypi/zc.recipe.cmmi)” recipe
to your dependencies and specify a particular build recipe for the
autotools package. This kind of worked, but it left me with two
problems.  
  
The first was that the Python libraries that it generated were buried
somewhere deep in the build output, and not included naturally in the
Python import paths as happens with a regular setup.py build. Not a big
deal, we can glue it together with symlinks.  
  
The second is that to build subunit, I actually needed cppunit and
check, and maybe some other things. I really, really don't want to
manually traverse the build dependency chain of subunit and add each of
these things as eggs to our buildout *just* so I can get subunit output
from our test suite.  

### Packages

Which naturally made me think of Debian packages. After all, what better
way to manage complex dependencies?  
  
Unfortunately, I really don't have any idea how to update the Debian
packages in [our
PPA](https://edge.launchpad.net/~launchpad/+archive/ppa). I asked on
\#launchpad-dev and quickly got some [helpful
advice](https://dev.launchpad.net/LaunchpadPpa) about how to do it.  
  
There's some `debian/` directory fiddling, changelog updating and so
forth. Then I use bzr-builder. Then I submit the branch to
l[p:meta-lp-deps](https://edge.launchpad.net/meta-lp-deps), which is
where we manage the code for the package, then I build it in the PPA.
The PPA build doesn't work because I didn't sign the code of conduct –
easily fixed.  
  
I try again and it works and it looks like all is right with the world.
Apparently though, I got something wrong. Luckily
[maxb](https://edge.launchpad.net/~maxb) fixed it for me while I slept
so I didn't need to do anything about it.  
  
Yay! I have now officially updated the version of subunit that we depend
on. Now all that's left for me to do is propagate that change and then
land my branch.  
  
To propagate the change, I need to update the EC2 images that we use for
running our tests. There's a command to do that and a [very helpful wiki
page with instructions](https://dev.launchpad.net/EC2Test/Image).  
  
I follow the instructions, and it doesn't work. The error is weird, and
to do with some crazy socket thing. No one has a clue what to do about
it, and I'm actually quite busy doing other things, so I leave it rest
for a couple of days.  
  
When I come back to try again, I google around for the error and
discover that it's actually a [bug in openjdk that affected the Lucid
beta
release](https://bugs.edge.launchpad.net/ubuntu/+source/openjdk-6/+bug/542395)
and has now been fixed. Hooray, I guess.  
  
I update my Lucid install and get ec2 to build the new image for
testing. Once that's done, I need to get our ops guys to update the
*completely different* set of images that we use on our buildbot.  
  
I send off a request, and there's a bit of back-and-forth. Apparently we
use one archive for development, which I've updated, and a completely
different archive for production rollouts, which I am not allowed to
update. After ten working days, it all gets sorted out, and now I am
able to land my branch.  

Landing the branch, 10th April 2010
-----------------------------------

At last, I'm ready to land my branch.  
  
It doesn't work. Of course.  
  
I could have sworn that I ran the full test suite with it, both with
subunit output and with the default, but it seems to be broken in two
ways.  
  
The first is that the subunit output support in zope.testing is broken.
I made the `error` method raise `NotImplementedError`. This means that
if ever a layer fails to start up properly, the test runner dies with an
unhelpful error that masks the layer's own error. Suck.  
  
The right way to fix it is to add a new API to the formatter to
specifically handle layer set-up errors. I take the quick-and-dirty
approach of just printing out whatever `error` gets. Patch is sent off
to zope-dev mailing list.  
  
The second is that new zope.testing has deprecated its `doctest` module,
and emits deprecation warnings all over the place. We have tests that
fail if warnings are emitted – sixteen, to be precise – so I can't
upgrade until I somehow stop the warnings.  
  
They are generated by zope.app.testing.functional in the Librarian
start-up. Why on earth the Librarian needs
[zope.app.testing](http://pypi.python.org/pypi/zope.app.testing) is
beyond me. I fetch zope.app.testing, work around [a bug in
python-setuptools](https://bugs.edge.launchpad.net/ubuntu/+source/distribute/+bug/490731)
to get it building, patch it and submit the patch to the zope list.  
  
If I wanted to, I could make two new eggs now for the two patched
projects and then just land the branch. I don't think I want to, since
the patches are so small I'm confident I can get them landed and maybe
even persuade someone to do releases.  
  
The fix to zope.app.testing lands without a hitch, and yet another kind
person from the Zope community does a release and even do what they can
to get the other patch landed.

<div>

However, it turns out that between zope.app.testing 3.7.3 and the new
3.7.5 that I need, zope.app.testing has started to depend on
[zope.component](http://pypi.python.org/pypi/zope.component) 3.8 or
better. zope.component has made some changes that break API
compatibility with a stack of other Zope bits, including
[zope.sendmail](http://pypi.python.org/pypi/zope.sendmail) and
[zope.app.component](http://pypi.python.org/pypi/zope.app.component).
zope.sendmail has been updated, but zope.app.component has not. I can't
find the code to patch it either.

</div>

<div>

Luckily, Launchpad doesn't really use the broken bits of
zope.app.component, so it's easy enough to [work around the
problem](http://bazaar.launchpad.net/~jml/launchpad/new-zope-testing/revision/10456)
there, and bump zope.sendmail's version in our buildout configuration.

</div>

<div>

Then the fix for zope.testing lands, and
[Sidnei](https://launchpad.net/~sidnei) is again kind enough to release.
I bump our versions.cfg, and land the branch.

</div>

<div>

It is finished.

</div>

<div>

Thoughts
--------

It should be obvious by now that I think the whole process has been
unreasonably complicated and taken far too long.  
  
Perhaps I chose a task that was fundamentally difficult. Perhaps it was
a one-off “perfect storm” of confounding factors. Perhaps there are
deep, serious problems in the way we do things. Perhaps I'm just not
very good.  
  
I certainly made some mistakes. For a start, I shouldn't have been so
afraid of breaking the edge rollout. We take measures like daily edge
rollouts precisely so that we can catch our mistakes, which should
embolden us to try things.  
  
I also should have done more testing between the time I asked for the
image updates and the time I landed the branch.  

</div>

<div>

I kind of like the way that Zope has been split out into a million
little projects. I think it made it easier for me to come along with my
small, opportunistic patches, and made it easier for others to review
and land them. It also makes it easier for stupid backwards
compatibility mistakes (since you can't just grep a tree). I somehow
think that if [Twisted](http://twistedmatrix.com/) broke itself up,
they'd find a way to deal systemically with backwards compatibility
changes, if only by blocking them in review.

</div>

<div>

Also, it would be pretty much impossible to use Zope at all without
[PyPI](http://pypi.python.org/).

</div>

<div>

I would love to know what you all think of this, and whether you have
any thoughts on how we can make hacking on Launchpad easier.

</div>
