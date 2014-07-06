Title: testtools moved to Github
Date: 2013-02-13 14:48
Author: Jonathan Lange (noreply@blogger.com)
Tags: testtools
Slug: testtools-moved-to-github

Those who closely follow
[testtools](http://pypi.python.org/pypi/testtools) development will
notice something unusual in the 0.9.28 release: we now [host the code on
Github](https://github.com/testing-cabal/testtools/) rather than [on
Launchpad](https://launchpad.net/testtools/).  
  
There are a few reasons behind the switch, but the biggest one is that
the ecosystem of tools and services around Git & Github is much, much
larger than that around Launchpad & Bazaar.  Already, by using Travis
(thanks [kampka](https://github.com/kampka/)!), I've been able to kill
off an old, cruddy, insecure Jenkins installation on my server, and
actually get proper testing across all of the Python versions that
testtools supports.  No more, "oops, I broke 3.2" again.  
  
We still [track our bugs on
Launchpad](https://bugs.launchpad.net/testtools/+bugs), because
Launchpad's bug tracker is still our favourite.  
  
Happy hacking!  
  

