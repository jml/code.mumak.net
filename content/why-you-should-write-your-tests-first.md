Title: Why you should write your tests first
Date: 2010-09-07 10:44
Author: Jonathan Lange (noreply@blogger.com)
Slug: why-you-should-write-your-tests-first

We're all agreed that any Python code that's even a little serious needs
unit tests, right? However, sometimes we end up writing our tests after
we've written our code rather than doing test-driven development, what
[Curtis](http://curtis.hovey.name/) calls "code and cover". That's bad.
Here's why.  

1.  It's dull. Really dull.
2.  You find bugs, but it's somehow more frustrating. Perhaps because
    you thought your code was correct already.
3.  The code is probably not written for testability, which means you
    have to mix refactoring up with verifying behaviour. Messy &
    perilous.
4.  Alternatively, you write tests with a [lot of
    mocks](http://martinfowler.com/articles/mocksArentStubs.html). Not
    bad in itself, but risky.
5.  It's much harder to get full coverage.
6.  You write tests for things that you don't care about, just to
    exercise a particular code path. This makes the tests more
    [fragile](http://xunitpatterns.com/Fragile%20Test.html).
7.  You never really know when you are finished.

<div>

Are you a TDDer or a code-and-cover person? Why do you prefer it that
way?

</div>
