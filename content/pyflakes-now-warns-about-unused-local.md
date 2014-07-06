Title: pyflakes now warns about unused local variables
Date: 2009-06-03 22:54
Author: Jonathan Lange (noreply@blogger.com)
Slug: pyflakes-now-warns-about-unused-local

I finally got around to finishing my fix for
[Divmod](http://divmod.org/trac) bug
[\#2718](http://divmod.org/trac/ticket/2718) -- Warn about unused
variables in methods in
[pyflakes](http://www.divmod.org/trac/wiki/DivmodPyflakes). Last night,
the magnificent [Jean-Paul
Calderone](http://jcalderone.livejournal.com/) reviewed and landed my
patch. This means that if you are using pyflakes trunk (either from
Subversion [trunk](http://divmod.org/svn/Divmod/trunk/) or from the
Launchpad [Bazaar
import](https://code.edge.launchpad.net/%7Evcs-imports/pyflakes/main)),
pyflakes will spot code like:  

    def foo(bar):baz = bar + 2return 12

and generate a warning like:  

    example.py:2: local variable 'baz' is assigned to but never used

I use pyflakes hooked up to
[flymake](http://www.emacswiki.org/emacs/FlyMake), so it's always
running all the time on every Python file I'm working on. Relying on it
has become as second-nature as relying on syntax highlighting. There's a
whole class of mistakes I don't make any more, simply because it's on.  
  
However, the <span>main</span> way it helps me is when I'm refactoring
code. When extracting a function or changing a variable name, pyflakes
acts like a sort of todo list for me. Now that it shows unused local
variables, it's getting dangerously close to perfect.  
  
To get pyflakes quickly, bzr branch
[lp:pyflakes](https://code.edge.launchpad.net/%7Evcs-imports/pyflakes/main).  
  
(Edit: Grammar fix)

