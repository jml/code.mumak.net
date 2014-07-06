Title: Command line apps
Date: 2011-08-01 10:59
Author: Jonathan Lange (noreply@blogger.com)
Slug: command-line-apps

Back in the day, I used to want to use
[twisted.python.usage](http://twistedmatrix.com/projects/core/documentation/howto/options.html)
for all of my command-line apps. It's a fairly nice
[API](http://twistedmatrix.com/documents/8.2.0/api/twisted.python.usage.html)
& a good way of writing code.  

<div>

Since I started writing Bazaar plugins though, I've fallen in love with
Bazaar's command interface.
[Jamu](https://code.edge.launchpad.net/~jkakar) has too, so he wrote
[Commandant](https://edge.launchpad.net/commandant). I don't really
understand it though, which is mostly for lack of trying.

</div>

<div>

Michael turned our internal EC2-using testing tool into a bzr-a-like app
[using the Bazaar
APIs](http://bazaar.launchpad.net/~launchpad-pqm/launchpad/stable/annotate/head:/lib/devscripts/ec2test/builtins.py).
There's a bit of duplication, but it works pretty well.

</div>

<div>

The Bazaar developers are aware that their command-line interface code
rocks and that it's too closely bound to Bazaar. I'm not sure whether
anyone has filed bugs about it or not, but here's what I actually want:

</div>

<div>

-   The subcommand interface, e.g. "bzr foo"
-   Option parsing
-   Help
-   Command aliasing
-   Error handling
-   Progress display
-   Verbosity control 
-   Logging
-   Debug helpers (e.g. The way bzr handles Ctrl-\\)

<div>

There's also a bunch of cool stuff in Bazaar that's useful for a lot of
applications, command-line or not.

</div>

<div>

-   Registries
-   Transports
-   Hooks
-   Configuration files
-   Oh yeah, **plugins**. (How could I have forgotten this?)

<div>

Sometimes I wish projects like Bazaar and Twisted split this sort of
stuff out into separate packages. That would probably change the way the
packages are maintained, and I don't know whether it would be for better
or for worse.

</div>

<div>

Sadly, no moral or action for this post. Just stuff that's been on my
mind that I wanted to write down and publish. I'd very much welcome
input.  
  
**Update:** Was rewriting this post, then realized that, umm, well, it
was a rewrite.

</div>

</div>

</div>
