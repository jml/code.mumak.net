Title: Useful, unpolished Bazaar plugin
Date: 2009-02-25 00:16
Author: Jonathan Lange (noreply@blogger.com)
Slug: useful-unpolished-bazaar-plugin

I've just pushed
[lp:\~jml/+junk/bzr-difftodo](http://code.edge.launchpad.net/%7Ejml/+junk/bzr-difftodo)
to Launchpad. It's a Bazaar plugin that:  

-   Finds the diff between your current branch and the submit branch
-   Looks in that diff for any Python comments that you've added or
    modified
-   Shows all the TODO or XXX items in Emacs "compile" format.

So the output looks something like this:  
  
\$ bzr todo  
Using submit branch /home/jml/repos/someproject/trunk  
lib/somefile.py:167:  
XXX: JonathanLange 2009-02-23: This matches the old search algorithm
that used to live in foobar.py. It's not actually very good -- really it
should match based on substrings of the unique name and sort based on
relevance.  
  
lib/otherfile.py:680:  
XXX: This is using \_cromulateSplonks -- a private method that no
longer exists.  
  
lib/anotherfile:779:  
XXX: I think that this can be moved into IAmAwesome.  
  
Things to do: 3  
  
The branch comes with an Emacs module bzr-todo.el. If you load this
module, you can just go "M-x branch-todo" in any file in a branch and
have the todo list come up in a compile buffer. Then you can just click
on any item to jump straight to it.  
  
The core code is pretty well tested, but everything around is really,
really rough. It works for me.  
  
I'd love some patches for it.

