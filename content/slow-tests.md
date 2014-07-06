Title: Slow tests
Date: 2009-09-01 08:37
Author: Jonathan Lange (noreply@blogger.com)
Slug: slow-tests

[Robert Collins](http://www.advogato.org/person/robertc/) of
[Bazaar](http://bazaar-vcs.org), recently blogged about the [cost of
slow tests](http://www.advogato.org/person/robertc/diary/113.html). I
couldn't agree more.  
  
[Launchpad](http://launchpad.net) has a very slow test suite. It takes
upwards of five hours to get a change into [our "known good"
branch](https://code.launchpad.net/%7Elaunchpad-pqm/launchpad/stable).
It's been a source of pain for the team for years, and now that
Launchpad is Free Software, it's becoming a pain to new contributors.  
  
We've tried a few things to deal with it, none of them great. First up,
we've got a tool for running the test suite on EC2 instances. It's nice,
but it's still too slow. I've written a "[faster
tests](https://dev.launchpad.net/FasterTests)" spec outlining some of
the options we have; but specs never got software written. Likewise,
there are a bunch of bugs flagged as
[build-infrastructure](https://bugs.edge.launchpad.net/launchpad-project/+bugs?field.tag=build-infrastructure),
many of which address the slow test sped. We also have a rotating
"[Build Engineer](https://dev.launchpad.net/BuildEngineer)" position
within the team to address those bugs.  
  
<span id="formatbar_Buttons"><span id="formatbar_CreateLink"
class="on down" title="Link">It's probably not enough though. From
watching Rob's blog posts, and the emails to the Bazaar mailing list, I
think that what Launchpad really needs is someone with a passion for
solving the problem (i.e. making Launchpad hacking fun) who is willing
to lead the way, and a full commitment from the rest of the team for
getting the runtime down and keeping it there.  
  
More on this later.  
</span></span>

