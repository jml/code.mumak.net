Title: More bzr hacking
Date: 2008-10-06 06:39
Author: Jonathan Lange (noreply@blogger.com)
Slug: more-bzr-hacking

I've extended bzr-establish to give it a new command: hack.  
  
'bzr hack lp:foo' will create a repository with working trees called
'foo' and fetch the lp:foo branch into that repository.  
'bzr hack --repository \~/repos lp:foo' will create a repository in
'\~/repos/foo', a working tree area in 'foo', fetch the branch into the
repo and make a light-weight checkout in the working tree area.  
  
You can also specify a non-Launchpad branch, e.g. 'bzr hack
http://example.com/some/branch/trunk foo'. This will make a repository
called 'foo', put the branch in there and... well, you get the picture.  
  
The plugin lives at lp:\~jml/+junk/bzr-establish. It's buggy, not
particularly well tested and rough as guts. Still, it's worth a play.

