Title: Neat Bazaar feature
Date: 2008-07-05 10:40
Author: Jonathan Lange (noreply@blogger.com)
Tags: Uncategorized
Slug: neat-bazaar-feature_9205

Ever find yourself working away on a branch, enjoying yourself and
getting just a little carried away? Maybe you're working on a feature
and you notice and fix a bug that's not strictly related to that
feature.  
  
If you catch yourself in time, there's a nice little feature in Bazaar
that can help with this: `bzr merge --uncommitted`. It will merge in the
changes that you've made to your working tree but haven't committed
yet.  
  
e.g.  

    $ cd some-feature-branch... hack hack hack ... oops!$ cd ..$ bzr branch trunk bug-fix-2357$ cd bug-fix-2357$ bzr merge --uncommitted ../some-feature-branch$ bzr ci -m "Fix up bug 2357. Found this while working on some-feature."$ bzr send

  
  
Don't know what `bzr send` does? Trust me, you want to find out.

