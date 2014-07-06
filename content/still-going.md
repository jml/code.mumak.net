Title: Still going
Date: 2010-11-04 17:24
Author: Jonathan Lange (noreply@blogger.com)
Slug: still-going

Last post, I talked about the [top priorities for Launchpad development
right now](http://code.mumak.net/2010/11/what-to-do-what-to-do.html):
performance, privacy, derivative distributions and desktop integration.
In this post, I want to talk about the other things that we are doing,
and why we are doing them at all.  
  
In September last year, we decided that we needed to put a lot of work
into something that is at the core of the very idea of Launchpad:
bridging the gap between Linux distributions (specifically Ubuntu) and
upstream open source projects. Launchpad has been intended from the very
beginning to smooth out and accelerate collaboration between these two
areas of endeavour.  
  
Much of that work has already been done, but we have three initiatives
still going: **making links, daily builds **and **importing upstream
translations**.  
  
  
**Making links** is all about making it incredibly to add useful, usable
information about package / upstream relationships. Launchpad has always
had the ability to store such information, but now it's much, much
easier to use because of a whole suite of changes: automatic suggestions
for upstream / distro links; simplified project configuration; automatic
linking to projects when marking a bug as upstream; just-in-time project
registration etc. There are a few more bugs to go before we're happy to
call it done.  
  
**Daily builds** are a very cool feature that's still in beta. You
provide us with a "recipe" that tells Launchpad how to combine branches
into something resembling a source package, then we take that recipe,
assemble the source package, build it and then publish it into a PPA of
your choice. Then, if the branches change, we'll provide a new build
each day. The feature mostly works right now – Project Neon are using it
to get [nightly builds of
Amarok](https://launchpad.net/~project-neon/+archive/ppa) – but the UI
needs polish, there are a few system-level
[glitches](https://bugs.launchpad.net/launchpad-code/+bug/669703) and
we're [asking
questions](https://bugs.launchpad.net/launchpad-code/+bug/608450) about
the recipe format. I'll be posting later about how to get involved with
the beta.  
  
**Importing upstream translations** into Ubuntu makes it much easier for
Ubuntu to be the best-translated Linux distribution ever. Right now it's
already possible to import translations from upstream projects into
Launchpad. Soon those translations will be imported directly into the
equivalent Ubuntu packages too, which means that Ubuntu translators can
choose to use the upstream translation or instead provide a better one.
Before we can do that, we'll need to do some scalability work. After
that's done, we'll also want to do some UI work to make it very easy to
connect the Ubuntu package translations to the imported upstream
translations.  
  
All in all, three very neat initiatives to bring Ubuntu and its
upstreams closer together.  
  
So that's it right? What with **performance**, **derivative
distributions**, **privacy** and **desktop integration** as well as
**making links, daily builds **and **importing upstream translations**,
the Launchpad team must have its plate full? Indeed not! Stay tuned, and
I'll let you know what other things we are currently working on, as well
as the future plans that are bubbling away.

