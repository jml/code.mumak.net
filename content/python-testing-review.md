Title: Python Testing: A review
Date: 2010-04-24 12:23
Author: Jonathan Lange (noreply@blogger.com)
Slug: python-testing-review

[![Cover of Python Testing book](http://4.bp.blogspot.com/_i72o3jegILg/S9LbHwDQ5_I/AAAAAAAAABs/oYwQaHlELgs/s200/Python+Testing.jpg)](http://4.bp.blogspot.com/_i72o3jegILg/S9LbHwDQ5_I/AAAAAAAAABs/oYwQaHlELgs/s1600/Python+Testing.jpg)Quite
a few weeks ago, perhaps even months, I was asked by [Packt
Publishing](http://www.packtpub.com/) to review a new book: "[Python
Testing: Beginner's
Guide](http://www.packtpub.com/python-testing-beginners-guide/book?utm_source=code.mumak.net&utm_medium=bookrev&utm_content=blog&utm_campaign=mdb_002509)"
by Daniel Arbuckle. They were very nice and even sent me a physical copy
of the book, and have been moderately tolerant of the long delay between
me receiving the book and writing this blog post.

<div>

Python Testing promises "an easy and convenient approach to testing your
Python projects". The book takes a tool-based approach to introducing
the reader to testing in Python. It starts with
[doctests](http://bemusement.org/diary/2008/October/24/more-doctest-problems),
goes on to [mocker](https://edge.launchpad.net/mocker), then
[unittest](http://docs.python.org/library/unittest.html), then
[nose](http://somethingaboutorange.com/mrl/projects/nose/0.11.3/). Then
I stopped reading.

</div>

<div>

It's not a bad book by any stretch, I just don't know who it's for. Bear
in mind that I'm not a beginner to Python testing so I'm probably not
the best judge.

</div>

<div>

Taking a tool-based approach seems like an odd decision to me,
especially for a printed book. The tools change all of the time, and
there is a reasonable amount of documentation for each of the tools
mentioned. A motivated beginner could probably make do with a blog post
listing each of the tools.

</div>

<div>

Many of the examples in the book are based on quite complex real-world
problems. In some ways, this is great, since it could help to convince
testing sceptics that testing is relevant to their project and it could
help along those who have trouble applying theory. On the other hand, I
think anyone who is up to following an AVL tree implementation is
capable of googling for "[python testing
tools](http://www.google.co.uk/search?hl=en&source=hp&q=python+testing+tools&meta=&aq=f&aqi=&aql=&oq=&gs_rfai=)".

</div>

<div>

Reading through, I found myself wishing for advice on the principles of
testing. How should I organize my tests on a Python project? How much
code should I cover in each test? What are the risks in using mock
objects? I sense that the author has never engaged with Gerald Meszaros'
excellent work on [xUnit Test Patterns](http://xunitpatterns.com/),
which is a must for everyone who isn't [Robert
Collins](http://rbtcollins.wordpress.com/).

</div>

<div>

I don't like writing such a negative review. It's hard work writing a
technical book – I tried writing one for Bazaar and gave up. Daniel
Arbuckle deserves credit for tackling such an important topic, for
working so hard to avoid being dry and for his obvious concern for
actually helping developers with their testing situation.

</div>

<div>

That said, if you are new to automated testing altogether, then you
would be much better off reading Kent Beck's [Test Driven Development by
Example](http://www.amazon.com/dp/0321146530/?tag=hashemian-20). If you
know testing well, but don't know Python so well, then I guess you might
get something out of Python Testing.

</div>
