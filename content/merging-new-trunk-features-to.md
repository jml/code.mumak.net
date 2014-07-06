Title: Merging New trunk Features to a Development Branch (redux)
Date: 2008-07-05 11:08
Author: Jonathan Lange (noreply@blogger.com)
Tags: Uncategorized
Slug: merging-new-trunk-features-to

[Oubiwann](http://oubiwann.blogspot.com/) has [recently
posted](http://oubiwann.blogspot.com/2007/09/merging-new-trunk-features-to.html)
about the joys of using
[Combinator](http://divmod.org/trac/wiki/DivmodCombinator) to do
branch-based development using Subversion. I thought it'd be fun to do
the same post, except this time with Bazaar.  

### Background

  
You're working on a project called "Project", you have a copy of the
mainline branch (i.e. 'trunk') in your `src` directory.  

    ~$ cd ~/src/Project~/src/Project$ lstrunk

  
You want to implement a new feature, so you branch trunk to work on it:  

    ~/src/Project$ bzr branch trunk viking-feature-836

  
Bazaar is a version control system, not a PYTHONPATH-managing system, so
it doesn't maintain a global list of projects and the branches that are
currently active for each project.  
  
Perhaps your company focuses on historical invasions of Britain. You
decide to start work on another feature:  
lass objects.  

    ~/src/Project$ bzr branch trunk norman-feature-1066

  
You multi-task for a bit, until you finish 'viking-feature'. You decide
to merge 'viking-feature-836' into trunk.  

    ~/src/Project$ cd trunk~/src/Project/trunk$ bzr merge ../viking-feature-836~/src/Project/trunk$ bzr ci

  
At this point, you begin to suspect that Bazaar treats branches as
first-class objects. However, at this point, a developer on the obverse
side of your continent calls you,  
  
"Where's your viking feature? I need it to invade Britain!"  
  
"I've just put it into trunk. Have you got the latest copy?"  
  
"Yeah, I do, I just pulled from trunk."  
  
"It's in trunk, you fool! ... Oh, wait, gimme a sec."  

    ~/src/Project/trunk$ bzr pushPushing to bzr+ssh://bzr.example.com/Project/trunk...~/src/Project/trunk$

  
"Try now."  

### Merging

  
OK, enough background, let's merge.  
  
Say you need some of the changes in trunk in order to finish work on
your norman feature. No problems.  

    ~/src/Project$ bzr merge trunk norman-feature-1066~/src/Project$ bzr ci -m "Merge from trunk."

  
It's hard not to feel smug at this point.  
  
Wait a second, you also want to look at the experimental branch that a
friend is working on:  

    ~/src/Project/norman-feature-1066$ bzr merge bzr+ssh://yourfriend.example.com/branches/sealion-1946~/src/Project/norman-feature-1066$ bzr diff | less # better double check this one~/src/Project/norman-feature-1066$ bzr revert # nope, doesn't seem like a good idea

  

### Summary

  
Bazaar treats branches as first-class objects and treats trunk just like
any other branch. Although Combinator is great for branch-based
development in Subversion, it is more complex and less flexible than
doing branch-based development in Bazaar.  
  
With Combinator, you lose history when you merge in changes from trunk,
with Bazaar you don't.  
  
With Combinator, you can only merge in changes from trunk, with Bazaar
you can merge from any branch.  
  
With Combinator, merging from trunk leaves a bunch of changed files in
the trunk checkout on your system (this has tripped me up more than
once). With Bazaar, this doesn't happen.

