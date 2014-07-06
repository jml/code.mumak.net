Title: OK I lied
Date: 2008-07-05 10:09
Author: Jonathan Lange (noreply@blogger.com)
Tags: Uncategorized
Slug: ok-i-lied_17

The next post is actually about a Bazaar plugin that I've now got ready
to share. To get it, 'bzr branch lp:\~jml/+junk/merged-branches'.  
  
Once you've got it, run 'bzr merged-branches' in the trunk of your
project. It will then show you all branches in sibling directories that
are safe to delete.  That is,  

-   They have no uncommitted changes.
-   They have no "unknown" files. (Files outside of version control that
    haven't been explicitly ignored.)
-   They have no shelved changes. The plugin will only check for this if
    it can find bzrtools.

  
The branch is now at the point where it works for me, but it still
belongs in '+junk' — here's why:  

-   It assumes that you have a trunk branch in the same directory as all
    of your other branches.
-   It assumes that branches and working trees are the same thing.
-   It's called 'merged-branches' when it really means 'safe-to-delete'.
-   It doesn't make it easy to see why a branch is *not* safe to delete.
-   It doesn't let you customize the conditions of the search. Maybe you
    want to see all branches with uncommitted changes.

  
Still, if you are like me and make a lot of branches, it's quite useful.
I'll tolerate bugs, accept patches and welcome encouragement.

