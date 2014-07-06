Title: Larval prototype for Launchpad dashboards
Date: 2010-12-23 16:09
Author: Jonathan Lange (noreply@blogger.com)
Tags: launchpad
Slug: larval-prototype-for-launchpad

I mentioned [a while
ago](http://code.mumak.net/2010/11/and-then-what.html) that I really
want to see something like a dashboard in Launchpad, some kind of view
that shows you everything that you *must* do, everything that you are
waiting on from others and all of your current work-in-progress.
Launchpad could do this really well, since it has rich, inter-linked
data about what's going on and since it can show you this information
for all of your projects.  
  
Today, I knocked up a very quick-and-dirty prototype for this. It shows
all of the work-in-progress for a person across all of Launchpad,
grouped by project.  
  
The code lives at
[lp:\~jml/+junk/whip](https://code.launchpad.net/~jml/+junk/whip) and
you can see examples of [my
work-in-progress](http://people.canonical.com/~jml/jml-wip.html) and
[jelmer's
work-in-progress](http://people.canonical.com/~jml/jelmer-wip.html)
online. You should be able to make your own with './bin/whip \$LP-NAME
\> wip.html'. Note that there'll be some PYTHONPATH shenanigans.  
  
Hackers, I'd love to see if you could turn this prototype into a
web-app, or even a page on Launchpad. There's a NOTES file in there with
whatever ideas I've had.  
  
Designers, there's got to be a better way of showing this data than what
I've picked. Take a look at the examples and see what you can turn them
into.

