Title: pyflakes update
Date: 2011-11-21 14:29
Author: Jonathan Lange (noreply@blogger.com)
Slug: pyflakes-update

Thanks to [radix](http://radix.twistedmatrix.com/),
[exarkun](http://as.ynchrono.us/) & [dash](http://as.ynchrono.us/), my
branch to [pyflakes](http://pypi.python.org/pypi/pyflakes) to warn about
duplicate definitions of classes finally landed. I did the work a year
ago as an outrage-powered, opportunistic fix after I saw a co-worker
struggle with tests weirdly not failing (Turned out it was a huge test
module and there was another class at the bottom with the same name).
I'm very happy to see it landed.  
  
For those who haven't been paying attention, official pyflakes
development is now taking place on [Launchpad](https://launchpad.net/)
as part of the [divmod.org](http://launchpad.net/divmod.org) project.
The trunk of that project now has the best version of pyflakes known to
man.  
  
pyflakes is the best static Python checker. It's fast, and has very few
false positives.  
  
**Update:** A couple of people have asked me about
[lp:pyflakes](https://launchpad.net/pyflakes). It's dead. It died when
the divmorg.org trac instance died ages ago. Don't use it. To get
pyflakes or any other divmod project, use
[lp:divmod.org](https://launchpad.net/divmod.org).

