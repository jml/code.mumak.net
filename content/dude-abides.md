Title: The Dude Abides
Date: 2010-04-20 10:02
Author: Jonathan Lange (noreply@blogger.com)
Slug: dude-abides

Last one on this topic.  
  
After I [broke the
rollout](http://code.mumak.net/2010/04/plane-has-crashed-into-mountain.html)
by [switching the subunit
dependency](http://code.mumak.net/2010/04/all-dude-wanted-was-his-rug-back.html)
from being managed in a branch to being managed with Ubuntu packages, I
thought my patch had to be reverted.  
  
But no! [Francis](https://launchpad.net/~flacoste) got angry enough to
fix the underlying problem. He split the [script authentication out of
our`lp.testing`
package](https://code.edge.launchpad.net/~flacoste/launchpad/bug-559128/+merge/23504)
, so we no longer use `lp.testing` – or subunit – in production. The
patch [missed a
spot](https://code.edge.launchpad.net/~jml/launchpad/no-testing-on-prod-bug-559128-devel/+merge/23655),
but that was easily fixed.  
  
Launchpad is rolling out regularly as ever, and my
[zope.testing](http://pypi.python.org/pypi/zope.testing) upgrade is
lying snug in the trunk.  
  
Lessons? I guess that anger is a powerful and
[constructive](http://life.mumak.net/2008/10/truth.html) force in
programming. That help from someone else is valuable for both the help
itself and for the boost in motivation that it brings. That software is
plain hard. That crying "Lean, Lean" isn't enough.

