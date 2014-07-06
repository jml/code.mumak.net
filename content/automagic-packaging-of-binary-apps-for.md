Title: Automagic packaging of binary apps for Ubuntu
Date: 2011-08-18 11:57
Author: Jonathan Lange (noreply@blogger.com)
Slug: automagic-packaging-of-binary-apps-for

For the last few weeks I've been working on a tool to automagically
package binary applications for Ubuntu. The idea is that anyone who
wants to distribute a binary app on Ubuntu should be able to do so
without having to learn how to package it.  
  
I've used [pkgme](http://pkgme.net/) to build a proof-of-concept: which
you can look at here:
[lp:\~jml/+junk/pkgme-binary](https://code.launchpad.net/~jml/+junk/pkgme-binary).  
  
Or, you can watch the demo:  
  

<div class="separator" style="clear: both; text-align: center;">

</div>

  
  
Right now, the tool assumes that the tarball:  

-   is an application
-   contains ELF objects that can be scanned for symbols, which
    determine the dependencies
-   has one main executable file
-   that its contents can be copied into `/opt/$PACKAGE/` and can be run
    from there by an ordinary user
-   comes with a JSON file specifying extra metadata

<div>

Our hope is that 90% of the binary applications we get will meet these
requirements.

</div>

<div>

The plan is to take this proof-of-concept and turn it into something
that will run server-side behind the [Ubuntu Developer
Portal](http://developer.ubuntu.com/). Next steps are to spec it out,
create a project, start filing bugs and fix the bugs I already know
about.

</div>

<div>

Watch this space for more updates.  
  
Thanks to James Westby and Adam Conrad for their help in doing the
proof-of-concept and to the dozen or so people who helped me get the
darn screencast out.

</div>
