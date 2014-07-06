Title: Make it really easy to fix bugs on Ubuntu
Date: 2010-11-15 14:36
Author: Jonathan Lange (noreply@blogger.com)
Slug: make-it-really-easy-to-fix-bugs-on

One of the best things that anyone ever said was, "not enough gets said
about the importance of abandoning crap". Mr Glass was probably talking
about writing, but his words could well have been aimed squarely at any
well-established software development process.  
  
Right now, it's too hard to [fix a bug in
Ubuntu](http://people.canonical.com/~dholbach/Fixing%20a%20bug.png).
There are [a lot of things that we can
do](https://blueprints.edge.launchpad.net/ubuntu/+spec/ubuntutheproject-community-n-improve-fixing-a-bug-workflow)
to make it easier, let me tell you about mine.  
  
If you see a small bug in a program on your desktop, you want to
something like this:  
  

1.  Figure out what package it's in
2.  Look for an existing bug, if not file one
3.  Get the source
4.  Build it, try to reproduce the bug
5.  Actually fix the bug
6.  Test to see that it's actually fixed
7.  Submit it then shepherd it through whatever processes come next

<div>

Much of this is monkey work if you know how to do it, or
incomprehensible arcana if you don't. Either way, it's important that we
abandon (or *automate*) this essentially uninteresting work.

</div>

<div>

In that spirit, at UDS I wrote a script that a lot of us have been
talking about for a long time. I called it
[start-hacking](https://launchpad.net/start-hacking), because I am
terrible at names and wanted to make a project. Right now, when you run
the script on your Ubuntu desktop, your cursor becomes a cross-hair.
When you click on an application, start-hacking will tell you the source
package that the application belongs to and where you can get the source
(both Ubuntu source and latest upstream if available).  It's very
simple, but that's because it builds on a very large amount of work that
Canonical has done, mostly through Launchpad and Apport.

</div>

<div>

Eventually, we want to make the script a much more beautiful application
that gets you a built, runnable copy of any Ubuntu application or
library in a test environment.  Our goal is to make fixing a typo (or
typo-level bug) as fast and as smooth as possible for any application on
the desktop.

</div>

<div>

All we need is a bit of time and a few volunteers.

</div>
