Title: Cool Launchpad/Bazaar hack
Date: 2008-07-25 05:52
Author: Jonathan Lange (noreply@blogger.com)
Slug: cool-launchpadbazaar-hack

If you push a lot of Bazaar branches to Launchpad, you might want to add
something like this to your .bazaar/locations.conf:

    [/home/jml/Code]public_branch = lp:~jmlpublic_branch:policy = appendpathpush_location = lp:~jmlpush_location:policy = appendpath

Once it's there, 'bzr push' will Just Work... as long as you want it to
do something like:

    jml@rhino:~$ cd ~/Code/pyunit3k/trunkjml@rhino:~/Code/pyunit3k/trunk$ bzr pushUsing saved location: lp:~jml/pyunit3k/trunkNo new revisions to push.

So if I've got a branch in `~/Code/<project-name>/<branch-name>`, it'll
be published at
`https://launchpad.net/~jml/<project-name>/<branch-name>`. This is only
a default, of course: you can override it for a given branch by doing:

    bzr push --remember <new_location>

Or you can override it for a bunch of branches by hacking
locations.conf.  
  
Neat huh?

