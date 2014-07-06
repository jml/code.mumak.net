Title: Tests that print stuff
Date: 2010-11-26 16:01
Author: Jonathan Lange (noreply@blogger.com)
Tags: subunit data
Slug: tests-that-print-stuff

Tests that print stuff to stdout or stderr annoy me.  They make a
successful test run much less satisfying to watch, and they clutter logs
when you are trying to debug a failure.  
  
Launchpad has quite a few tests that print stuff.  I was going to fix
them up today, but I've got a Launchpad branch in progress and I've
promised myself that I'll have only one in progress at a time. Besides,
the build is broken.  
  
Anyway, I've written a quick hack that lets you analyze a
[subunit](http://launchpad.net/subunit) stream to [see which tests print
stuff](http://paste.ubuntu.com/536731/).  
  
To get a subunit stream including the output itself:  

    $ gzip -dc testtools-experiment-r11753.subunit.gz | grep -v time: |  python tests-with-output.py

  
To get a list of the tests:  

    $ gzip -dc testtools-experiment-r11753.subunit.gz |  python tests-with-output.py  | subunit-ls --no-passthrough

  
For those interested, Launchpad has roughly one hundred such tests.  
  
As with my last post, I'm left with the feeling that subunit is great
but needs a lot more polish.  I guess my next step is to figure out how
to upstream these.

