Title: Get started with launchpadlib
Date: 2010-03-10 10:43
Author: Jonathan Lange (noreply@blogger.com)
Slug: get-started-with-launchpadlib

In my spare time, I sometimes talk to people about how they can get
started with launchpadlib hacking.  
  
launchpadlib is the Python client-side library that talks to Launchpad's
own [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer)
API. It turns out that customize scripted control of a
[bug-tracker-code-hosting-translation-distribution-building-cross-project-collaboration
thing](https://launchpad.net/) is actually quite handy.  
  
If you want to get started hacking with launchpadlib, and you have
Ubuntu, then install 'python-launchpadlib' now. I'm pretty sure you can
also get it from PyPI.  
  
You can check that it works by running:

    $ python>>> import launchpadlib>>> launchpadlib.__version__'1.5.1'

  
I'll be assuming you're running 1.5.1 or later.  
  
I've written a very simple launchpadlib application that you can get
with 'bzr branch lp:\~jml/+junk/bugstats'. Each revision shows a
meaningful launchpadlib script. You can get at the old revisions with
'bzr revert -r1' or 'bzr revert -r2' or '-r3'.  
  
Here's what the simplest launchpadlib script that I could think of looks
like:  

    import osimport sysfrom launchpadlib.launchpad import Launchpad, STAGING_SERVICE_ROOTAPP_NAME = 'jml-bug-stats'CACHE_DIR = os.path.expanduser('~/.launchpadlib/cache')SERVICE_ROOT = STAGING_SERVICE_ROOTlaunchpad = Launchpad.login_with(APP_NAME, SERVICE_ROOT, CACHE_DIR)print launchpad.bugs[1].title

(Adapted from r2 of the above branch).  
  
A few points.  
  

-   We use `STAGING_SERVICE_ROOT`, which means that we're pointing  
   at [Launchpad's staging service](https://staging.launchpad.net/),  
   just in case we screw up any data.
-   We give the application a name, when you run the application,
    launchpadlib  
   opens up a browser window letting *you* decide how far the
    application  
   can act on *your* behalf.
-   We provide a cache directory. Credentials, among other things, get
    stored  
   here.  
-   We then login and get an object that represents a Launchpad instance
-   Once we've got it, we look at the collection of bugs, get Bug \#1
    and then  
   print the title

Very simple. To learn how to write this application, I looked at the
main [Launchpad API help](https://help.launchpad.net/API) page, the  
[examples](https://help.launchpad.net/API/Examples) page and the
[reference documentation](https://staging.launchpad.net/+apidoc). You'll
notice that I had to translate the reference documentation from
REST-speak into Python-speak.  
  
Already you have enough to go exploring with the Launchpad API and think
of cool things to do. A bunch of people are already doing [cool
stuff](https://help.launchpad.net/Clients) and there are many [projects
that use launchpadlib](https://help.launchpad.net/API/Uses).  
  
Next up, I hope to show you some more complex things you can do with the
API.

