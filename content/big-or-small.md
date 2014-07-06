Title: Big or small?
Date: 2010-11-24 16:12
Author: Jonathan Lange (noreply@blogger.com)
Slug: big-or-small

I've been thinking a bit about whether it is better to have one big code
base that has a lot of different components and features, or whether
there should be many small code bases that each do one thing well.  
  
I don't have any answers, but perhaps these half-formed thoughts will
help: positive, negative and interesting things about having many small
related projects. These thoughts are mostly inspired by working on a
bunch of different testing-related projects.  
  
**Positive**  
  

<ul>
<li>
"Do one thing and do it well"

</li>
<li>
Enforces a certain kind of interface discipline

</li>
<li>
Avoids/postpones scaling problems with big projects

</li>
-   test suite run times
-   documentation navigation
-   bug triage
-   forking mailing lists etc.

<li>
Newcomers only need to "buy in" to one idea at a time

</li>
<li>
Aligns with conceptual understanding of the problem

</li>
<li>
Better separation of commit privs etc

</li>
</ul>
<div>

**Negative**

</div>

<div>

<ul>
<li>
Release overhead
</li>
<li>
Duplication of infrastructure
</li>
-   buildbot / hudson / pqm
-   bug tracker
-   mailing list

<li>
Duplication of license / copyright games
</li>
<li>
Harder for newcomers to see the big picture
</li>
<li>
Problems caused by interactions between different versions
</li>
<li>
Depending on multiple libraries is a pain on many platforms
</li>
<li>
Lag with commit privs etc
</li>
</ul>
<div>

**Interesting**

</div>

</div>

<div>

-   Perhaps smaller & self-contained means easier to upstream
-   Some projects like adding only small dependencies, other projects
    like adding few dependencies

<div>

Do these make sense? What would you add?

</div>

</div>

<div>

Twisted is in a sense the opposite of the small/many paradigm, in that
it includes a great deal of extra features along with its core.

</div>
