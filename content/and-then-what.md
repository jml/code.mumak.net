Title: And then what?
Date: 2010-11-16 15:03
Author: Jonathan Lange (noreply@blogger.com)
Tags: launchpad
Slug: and-then-what

By now, you know where Launchpad is at. You know what [our top
priorities](http://code.mumak.net/2010/11/what-to-do-what-to-do.html)
are, you know the [other important stuff that we're still working
on](http://code.mumak.net/2010/11/still-going.html), you know [the other
bits and pieces we've got
going](http://code.mumak.net/2010/11/what-else-have-you-got.html). You
might even know why.  
  
What you might not know, and what this post hopes to tell you, is what
we are *thinking* about right now. Humans are plan-making creatures, and
product strategists perhaps more so than most. What follows is a brief
description of the half-formed thoughts and plans that I have for
Launchpad. (Also, have I mentioned the
[roadmap](http://dev.launchpad.net/RoadMap) yet?)  
  
Strategically speaking, there are two major approaches we can take to
our work on Launchpad. The first is working on things that bring new
users and new projects to us. This would mean finding something that we
can provide that alternatives don't and potential users want, *or*
assuming that we already have such a thing, find the blockers that stop
people from using Launchpad and remove them (the blockers, not the
people).  
  
For example, if we thought that open source developers wanted their
hosting site, say, to be part of the semantic web, we could go and do
that and be relatively confident that no one else will. That would be
finding a competitive advantage.  
  
Or, to take another example, we could say that our awesome bug tracker,
our translation support and daily builds are heaps plenty good
advantages, but people don't use Launchpad because we only have full
support for one VCS and we provide no place to host a project shop-front
web site. That would mean adding Git, Subversion and Mercurial support,
and adding some kind of wiki / webhosting. Personally, I find this much
more appealing than semantic web shenanigans.  
  
All of that's one strategic approach: attract new users. There's another
major approach that we could take: make things better for our current
users. All things considered, I think I want to take the second
approach.  
  
There's so much we could do here, partly because Launchpad itself is so
broad. Some key things stand out though.  
  
First, there is a cluster of problems related to the way that people
approach the website. Although we tout cross-project collaboration as
one of our big things, we don't make it particularly easy. We need to
provide each user and each team with a view that shows them all of the
things that are interesting to them across all of Launchpad. In fact, we
probably need to give them two views: one that's historical and
chronological, and another that's forward looking and more
dashboard-like. In my head, I've been thinking of this as **walls** (ala
Facebook) and **dashboards**.  
  
If we dig into this, there'll be other changes: better, fairer karma;
more social interaction; better person, project and team pages; a
"waiting for" section in the dashboard so you can see who to hassle; a
better experience for new users; and probably death to the home page for
users who've got accounts. Lots of goodness here.  
  
Second, it's becoming increasingly clear that blueprints are a good idea
with a sub-standard implementation. Persuaded largely by Matthew Paul
Thomas, I think that we should merge the blueprint tracker with the bug
tracker to make a **[combined issue
tracker](http://dev.launchpad.net/IssueTracker)**. A lot of people get
worried when I say this, because they really like blueprints and they
understand that bugs and blueprints are actually two different things.
Please don't worry. There will almost certainly always be something in
Launchpad like a blueprint or specification that is visibly different
from a bug. However, I think we ought to change what lists they appear
in, what statuses they have and many other things. The loss of
distinctiveness will be more than made up for with an increase in
capability.  
  
Third, the way we **search** and the way we display results of searches
needs to be revamped to be faster and more flexible. I want to see easy
forms, a good search string mini-language, sexy URLs, searches that can
be saved and shared.  
  
There's so much more that we could do, that we ought to do: make mailing
lists rock; inline commenting on merge proposals; eliminate all of the
silly "refresh this page" business that we still have; go to series and
milestones with a sharp axe and a clear conscience; provide top-notch
tools for QA teams; show way more cool stuff based on our data; make
filing bugs upstream a complete no-brainer; clean up the terminology we
use for naming things; provide an event sending interface for
launchpadlib so that people don't have to poll. I could go on for a very
long time.  
  
I call out the three things above – cross-project views, merging bugs
and blueprints and better search – because I think they are things that
will make Launchpad better for absolutely everyone who uses it. In
particular, done right, good cross-project views turns a weakness into a
strength. It takes the vast, daunting size of Launchpad and instead
turns it into a huge realm of opportunity.  
  
Now, none of this is fixed in concrete. There's still plenty of time to
discuss, plan out, change our minds and what not. But it's what's in my
head right now.  
  
That's it. Right now, we're working on **privacy**, **performance**,
**derived archives** and **desktop integration** as our top priorities.
We're still plugging away at **daily builds** and **making links**
between distributions and upstreams, and we're working on a host of
useful, important things. In the future, if my plans go as … planned,
then we'll have **dashboards**, activity **walls**, a **combined issue
tracker** and excellent **search**.  
  
What do you think?

