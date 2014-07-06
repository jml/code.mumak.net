Title: Trying Haskell again
Date: 2013-07-15 10:56
Author: Jonathan Lange (noreply@blogger.com)
Slug: tag:blogger.com,1999:blog-5733547231775030285

I've been wanting to muck-around with Haskell again for ages and ages
now. My recent trip to the UK gave me a chance to do that. Here are some
quick reflections:  
  

<ul>
<li>
Typeclasses are great

</li>
<li>
I forgot to install docs on my laptop before I hit the road, but I got a
fairly long way by looking at old code that I had written

</li>
<li>
I spent a lot of time making the type system happy for some fairly basic
numeric operations

</li>
<li>
I really love Haskell's pattern matching

</li>
<li>
I really, really love the magic combination of partial application and
function composition. It's such a nice feeling to make a useful
programming by just gluing parts together.

</li>
-   There's a significant readability boost with point-free style (f . g
    . h) vs nested call style (f(g(h(x))))

<li>
When I'm writing Haskell, I miss literal map (dict) syntax

</li>
<li>
Guy Steele did a talk on map/reduce as a primitive which I'm constantly
reminded of and need to re-watch and understand

</li>
<li>
The main thing that attracts me to Haskell & Clojure is immutable data
structures

</li>
<li>
Haskell is more attractive than Clojure for command-line scripts,
because JRE start-up time is prohibitively expensive

</li>
<li>
Haskell does indeed have a learning curve

</li>
-   I'm optimistic that this will go away as more concepts filter down
    to more mainstream languages

<li>
Understanding mathematical concepts (e.g. knowing what 'associative
operator' means) might sound ivory tower, but helps so much when making
things that can be combined, re-used, and understood.

</li>
-   If PHP developers knew that equality is an equivalence relation and
    that equivalence relations are transitive then perhaps === wouldn't
    be necessary.
-   XXX: Probably make this a separate post

<li>
ghci is much better than hugs

</li>
<li>
I miss the quick hacking loop of Python. The "Real World Haskell"
authors suggest that a good way to do this is use the ghci repl to
develop things and then move into your file. I need to work on this.

</li>
<li>
My exercise was to do thinkstats exercises in Haskell. This is quite
nice.

</li>
<li>
Data.Map is a binary tree. Why not a HAMT?

</li>
</ul>
<div>

XXX: Maybe rewrite for audience = Python developers.

</div>

<div>

XXX: Maybe include / link to code that I wrote

</div>


