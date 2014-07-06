Title: Neat trick
Date: 2009-02-21 00:11
Author: Jonathan Lange (noreply@blogger.com)
Slug: neat-trick

In Argentina I hacked up a little command for the 'launchpad' Bazaar
plugin. It's a command line tool to open the Launchpad page for your
branch in your web browser.  

      $ cd ~/src/testresources/expose-reset-bug-271619 $ bzr lp-open Opening https://code.edge.launchpad.net/~jml/testresources/expose-reset-bug-271619 in web browser

... and it works!  
  
Available in Bazaar 1.12. Due to an unfortunate oversight, the NEWS file
doesn't mention it.

