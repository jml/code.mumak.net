Title: A Modest Success
Date: 2012-11-09 14:18
Author: Jonathan Lange (noreply@blogger.com)
Slug: a-modest-success

Over the last few months, James Westby and I have been working on
automatic packaging. I want to talk today not about the thing itself but
rather how we go about making it, because I think that we have got a
fairly good process going.  
  
Here's what it looks like.  
  
**Conception**  
**  
**We pull the work that we do from a backlog of ideas and requests. For
example, a little while ago, we did some experiments that showed that if
we changed the way we mapped libraries to Ubuntu packages, we could get
much better results for automatically packaging binary apps. The project
to change this ended up in our backlog, and we recently decided to work
on it.  
  
Before we begin work, we like to have a definition of "done". We also
write down why we are doing this, and what our assumptions are. We then
break things up into tasks. Maybe I'll dig into this another time.  
  
**Guts**  
**  
**Most of what we do goes in a loop:  
  

1.  Make a branch
2.  Work on it
3.  Propose for merging
4.  Code review
5.  Automated tests-then-land
6.  Automatically triggered staging deploy
7.  Manual "is it deployable" check
8.  Request production deployment from webops 

<div>

We use Bazaar for version control and we use Launchpad for hosting code
and doing code review. Here's [an example
one](https://code.launchpad.net/~jml/pkgme-service/remove-django-fixture/+merge/131424).

</div>

<div>

Code review is quite often fairly boring. My guess is that one in ten
actually provoke interesting changes. Most of our branches make small
changes, all of our changes are covered with tests, and we have
confidence in our test suite and our ability & willingness to make
follow-up improvements. Thus, rather than seeing code review as our last
line of defence for ensuring code quality, it's an opportunity to learn
and to perhaps accelerate the process by spotting problems earlier.

</div>

<div>

Once a merge proposal is approved, magic happens.

</div>

<div>

In this case, "magic" is a Jenkins instance that uses tarmac to poll
Launchpad to figure out which merge proposal are approved and thus ready
to land.  It runs our test suite, and if it passes, lands the change. If
it fails, it posts the failure to the merge proposal and our IRC channel
and marks it as needing more work.  
  
It's important here that our test suite is fast, that it's reliable, and
that it gives useful error messages when things fail.

</div>

<div>

When the change is to a dependency, then we run the tests of the things
that depend on it with the latest change.

</div>

<div>

After a successful change to trunk, we have a Jenkins job that triggers
an automatic deployment to our staging server.

</div>

<div>

All of this takes less than five minutes.

</div>

<div>

Once it's on staging, our "QA" website lists it as a revision that needs
to be manually verified. What we do there isn't really QA, but instead
making sure that if we roll it out to production, we won't break
anything. As with code review, we are confident in our ability to fix
things later.   

</div>

<div>

We tend to do these in batches, as our webops are insanely busy. Once
we've got a group of changes that are safe to deploy to production, we
ping the webops, who then (I think) run a single command that deploys to
production very quickly. Sometimes because of interrupts, it can take
twenty minutes to an hour to get someone to do this.

</div>

<div>

**Completion**

</div>

<div>

At this stage, we return to our definition of done and check to see if
the change actually provides the value we thought. 

</div>

<div>

Because automatic packaging is an inherently fuzzy problem, we run a
barrage of real world data through the new system to see if the recent
changes actually help. This also generates interesting qualitative data
that gives us hints on where we might want to work next.

</div>

<div>

**Principles**

</div>

<div>

**  
**

</div>

<div>

This is the end result of a lot of work, mostly by James Westby with me
cheerleading from the sidelines. We've iterated through it a lot, making
things faster and more reliable, generally by going from polling to
events, by cutting out unnecessary review steps, and by making
visibility improvements for when things are broken.

</div>

<div>

Underlying it all are a few principles that we have found to be either
true or useful:

</div>

<div>

-   a thing is not done until users are happily using it
-   more strongly, a thing is not valuable until users are happily using
    it, until then it is wasted effort 
-   we should be able deploy any change in the main code or a dependency
    within minutes at any time, every time
-   all deployments must be from trunk, all revisions of trunk must be
    tested and known-good
-   we can avoid a lot of needless effort by asking ourselves why we are
    doing what we doing, and by being explicit about our assumptions
-   regressions are intolerable, everything else is tolerable, because
    we can, will and do fix it

<div>

Rather than spend time shaping up this information into a pitch for why
doing things our way will bring you fortune and glory, we just want to
use this post to do the bare minimum of making what we are doing known
more broadly.  
  
Do you do something similar? Is there something above that you would
like to know more about? Are we making claims that seem a bit
far-fetched? Are any of our principles BS? Have you tried working toward
goals like these?  
  
We would really love to know and to hear from you. It will help us get
better. Also, I've deliberately fudged some stuff, so it'd be great to
get called out on that.  
  
Thanks to James Westby for reviewing this post. All errors are mine.  
  

</div>

</div>
