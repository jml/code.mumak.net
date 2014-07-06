Title: testtools 0.9.2 released
Date: 2009-12-15 23:19
Author: Jonathan Lange (noreply@blogger.com)
Slug: testtools-092-released

I've just released [testtools
0.9.2](http://pypi.python.org/pypi/testtools/0.9.2), which I firmly
believe is the best [testtools](https://launchpad.net/testtools) release
ever. Thanks very much to [Robert
Collins](http://rbtcollins.wordpress.com/) and [Benjamin
Peterson](http://pybites.blogspot.com/) for making it so.

<div>

For the last few releases, we've been working on being more than just a
simple aggregation of existing unit testing best practices and tried to
do our own experimental extensions.

</div>

<div>

These extensions aren't actually all that exciting by themselves. We
haven't added better logging support or new types of outcomes or test
replay or smart rendering of error results or anything like that. I'm
pretty sure testtools will never do those sorts of things.

</div>

<div>

Rather, the extensions we've added are designed to let *you* do that,
and then share *your* extensions with other people without getting them
into the standard library's base `unittest` classes.

</div>

<div>

If you are using testtools, you can change the way `TestCase.run()`
works without overriding run and without figuring out how to safely call
user code. You can handle exceptions raised from tests however you'd
like — again not needing to change `TestCase.run()`. You can add new,
rich types of assertions without having to modify some base class
somewhere. You can store information on a test object that can be used
by a sufficiently smart `TestResult`, which can be handy if you want to
see, say, access logs for all failed tests.

</div>

<div>

Of course, all this starts to get really powerful when testtools is in
the standard library, and all of the other major Python test frameworks
inherit from it: nose, py.test, zope.testing and Twisted Trial.

</div>

<div>

Even so, it's worth switching to testtools today, just for the assertion
logic alone. All it takes is changing the base class of your test cases
to `testtools.TestCase`. If your test framework supports running
standard Python unit tests, it'll support testtools.

</div>
