Title: Another Bazaar story
Date: 2008-07-05 10:09
Author: Jonathan Lange (noreply@blogger.com)
Tags: Bazaar
Slug: another-bazaar-story

I'm currently hacking away on Launchpad's support for "[stacked
branches](http://jam-bazaar.blogspot.com/2008/05/this-week-in-bazaar_29.html)",
something that will really make Launchpad's codehosting a joy to use.  
  
At the moment, I'm writing some tests that require a user to login. This
was becoming a bit cumbersome, until I remembered something: Tim has
recently landed some code to make this easy. But how do I get these
changes without messing up all of the work I'm doing now? bzr shelve to
the rescue!  
  
'shelve' interactively goes through each change you've made to your
current working tree and allows you to decide whether to keep a change
or shelve it. It comes with a twin command 'unshelve', which lets you
interactively restore your changes.  
  
In this case, I don't even care about the interactivity, so here's what
I did:  

    # Shelve my changesbzr shelve --all# Fetch the latest trunkcd ../trunkbzr pull# Merge it into my branchcd ../stackingbzr merge ../trunkbzr ci -m "Merge in changes from trunk to get login testing improvements."# Restore my changesbzr unshelve --all

  
  
The 'shelve' command comes with the
[bzrtools](http://launchpad.net/bzrtools) plugin, and I am basically in
love with it.  
  
As a parting shot, I should mention that things like bzrtools aren't
accidents. They are natural and inevitable when you have [good
APIs](http://starship.python.net/crew/mwh/bzrlibapi/bzrlib.html) in a
[high-level language](http://python.org) and a [very nice plugin
system](http://bazaar-vcs.org/WritingPlugins).  
  
And now I'm off to keep working on this branch.  
  

