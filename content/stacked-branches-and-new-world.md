Title: Stacked branches and the new world
Date: 2008-12-15 06:54
Author: Jonathan Lange (noreply@blogger.com)
Slug: stacked-branches-and-new-world

A few months ago, we rolled out a version of Launchpad that supports and
encourages <span>stacked branches</span>. This means medium to large
size projects are be able to use Launchpad for hosting their code. I
wrote this post shortly before the roll-out, but never got around to
blogging it. Hope you enjoy it.  
  
<span>The Problem</span>  
As far as code goes, Launchpad thinks in terms of individual Bazaar
branches. Each of these Bazaar branches stands alone, isolated from
other branches. Further, each of these branches has the full history of
whatever project they are a branch of.  
  
That means that every time you push a branch up to Launchpad, you have
to push the <span>entire history</span> of your project. That's not a
problem for small projects, but for large projects it's simply
unacceptable. It takes well over an hour for me to push up a branch of
Bazaar, for example.  
  
On our side, we simply don't have the space to store hundreds of copies
of the full history of every Free Software project in the world.  
  
<span>The Shape of the Solution</span>  
The answer to both of these problems is to share history information
between branches. That way, when you push a new branch, you would only
have to push up the data that's unique to that branch, the changes that
you've made locally. Similarly, we'd only need to store those changes,
rather than another full copy of the history.  
  
<span>Shared Repositories?</span>  
Experienced users of Bazaar might be wondering why we didn't just use
shared repositories. A repository is like a big bucket full of Bazaar
revisions. A repository can be made a shared repository, and branches
can be made to get their revisions from <span>that</span> repository,
rather than from their own. This works fine in many circumstances, but
for a public service like Launchpad, it's not good enough.  
  
First, people can put poison the bucket. If you can push up a branch,
you can write to the shared repository. If you can write to a shared
repository at all, then you can write to <span>any</span> revision in
that shared repository. This means malicious users could poison any
repository that they can push to. If we had a shared repository per
project, then malicious users could push up branches that change a
project's history.  
  
A shared repository per person, per project is not so bad, but it's not
so good either. In that model, users would have to push up the full
history of a project the first time they contributed a project.
<span>Blech.</span> The last thing we want to do is penalize someone for
contributing to a new project. Launchpad is supposed to make it easy for
you to get started.  
  
<span>Stacked Branches</span>  
A stacked branch is a branch that only has a little bit of its own
history. The rest of its history lives in another branch, what we call
the <span>stacked-on branch</span> (I don't like the name, but all the
better ones are taken). The Bazaar team has been working on making
Bazaar support stacked branches for much of this year.  
  
Stacked branches are exactly what Launchpad needs to get you pushing
your branches up quickly. When you push up a stacked branch, you only
need write access to the repository of <span>that branch</span>, you
only need to read the stacked-on branch. This eliminates the poisoning
problem, and allows revisions to be shared safely between branches.  
  
<span>How We Do It<span><span></span></span></span>  
For each project with a development focus (Launchpad's jargon for an
official trunk), Launchpad has a policy file that tells Bazaar that new
branches should be stacked on that development focus.  
  
So, you make a branch from trunk, do a bit of hacking locally, commit a
few revisions and push it up to Launchpad as your own branch, say
lp:\~jml/tribunal/awesome-new-feature. When you push, Bazaar asks
Launchpad where it should stack the branch, and Launchpad says
lp:\~jml/tribunal/trunk. Bazaar then pushes only the new revisions I've
added to my "awesome-new-feature" branch.  
  
We do a lot of stuff behind the scenes to make sure the branches work
over HTTP, bzr+ssh, SFTP and to make sure that mirrored branches work
just as well as hosted branches and so on. I hope that most of this is
invisible to you, and that you simply notice that pushing big branches
to Launchpad suddenly got a lot faster.  
  
<span>The Future</span>  
By making it possible to quickly push big branches to Launchpad, we've
entered a new era. Projects like Bazaar and Launchpad itself can start
actually hosting their branches on Launchpad. For other projects (like
Twisted, Python or even GNOME), hosting branches on Launchpad is now an
option that can be seriously considered.  
  
For my part, stacked branches are already changing the way I work. I'm
now using the product that I helped build each and every day as part of
my job. Further, my colleagues and my boss are also using it. This
quickly exposes rough edges and raises obvious ideas for improvement in
the rest of the Code site. It also helps me see which bugs are the
really important ones.  
  
More importantly, it's reminded me that Launchpad actually is pretty
cool. I'm using it more, and looking forward to the day when I can
really, genuinely say that Launchpad is a joy to use.

