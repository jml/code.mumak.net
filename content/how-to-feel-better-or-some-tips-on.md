Title: How to feel better (or, some tips on refactoring)
Date: 2011-11-04 18:29
Author: Jonathan Lange (noreply@blogger.com)
Slug: how-to-feel-better-or-some-tips-on

<span>A few months back I gave a lightning talk at the
[Launchpad](https://launchpad.net/) Thunderdome about how I do
refactoring.  It's very opinionated, and mostly applies to big, old code
bases, but worth writing up anyway.</span>  
<span>  
</span>  
<span>The core idea here is that very few things make me feel as good as
deleting code. I love cleaning up code and the clean code base that
results, and I'm sure that many others feel like me. As such, this is a
guide on how to feel better.</span>  
  
**1. Know your enemy**  
  
“Functionality is an asset, code is a liability”. Truer words were never
spoken. Every line of code is a potential source of bugs and a barrier
to understanding, and thus carries a maintenance cost.  
  
Maintain an awareness of things that need refactoring. Here's a quick
and incomplete list:  
  

-   <span>unused code – this can be deleted</span>
-   <span>boilerplate – this should become a function or class</span>
-   <span>wrong documentation – these should be updated</span>
-   <span>two ways of doing something – perhaps there should be
    one</span>
-   <span>bad names – change them to something that makes you think
    less</span>

**2. Keep a "yak stack"**  
  
[Yak
shaving](http://projects.csail.mit.edu/gsb/old-archive/gsb-archive/gsb2000-02-11.html)<span> is
"any seemingly pointless activity which is actually necessary to solve a
problem which solves a problem which, several levels of recursion later,
solves the real problem you're working on." ([Jargon
File](http://catb.org/jargon/html/Y/yak-shaving.html))</span>  
  
A few of us have extended the concept beyond the "actually necessary" to
include anything that's making the task at hand more difficult and less
fun but is not worth fixing *right* now. Hence the yak stack. Here's how
it works:  
  
Whenever you come across something in your code base that is difficult
to understand or that slows you down: make a note of it. When you've
finished the task at hand, fix the problem. If you encounter other
things that slow you down, write them down. Work through the list.  
  
**3. Every option is wrong**  
  
In a big, old code base, there are probably many, many areas that need
refactoring.  Don't worry about which is the "best" place to start –
there is no best place.  
  
**4. Start from green, stay green**  
  
Never, ever refactor while your tests are failing. Refactoring is about
changing the shape of code while preserving its behaviour. It's much
harder to be sure you're keeping the behaviour if you are comparing one
set of thirty tracebacks with another set of thirty tracebacks. Better
to compare a passing ("green") test run with another passing test run.  
  
Run tests frequently. More often then you think you should. Commit often
– think of it like quick save in a tough level of a video game. It frees
you up to experiment more and means you have less in your head at any
one time.  
  
**5. Do not nest**  
  
Don't begin a refactoring while you are in the middle of another
refactoring. If you find you must, use tools like '[bzr
shelve](http://doc.bazaar.canonical.com/beta/en/user-guide/shelving_changes.html)'
to store your current diff and then work from the clean head of your
branch.  
  
**6. Keep moving, leave a trail**  
  
Don't get bogged down in details, otherwise you'll never finish.
Literally. Someone will come along and distract you and before you know
it, three months will pass and your refactoring branch will be full of
conflicts. If you see something you are unsure of, mark it with a XXX or
a FIXME or a TODO or whatever works for you and then continue with what
you are doing.  
  
Tools like '[bzr todo](http://launchpad.net/difftodo)' can make it
really easy to check to see if you've added any XXX comments.  
  
**7. Translate tests with care**  
  
As said above, refactoring is about changing the shape of code while
preserving its behaviour. When you update tests, you risk changing your
definition of the system's behaviour – so be careful.  
  
**8. Confront uncertainty with destruction**  
  
If you see some code and you are not sure if it's needed, delete it.
Doesn't matter if it's a whole function or just an odd line. If you have
a test suite, and it was important, that will catch the failure. If you
have version control, and it was important, one of your collaborators
will notice and revert the change.  
  
If it was important and neither of these happened, then your whole
project has learned something new about itself, and that's probably
worth the hassle. (Oh, add tests & better docs after this happens.)  
  
**9. Good grep tools**  
  
Remember that symbols aren't only referenced from files that match
\*.py.  In big code bases there are often other sorts of files that
refer to symbols in the main code. In Launchpad, for example, we have
ZCML and doctest files that refer to symbols. When you want to know how
something is used or you want to rename something, make sure you use a
grep command that actually finds everything.  
  
Ideally, you should be able to run this command faster than you can
think about wanting to do it.  
  
Personally, I use 'bzr grep' a lot. Others recommend 'ack'.  
  
**10. There will be failures**  
  
Mentally prepare yourself for the fact that the first two or three full
test runs after your refactoring will fail.  This is especially
important for code bases that have multi-hour test run times.  
  
If you think this way, then you won't be as discouraged when it actually
happens.  
  
**11. Finish the job**  
  
Busy people refactoring a big code base are often tempted to apply a
refactoring to only a single part.  For example, some useful function is
extracted from repeated boilerplate in a few other functions. However,
many, many other instances in the code base continue to use the repeated
boilerplate.  
  
This is *almost* worse than just leaving the repeated boilerplate.
 There are now two idiomatic ways of doing the activity.  Further, other
developers who work on other parts of the code base probably won't find
out about it, and might end up repeating your refactoring. Ugh. How is
anyone new expected to get to grips with this code?  
  
Similarly, if a class, function or concept is renamed, rename it
everywhere, especially in the documentation.  
  
It's difficult and often tedious, but it really is worth taking
refactorings to completion. Apply them to the whole code base, or not at
all.  
  
Note that I'm referring to completeness, not perfection. If you block on
perfection, you never get anything useful done. If you aim for frequent
incremental improvements, you soar.  
  
**12. Read these books**  
  
I highly recommend
"[Refactoring](http://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672/ref=sr_1_1?s=books&ie=UTF8&qid=1320430812&sr=1-1)"
by Martin Fowler and "[TDD by
Example](http://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672/ref=sr_1_1?s=books&ie=UTF8&qid=1320430812&sr=1-1)"
by Kent Beck. I stole many of these ideas from them.  

<div>

**Over to you**

</div>

<div>

**  
**

</div>

<div>

This was very much just a dump of how I do refactoring when hacking on
Launchpad. I'm always keen to learn more, and would love to hear about
what works for you.

</div>


