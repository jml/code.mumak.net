Title: How dependency guessing works
Date: 2011-08-18 12:18
Author: Jonathan Lange (noreply@blogger.com)
Slug: how-dependency-guessing-works

Although in my [last
post](http://code.mumak.net/2011/08/automagic-packaging-of-binary-apps-for.html)
I talked about our proof of concept tool, I didn't actually explain how
to use it. That's mostly because it's not quite ready to be used by
others. There's a good reason.  
  
The most interesting thing that
[pkgme-binary](https://code.launchpad.net/~jml/+junk/pkgme-binary) does
is to guess the dependencies of an application given only its tarball.
The way it does this is by finding all of the ELF objects (executables,
shared libraries etc.), reading the symbols from them, and figuring out
the packages based on those.  
  
Canny readers are already thinking, "Yes, that is what dpkg-shlibdeps
does" – which is true. As some background, Debian packages that export
symbols for linking also provide explicit metadata about those symbols
and what versions they appear in, in order to allow Debian packagers to
figure out dependencies easily using dpkg-shlibdeps. Fascinating reading
can be found in the [Debian policy
manual](http://www.debian.org/doc/debian-policy/ch-sharedlibs.html), a
[spec on improving
dpkg-shlibdeps](http://wiki.debian.org/Projects/ImprovedDpkgShlibdeps)
and [the guide on using the new symbol
files](http://wiki.debian.org/UsingSymbolsFiles).  
  
Unfortunately, dpkg-shlibdeps can only query packages that are installed
on your system. If you have a binary with symbols that are not provided
by any library on your system, you cannot use it to calculate
dependencies. Debian (or the Debian flavour of your choosing) might have
a perfectly good package to satisfy that dependency, but you won't be
able to find it.  
  
So, to do dependency guessing properly, you need to have a database
mapping symbols back to packages. Debian already has something like this
in its [mole database](http://qa.debian.org/cgi-bin/mole/seedsymbols/).
Ubuntu doesn't have anything like this that I know about.  
  
Assembling and maintaining such a database is pretty much a simple
matter of programming, but it's still work that I wanted to avoid for
the proof-of-concept. Instead, I used the mole database in Debian for
the calculations. That means we'll get wrong answers for Ubuntu, but it
demonstrates that the concept works.  
  
Since I have a copy of that mole database locally, and since it's about
1.5GB, I'm not distributing it with the branch. Which means that the
[automagic binary packaging
branch](https://code.launchpad.net/~jml/+junk/pkgme-binary) won't
actually work for you.  
  

