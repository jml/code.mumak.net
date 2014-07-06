Title: juju debug-hooks
Date: 2012-06-26 13:43
Author: Jonathan Lange (noreply@blogger.com)
Slug: juju-debug-hooks

OK, I think I've figured it out.  
  
[juju debug-hooks](https://juju.ubuntu.com/docs/hook-debugging.html)
replaces hooks for a service unit with an interactive terminal session.
You run it, it launches [tmux](http://tmux.sourceforge.net/) (which
seems to be a thing like screen or byobu), and when a hook for that
service unit runs, it *won't* run the hook in the charm, rather it opens
a new window and you can then do whatever you want in that. Including
manually running the hook in the charm.  
  
debug-hooks doesn't actually do anything to your hooks, nor does it
increase the amount of information available to you (e.g. by increasing
log verbosity). It just replaces hooks with terminal sessions.  
  
You have to know the service unit first, e.g. libdep-service/41.  
  
It seems as if it's a really common thing to want to use debug-hooks on
install. There doesn't seem to be any smooth way. As far as I can tell,
you have to run 'juju deploy', run 'juju status', quickly note the unit
name and then run 'juju debug-hooks'.  
  
That aside, it's very useful. I found myself using it to edit hooks (and
puppet files used by my hooks) and re-run them until they worked.  
  
Still don't know easy way of exporting changes to a charm on a unit back
down to my laptop.  
  

