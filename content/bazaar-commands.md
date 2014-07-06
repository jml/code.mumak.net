Title: Bazaar commands
Date: 2009-02-04 21:45
Author: Jonathan Lange (noreply@blogger.com)
Slug: bazaar-commands

While in Argentina, I got around to doing something that I've wanted to
do for ages: refactor Bazaar's "serve" command. It's been bugging me for
a while, since we actually duplicate some of that code in Launchpad, and
we keep getting bitten by changes to `cmd_serve`. There's also another,
deeper reason why I wanted to do it.  
  
Bazaar isn't just a version control system, it's also a very good
version control <span>library</span>. It's very easy to figure out, use
and test. I'm almost tempted to say "beautiful". In any case, if you're
writing a Python library, you should probably copy bzrlib.  
  
Except for bzrlib/builtins.py, which is where all of the built-in
commands like "serve" live. For one reason or another, it's full of
massive `run()` methods. Many of these methods contain logic that plugin
authors end up copying and pasting — blech.<span></span> Hence,
refactoring `cmd_serve`.  
  
If you are keen to learn how a version control system works, you could
do a lot worse than dive into bzrlib/builtins.py, figure out what a
particular command is doing, then refactor that command so the code
speaks for itself. There are 64 commands in core Bazaar: get cracking!

