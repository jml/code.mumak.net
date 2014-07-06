Title: pyunit3k renamed to testtools
Date: 2008-10-04 04:04
Author: Jonathan Lange (noreply@blogger.com)
Slug: pyunit3k-renamed-to-testtools

After thinking and talking about it for ages, I've renamed 'pyunit3k' to
'testtools'. You can now find it at https://launchpad.net/testtools or
get your copy by running 'bzr branch lp:testtools'.  
  
This is the only major API change I plan to do without introducing some
sort of formal release process. The code as it stands is highly stable,
well tested and in use on production systems. Download it, use it, send
me patches.  
  
<span>Addendum</span>  
I forgot to mention that ITestResult has been removed, and thus the
undocumented dependency on zope.interfaces. If this matters to you,
please let me know.

