Title: Releasing Twisted, and procedure in general
Date: 2010-07-04 13:45
Author: Jonathan Lange (noreply@blogger.com)
Slug: releasing-twisted-and-procedure-in

I'm in the middle of releasing [Twisted](http://twistedmatrix.com/)
10.1, following the [procedure
document](http://twistedmatrix.com/trac/wiki/ReleaseProcess) that I
wrote when I released [Twisted
10.0](http://labs.twistedmatrix.com/2010/03/twisted-1000-released.html).
Having everything written down has been a wonderful aide so far, but
doing the release twice has made me think about what it takes to breathe
life into old procedure.  
  
The very first step has already been taken, *figure out what the process
is and write it down.* There are still some bits that are unknown and
hazy, but I expect they'll be clear by the time we're done. Anyway,
writing things down is only the beginning, after that, there are two
things that I think we ought to do roughly concurrently.  
  
The first is *automate the existing procedure* for which here are
already [many tickets
filed](http://twistedmatrix.com/trac/query?status=assigned&status=new&status=reopened&group=status&milestone=regular-releases),
and the second is *simplify the process itself*. Are all of the steps in
the process really needed? Why do we have so many tarballs? Why upload
the tarballs to a server that is only periodically mirrored by the
actual official download location? Why generate a PDF?  
  
I don't want to start a discussion on the details here, but rather raise
the need for Twisted to begin considering this simplification, and for
myself to begin articulating some of my own thoughts about process in
general.  
  
The final, on-going step in revitalizing procedure is to *delegate the
task*, either to another human being or better yet a machine. I wonder
if it would be possible to have the Twisted release done by a monthly
cronjob?  
  
In summary, to revive an existing process:  
  

-   Figure out what the process is and write it down
-   Simplify the process itself, reducing the number of steps
-   Automate as many of the steps as possible, thus combining them
-   Delegate the execution of the process

<!-- -->


