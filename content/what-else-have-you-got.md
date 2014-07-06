Title: What else have you got?
Date: 2010-11-18 18:16
Author: Jonathan Lange (noreply@blogger.com)
Tags: launchpad
Slug: what-else-have-you-got

I recently mentioned some of the [very important things we're doing on
Launchpad](http://code.mumak.net/2010/11/what-to-do-what-to-do.html)
(performance, privacy, derived archives and desktop integration) and
some of the equally [important things that
we're*still* doing](http://code.mumak.net/2010/11/still-going.html)
(making links, importing upstream translations, daily builds). We've
also got a few other things on the hob.  
  
In particular, there's some corking great work going on in making our
**build farm more scalable**. The build farm is used for building
[Ubuntu](http://ubuntu.com/), PPAs, building recipes and doing upstream
translation imports, so it's a critical part of our infrastructure.
We've been working to make better use of the machines we have, and make
sure that we don't actually degrade in performance as we add more
machines. There's also been a lot of good work here in making the code
more understandable and robust.  
  
Since we're now using the build farm for more things that just building
packages, we've had to give the UI some love, particularly in making
**[generalized build
histories](https://dev.launchpad.net/LEP/GeneralBuildHistories)** for
the builders. This just means making builder and archive pages on
Launchpad show all of the builds nicely, regardless of what type of
build they are. We're kind of finished here, we just need that lousy
[product strategist](https://launchpad.net/~jml) to get around to
reviewing the feature.  
  
On the bug tracker, we're adding a new facility that will **disable the
automatic duplicate detection on a package-by-package basis**. The dupe
finder is one of my favourite parts of Launchpad, and I would never
disable it for anything I do. However, the packages that take care of
providing sound, graphics and networking get a lot of bugs that have the
same symptoms but are actually completely different, and only an expert
can tell them apart. In these cases, auto dupe detection does more harm
than good, so we're providing a way to turn it off.  
  
Perhaps most excitingly of all the "non-core" work, we're working on
giving you **[far more control over your bug
mail](https://dev.launchpad.net/LEP/BetterBugSubscriptionsAndNotifications)**.
Launchpad has long been known for sending way too much email. We're
changing that.  
  
There's also some great stuff being done outside the Launchpad team:  

-   [DKIM-based mail
    authentication](https://dev.launchpad.net/LEP/DKIMAuthenticatedMail)
    (aka "Change bug statuses from GMail")
-   [Pre-forking lp-serve](https://dev.launchpad.net/LEP/ForkingLPServe)
    (aka "Shave two seconds off every bzr push to Launchpad")
-   [Bugzilla
    components](https://dev.launchpad.net/LEP/BugzillaComponents) (aka
    "One step closer to smooth upstreaming of bugs")
-   [**Branch merge
    queues**](https://dev.launchpad.net/Code/MergeQueues/LEP) 

<div>

And that's all of the stuff that's going on in Launchpad, as far as I
know.  Actually, there's a fair bit of work going on to make it so we
can deploy Launchpad way more often and work on features for as long as
we want without exposing them to unsuspecting users. And we're also
working on simplifying our branch landing machinery.  But that's it.

</div>

<div>

As you can see, there are a lot of things.  That means that progress on
any one thing is much slower than anyone would like.  However, progress
is being made.  Give us a few months and we might be working on only
three things at once, rather than over a dozen.

</div>

<div>

As always, if you're keen on following Launchpad development, you can
join \#launchpad-dev on Freenode, or our [developer mailing
list](https://launchpad.net/~launchpad-dev).

</div>

<div>

Coming soon: ideas for the not-so-distant future.  
  
**Edit:** Oops! Forgot merge queues.

</div>
