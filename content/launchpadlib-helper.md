Title: launchpadlib helper
Date: 2011-08-02 11:05
Author: Jonathan Lange (noreply@blogger.com)
Slug: launchpadlib-helper

I often need to muck around in a Python interpreter to figure out what I
need to do with [Launchpad's API](https://help.launchpad.net/API). As it
is, I write out the same commands over and over.  
  
Since repetition is a stupid boring job that we should force machines to
do while they are still subservient, I wrote [a
harness](http://paste.ubuntu.com/657088/) that, when run, gives you a
Python interpreter and a few useful objects for playing with the
Launchpad API.  
  
For example:  
  

    $ ./lpharness.py lp:     authenticated Launchpad objectme:     logged in useranon:   anonymous Launchpad objecterrors: launchpadlib.errorsuris:   launchpadlib.urispprint: pretty printer>>> pprint(list(me.searchTasks(status='In Progress')))[<bug_task at https://api.launchpad.net/1.0/launchpad/+bug/240067>, <bug_task at https://api.launchpad.net/1.0/launchpad/+bug/418932>, <bug_task at https://api.launchpad.net/1.0/hydrazine/+bug/535414>, <bug_task at https://api.launchpad.net/1.0/hydrazine/+bug/574981>, <bug_task at https://api.launchpad.net/1.0/hydrazine/+bug/612641>, <bug_task at https://api.launchpad.net/1.0/tarmac/+bug/683351>, <bug_task at https://api.launchpad.net/1.0/wikkid/+bug/695232>, <bug_task at https://api.launchpad.net/1.0/launchpad/+bug/721166>, <bug_task at https://api.launchpad.net/1.0/ensemble/+bug/728320>, <bug_task at https://api.launchpad.net/1.0/bughugger/+bug/731075>, <bug_task at https://api.launchpad.net/1.0/tarmac/+bug/807785>, <bug_task at https://api.launchpad.net/1.0/pkgme/+bug/809447>, <bug_task at https://api.launchpad.net/1.0/ubuntu-archive-tools/+bug/805634>]

<http://paste.ubuntu.com/657088/>  
  
You are free to do whatever you like with it. I hope that someone puts
it into some useful, *maintained*, centralized place for doing stuff
with Launchpad. Perhaps launchpadlib itself.  


