Title: Wheels within wheels
Date: 2010-04-27 17:34
Author: Jonathan Lange (noreply@blogger.com)
Slug: wheels-within-wheels

Software is best built incrementally. I hope everyone agrees with that.
There's quite a bit of disagreement as to what "incrementally", of
course, but it seems to have something to do with *iterations*.  
  
No one really agrees on what an iteration is either. There are a lot of
fancy metaphors and abstract phrases that get used to describe the
various bits of what people think an iteration is: customers tell
"stories" that engineers then "estimate"; programmers "sprint" like
children at an athletics carnival; they "release" software as if it were
an insufficiently randy panda; deliverables get delivered.  
  
When one washes all of the metaphors and best little practices away,
what's left is this: build a little bit of software; evaluate it.
Ideally, the software is evaluated by someone who stands to benefit
directly from using it.  
  
I'm not sure there's much more to recent software methodologies than
that. Perhaps we can explore it more in the comments.  
  
This combination of increments and iterations spirals toward the final
product, which is generally what you have left when the money runs out.
Alas, if only we could draw a picture of the process with a simple
spiral! When I think of it, I fall prey to a rare attack of envy toward
students of [hermeneutics](http://en.wikipedia.org/wiki/Hermeneutics).  
  
The process involves spirals within spirals, cycles made up of cycles.
Going  
inwards from the greatest wheel to the smallest, the Launchpad project
has:  

planning cycles
:   When we plan the major features and general direction of Launchpad.
    [Road map](https://dev.launchpad.net/RoadMap) sort of  
   stuff. Approximately six months.
feature cycles
:   The repeated process of beginning a feature, developing it,
    releasing it,  
   fixing it, then stopping. Varies in cycle time, but usually one to
    three  
   months.
release cycles
:   We release whatever is in [trunk](https://dev.launchpad.net/Trunk)
    each month
branch cycles
:   Branch from trunk, hack on it, push it up, get it reviewed, land it,
    wait  
   until it passes the test suite, check that the changes worked. Two
    or three  
   days.
experiment cycles
:   A developer is working on a thing and wants to actually see how it
    works  
   in the running code. They write many tests and a fair bit of code
    and then  
   fire up a development instance of Launchpad and see how it looks.
TDD cycles
:   Write a failing test. Run the tests (a subset of the whole suite).
    Make  
   the test pass. Run the tests. Refactor. Run the tests. Probably
    about  
   half-an-hour?

Different projects surely have different kinds of cycles. Most projects
probably have a subset of the ones above. In any case, thinking in terms
of nested cycles is a good way of analyzing ones development process.  
  
Each of these cycles has its own overhead and its own waste. One cycle
being particularly slow has a different effect to another cycle being
slow. For example, I contend that the slow branch cycle makes it less
likely that trivial bugs get fixed.  
  
Lean advocates would tell me not to think this way. They would have me
unroll these cycles and lay them out on a line beginning with someone
wanting something and ending with that want satisfied. They would have
me draw a "value stream map".  
  
Bollocks to them. At least on Launchpad, we should optimize the
innermost loops first.  
  
Have I missed some kinds of cycles? Can you think of a better name than
"experiment cycle"? Is there prior literature I should read? Are you
going to apply these ideas to your project?

