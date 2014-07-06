Title: Getting set up with Twisted development
Date: 2012-12-15 10:55
Author: Jonathan Lange (noreply@blogger.com)
Slug: getting-set-up-with-twisted-development

I haven't contributed much to Twisted recently, but today I'd really
like to get my [new Deferred
documentation](http://twistedmatrix.com/trac/ticket/6180) ready for
review.  
  
To my knowledge, the only sensible way to actually work on Twisted code
is using [Combinator](http://twistedmatrix.com/trac/wiki/Combinator).
With it, I can make branches, commit to those branches, merge in updates
from trunk and when my branch is approved, actually land it. All of this
is described more fully in Twisted's pioneering [Ultimate Quality
Development
System](http://twistedmatrix.com/trac/wiki/UltimateQualityDevelopmentSystem).  
  
Combinator works by convention, so its source *must* live within a
`Divmod/trunk` directory. Since I have the divmod.org code in a
colocated Bazaar branch in `~/src/divmod.org`, I created a new directory
under `~/src/` called Divmod and symlinked trunk to it, approximating
the instructions on the [Combinator
page](http://twistedmatrix.com/trac/wiki/Combinator).  
  
`  $ cd src`  
`  $ mkdir Divmod`  
`  $ cd Divmod`  
`  $ ln -s ~/src/divmod.org trunk`  
  
Trying to actually use Combinator only got me stack traces and warnings
though, so I poked around in the source code and now have a shell script
in \~/src/combinator.sh that does this:  
  
  
`  export COMBINATOR_PROJECTS=/home/jml/src`  
``   eval `python ~/src/Divmod/trunk/Combinator/environment.py` ``  

<div>

Sourcing that script works:

</div>

      $ .  ~/src/combinator.sh

  
<span>After that, I blew away my checkout of Twisted and made a newer,
Combinator-friendly one:</span>  
<span>  
</span>`  $ rm -rf ~/src/Twisted`  
`  $ chbranch Twisted trunk \`  
`      svn+ssh://svn.twistedmatrix.com/svn/Twisted/trunk`  

<div>

<span>All a little bit of a hassle, but worth it to get back into the
swing of contributing to Twisted.</span>

</div>
