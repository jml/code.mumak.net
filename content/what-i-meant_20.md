Title: What I meant
Date: 2008-07-05 10:09
Author: Jonathan Lange (noreply@blogger.com)
Tags: Uncategorized
Slug: what-i-meant_20

[z3p](http://z3p.tumblr.com/) recently [blogged
about](http://z3p.tumblr.com/post/32324725) a comment I made in [a code
review](http://twistedmatrix.com/trac/ticket/2710). In the review, I
linked to:  
  
![The only measure of code quality is WTFs /
minute](http://74.54.212.169/2ERcULhJC81alpg64P4WN7Of_400.jpg)  
  
That's a negative and grumpy way of phrasing an idea that I've come to
value a lot: *good code expresses its intent clearly.*  
  
When looking at a patch, the reviewer needs to understand two things:
the intent of the code and the intent of each *change* to the code. To
be clear on the former, you need:  

-   intent-revealing names.
-   good abstractions / interfaces.
-   good, small tests.
-   simple implementations where possible.[1]
-   docstrings where appropriate
-   comments where appropriate.

  
That's not exhaustive, but it's in a rough order.  
  
To be clear on the intent of your change to code, you need:  

-   Small patches.
-   A good bug / spec with a good, short summary.
-   A review request letter, summarizing your implementation strategy,
    any compromises you made, gaps in testing, future work etc.

  
That's not exhaustive either. In \#2037, I didn't understand the
motivation for lots of the code, nor for some of the changes to the
code.  
  
I'm indebted to [Andrew Bennetts](http://andrew.puzzling.org) for
teaching me that the first duty of a reviewer is to ensure that the code
is clear and to [Tom Berger](http://intellectronica.net/) for reminding
me that compromises are worth noting.  
  
----  
  
[1] Actually, this reminds me of something I heard [a
preacher](http://en.wikipedia.org/wiki/Don_Carson) say, "before I give a
sermon, I go through it, find everything clever, and take it out" (I
paraphrase, not having a reference on hand).  
  
In as much as sermons and code should both be ego-free communications of
ideas, I think this is sound advice for hackers.

