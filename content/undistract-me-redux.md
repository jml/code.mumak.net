Title: Undistract me (redux)
Date: 2012-10-04 11:35
Author: Jonathan Lange (noreply@blogger.com)
Slug: undistract-me-redux

[In January](http://code.mumak.net/2012/01/undistract-me.html), I told
you all about a terminal hack to help me recover from the inevitable
distraction that comes when I run commands that take a while to run (for
me, mostly test suites).  
  
I've been using the hack since then, and it has given me a great deal of
pleasure. Others have watched it and said that they very much wanted
it.  
  
As such, you can now go to the
[undistract-me](http://mumak.net/undistract-me/) website to get
instruction on how to download and install it. Or, if you're using
Ubuntu:  

>     $ sudo add-apt-repository ppa:undistract-me-packagers/daily$ sudo apt-get update$ sudo apt-get install undistract-me

Once you've done that, and have started a new login shell, then you'll
get a notification whenever a command that takes more than 10 seconds to
run finally completes.  
  
Thanks to [Glyph Lefkowitz](http://glyph.twistedmatrix.com/) for [the
preexec hack](http://www.twistedmatrix.com/users/glyph/preexec.bash.txt)
that made this possible, and to [Chris Jones](http://www.tenshu.net/),
[Clint Byrum](http://fewbar.com/) and [Michael
Vogt](http://mvogt.wordpress.com/) for their help in figuring out what I
should do.

