Title: I don't want to talk about documentation
Date: 2010-04-29 16:02
Author: Jonathan Lange (noreply@blogger.com)
Slug: i-dont-want-to-talk-about-documentation

Most of the time, I don't like talking about documentation. I
particularly don't like talking about documenting code. There's not much
to say.

<div>

  
<div>

I do like talking about testing though, since I enjoy writing code TDD,
since tests for[big, big, big programs](https://launchpad.net/launchpad)
are really hard and because most everyone else is doing it wrong.

</div>

<div>

Thing is, every time I talk about testing in the Python world, I have to
talk about documentation because [someone](http://barry.warsaw.us/)
always brings up [doctest](http://docs.python.org/library/doctest.html)
and thinks it's a good way of testing code. It's not. Andrew has
explained clearly the problems with the
[principle](http://bemusement.org/diary/2008/October/23/narrative-tests)
and with the
[implementation](http://bemusement.org/diary/2008/October/24/more-doctest-problems).
He concludes that the only thing that doctest is any good for is writing
self-testing documentation about Python code, and I agree.

</div>

</div>

<div>

However, I humbly suggest that for many projects, this is a solution in
search of a problem. Which means I am going to have to talk about
documenting code. Before that, a short plea.

</div>

<div>

Please stop talking about documentation and testing at the same time!
They are both actually quite tricky, and you can never, ever, ever
effectively address both of them with the same initiative. They are
different! Just stop it!

</div>

<div>

OK, let's talk about documenting code.

</div>

<div>

**Why bother?**

</div>

<div>

Before you even begin to talk about the best way to document your code,
you must seriously consider why you are even bothering.

</div>

<div>

Time spent documenting code is time not spent fixing bugs. Instead of
writing docs you could be talking to users, making your software
internationalizable, improving its website, improving the *user*
documentation, making the test suite run faster or any number of things
that directly help your end users or your existing developers.

</div>

<div>

You might want to document your code as part of an initiative to get
more contributors, or to make your existing contributors' lives happier.
If so, great, but make sure that documenting code will actually achieve
these goals.

</div>

<div>

If not, take pride in your lack of code documentation! It is the direct
fruit of you doing better things with your life. Stand up, walk out the
door and skip down the street, clutch the first suit-wearing stranger
you see by his lapels and shout "My code is under-documented, yippee
ki-yay!"

</div>

<div>

More seriously, know why you are documenting your code, don't just do it
out of guilt, and don't feel guilty if your code is under-documented
while your users are many and happy.

</div>

<div>

**Guiding principles**

</div>

<div>

*Audience and benefit*

</div>

<div>

Do not even bother to write a document unless you have an audience in
mind and a clear benefit in mind for what they'll get out of reading
this document. And no, "help them understand the branch puller XML-RPC
API" is not a clear benefit.

</div>

<div>

As an example, I'm writing this blog post primarily for Python
programmers at work and in the open source projects I care about. My aim
is to convince them to be silent about doctest when we're talking about
testing and to see the whole picture when talking about documentation so
that they'll have good unit tests and won't misdirect energy toward
inappropriate documentation. I have a secondary aim of learning where
I'm wrong by reading the comments.

</div>

<div>

*Clear code*

</div>

<div>

If someone is reading documentation that's about code, then they can
probably read code. You can probably save everyone a lot of trouble by
picking better names, adding a couple of docstrings, fixing the bits
you're embarrassed by and deleting the crap that you don't need.

</div>

<div>

To put it another way, when people say "this needs documentation" they
often mean "I don't understand this" (similarly, "we have a
communication problem" often means "you are not doing what I want"). The
best way to help them is not necessarily to write documentation.

</div>

<div>

*Value is in the output*

</div>

<div>

Documentation that's not being read is worthless and probably incorrect,
much like code that is not being executed. Documentation that cannot be
found cannot be read. How is your audience going to find your
documentation? Is it going to be in a format they like to read? Don't
bother writing anything until you've figured this out.

</div>

<div>

**Different approaches**

</div>

<div>

*No documentation, just code*

</div>

<div>

Some people believe that no human language text should ever sully their
code base. There are plenty of good sentiments behind this idea: source
code is a powerful tool for describing how to think about a problem;
textual documentation about code frequently goes out of date and it's
often used as a crutch for bad code.

</div>

<div>

Personally, I think it's a bad idea to have no documentation. Even the
best coders read good prose faster than good code, and text has a
wonderful power of summary that code lacks. Sometimes it's impossible to
communicate the intent of the code in the code itself (for example, you
might be working around a POSIX insanity). Nothing wrong with using a
crutch when your leg is broken.

</div>

<div>

*API reference documentation*

</div>

<div>

Instead of having no documentation, you can use Python's docstring
feature to add a mini-document describing a class or function. This
docstring can tell you how to use it, what to expect from it, and most
importantly, why you should care. Because Python functions don't have
explicit type declarations, these docstrings can be *very* useful (is
that `branch` parameter a Bazaar branch, a Launchpad `IBranch` object or
the URL for a branch?). Also, because the docstring is so close to the
code, they are much less likely to be out of date or incorrect.

</div>

<div>

*Specifications*

</div>

<div>

[Some people](http://rspec.info/) like having specifications as part of
the documentation for their code. I haven't really seen this in
practice, so I can't comment much. I can say that I find good comments
on unit tests extremely helpful, and now almost always write such a
comment before I write the test.

</div>

<div>

*Guides, tutorials and howtos*

</div>

<div>

Rather than consulting a reference, you sometimes want to be guided
through a task or to be introduced to some new area of the problem
domain. In these cases, it's pretty hard to beat a solid chunk of prose
with some code examples. It's here that doctest shines, since it's quick
to write, can be rendered nicely and can be executed to guarantee the
code is not hopelessly wrong.

</div>

<div>

**Summary**

</div>

<div>

Code documentation is not intrinsically valuable. It has no value unless
you give careful thought to why you want to do it and how it is going to
connect you to your audience. Once you've done that, prose documentation
can be very helpful, but you can also get a lot of the same benefits by
cleaning up your code base.

</div>

<div>

Doctest is neither necessary nor sufficient for good code documentation.
Do not use it simply because it is there. Use it when it fits.

</div>

<div>

Now, please can we go back to talking about testing?

</div>
