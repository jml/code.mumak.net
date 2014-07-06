Title: What's wrong with ORMs
Date: 2012-11-20 15:07
Author: Jonathan Lange (noreply@blogger.com)
Slug: whats-wrong-with-orms

I was recently reading about [F1, Google's fault-tolerant distributed
RDBMS](http://research.google.com/pubs/pub38125.html) and came across
this neat little summary of what's wrong with ORMs.  
  

1.  Obscured database operations
2.  Serial reads
3.  Implicit traversal

<div>

*Obscured database operations* essentially means that when scanning
code, you cannot easily tell which code is going to kick off a network
round-trip to the database. If you care about writing code that performs
well, it's pretty important to know.

</div>

<div>

*Serial reads* are what many in my circles know as "[potato
programming](http://divmod.readthedocs.org/en/latest/philosophy/potato.html)".
When you have a loop, and something inside that loop is doing a query,
that's potato programming. Again, disastrous for performance.

</div>

<div>

*Implicit traversal* is doing unwanted joins and loading unnecessary
data. ORMs tend to load up an object with all of its instance variables,
which often means traversing the graph of references.

</div>

<div>

Anyway, this is a much handier answer to have than 'google for "[Vietnam
of Computer
Science](http://blogs.tedneward.com/2006/06/26/The+Vietnam+Of+Computer+Science.aspx)"',
which is fascinating but rather lengthy. (See also [Jeff Atwood's
summary](http://www.codinghorror.com/blog/2006/06/object-relational-mapping-is-the-vietnam-of-computer-science.html)).

</div>

<div>

For bonus points, these three things are also what's wrong
with [Launchpad's API](https://help.launchpad.net/API).

</div>
