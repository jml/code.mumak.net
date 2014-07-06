Title: Bazaar hacking
Date: 2008-10-04 13:05
Author: Jonathan Lange (noreply@blogger.com)
Slug: bazaar-hacking

I spent a little bit of time mucking around with some Bazaar plugin
ideas I've had.  
  
The first is a command that switches from "branches and trees together
inside a shared repository" to "treeless repository with lightweight
checkouts". I ran it against a couple of my local repositories and it
works out rather nicely. If you are thinking of using cbranch and the
like, you should have a look at this plugin. If you don't know why it's
a good idea, well, umm, maybe one of the [other people on the
Planet](http://planet.bazaar-vcs.org) will blog an answer.  
  
The second adds 'bzr new' to the command list.  
\$ bzr new awesomer  
  
will create a new shared repository called 'awesomer' and a new branch
in that repository called 'trunk'. If you think trunk is a terrible
name, you can do:  
\$ bzr new awesomer devel  
  
If you are like Tim or Aaron, you'll want your repository and branches
separated from your working tree:  
\$ bzr --repository \~/repos/foo foo devel  
  
I'd like to figure out a nice way of letting users specify a default
directory for repositories to go into, for those people who always use
the split model.  
  
The plugin with both of these commands can be found at
https://code.edge.launchpad.net/\~jml/+junk/bzr-establish. As the "junk"
in the name indicates, it's really rough code.  
  
If either of these features sound like good ideas to you, let me know!

