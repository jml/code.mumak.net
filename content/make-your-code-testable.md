Title: Make your code testable
Date: 2009-02-05 23:32
Author: Jonathan Lange (noreply@blogger.com)
Slug: make-your-code-testable

A lot of people struggle with writing unit tests. They sit down with the
noblest of intentions, ready to turn themselves around and be good
little engineers, but then somehow, suddenly, everything goes horribly
wrong.  
  
It turns out that it's really hard to write unit tests. When we first
discover this, we generally consider two options:  

1.  Give up
2.  Work hard to write the damn test

There is actually a third way: <span>make the code easier to
test</span>. Many of the barriers to testing are built from the design
of one's own code. Globals, hard-wired access to resources, poorly
parametrized behaviour and badly encapsulated data can make it a
nightmare to test things.  
  
The cool thing is, if you do this, your code base will actually be more
fun and more productive to work with. Your application will start to
look like a set of libraries that build high-level concepts, rather than
like a maze of twisty passages. This is actually why the [Bazaar API is
so amazingly good](http://code.mumak.net/2009/02/bazaar-commands.html)
-- they've written their code to make it easy to test.  
  
Thanks to [Cory Dodt](http://strongdynamic.blogspot.com/) for the idea
for this post.

