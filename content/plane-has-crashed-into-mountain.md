Title: The plane has crashed into the mountain
Date: 2010-04-15 17:55
Author: Jonathan Lange (noreply@blogger.com)
Slug: plane-has-crashed-into-mountain

In [my previous
post](http://code.mumak.net/2010/04/all-dude-wanted-was-his-rug-back.html),
I described all of the steps that I and several others took to get [my
upgrade](https://code.edge.launchpad.net/~jml/launchpad/new-zope-testing/+merge/21539)
to [zope.testing](http://pypi.python.org/pypi/zope.testing) landed.

<div>

There has been a problem. [subunit](https://launchpad.net/subunit) is a
dependency of the launchpad-developer-dependencies package, since it's
only there for running tests.

</div>

<div>

However, subunit is being imported by our core test support package,
`lp.testing`. That package is being imported by the webapp in
production. launchpad-developer-dependencies is not installed in
production, launchpad-dependencies is instead. Now that I've removed
subunit from our sourcecode dependencies, subunit is no longer installed
on production.

</div>

<div>

I broke the rollout.

</div>

<div>

The real problem, apparently, is that we are importing lp.testing in
production. That problem always existed, but my patch made it known. And
now that we know it, we can't have unnecessary packages installed on our
production systems. Not that installing subunit as a package would be
any *worse* than running a production system that relies on really old
non-packaged version, but sometimes you've got to draw a line in the
sand. Across this line, you do not—

</div>

<div>

Anyway. Since installing subunit as a package is unacceptable, my patch
must be reverted, as well as the [ec2 test
improvement](https://code.edge.launchpad.net/~jml/launchpad/subunit-by-default/+merge/18449)
I did based on it. I can land it again when we have fixed the “real”
problem of production code importing test code.

</div>

<div>

**Update:** Just to be crystal clear, I've talked about this and the
previous post with my manager before I posted. Both of us want to
understand the underlying problems and solve them.

</div>
