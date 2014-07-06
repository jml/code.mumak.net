Title: Doctests
Date: 2008-11-21 00:29
Author: Jonathan Lange (noreply@blogger.com)
Slug: doctests

[Andrew](http://andrew.puzzling.org/) has written about why [narrative
tests make lousy unit
tests](http://andrew.puzzling.org/diary/2008/October/23/narrative-tests)
and [problems with the doctest
format](http://andrew.puzzling.org/diary/2008/October/24/more-doctest-problems).
In summary:  

-   Unit tests work better if each one has a name that identifies it.
-   Specific, isolated tests give clearer failures, and are easier to
    debug.
-   Specific, narrow tests are better at communicating intended
    behaviour.
-   Comparing two objects in doctests is hard.
-   It's hard to get an overview of what's tested in a particular
    doctest file.
-   Doctest is a mini-language that's worse than Python. It's got
    corner-cases and outright bugs.
-   <span>Tests are code, and code works better in .py files than .txt
    files.</span> In particular:
    -   Python has better tool support. Syntax highlighting, code
        folding, pyflakes, 2to3 etc.  
   -   It's easier to build test infrastructure in Python.
    -   Test code benefits from refactoring as much as regular code, but
        doctests make it hard to do this.

Of course, in the end, it comes down to this:  

> It is just as possible to write incomprehensible tests using doctest
> as it is using `TestCase` classes with test methods.  

