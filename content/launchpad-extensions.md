Title: Launchpad extensions
Date: 2009-10-15 09:26
Author: Jonathan Lange (noreply@blogger.com)
Slug: launchpad-extensions

Launchpad has a pretty awesome [public
API](http://edge.launchpad.net/+apidoc), implemented using
[lazr.restful](https://launchpad.net/lazr.restful). I've written a few
small scripts for it, and the Launchpad team has a few scripts that they
use internally for doing admin tasks.

<div>

The Ubuntu Platform team does a heap of stuff with the Launchpad API.
[James Westby](http://jameswestby.net/weblog) has been using it to make
sure that there's a branch on Launchpad for every single package in
Ubuntu.

</div>

<div>

There's all this great work, but there's been nothing to tie the room
together. I've seen hardly any discussion about how to write Launchpad
API applications, or how to test them, or how to get
[launchpadlib](https://launchpad.net/launchpadlib) working in GTK+. I
haven't even seen much code sharing.

</div>

<div>

So, borrowing a trick from Twisted's [tx](https://launchpad.net/tx)
super-project, I've created an '[lpx](https://launchpad.net/lpx)'
project group on Launchpad. Bring it your scripts, your applications,
your huddled masses. If you want to know more about the API, look at the
[API help page](http://help.launchpad.net/API).

</div>

<div>

Thanks to [Mark](http://markshuttleworth.com) for reminding me that this
is important.

</div>


