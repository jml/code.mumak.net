Title: unittest API, part 4
Date: 2010-09-06 09:47
Author: Jonathan Lange (noreply@blogger.com)
Slug: unittest-api-part-4

As I said at the very beginning, unittest has an API with lots of
interfaces. You can read about the interfaces for test frameworks in
[part 1](http://code.mumak.net/2010/07/unittest-api-part-1.html), [part
2](http://code.mumak.net/2010/07/unittest-api-part-2.html) and [part
3](http://code.mumak.net/2010/08/unittest-part-3.html) of this series.
This post is about the interface for test authors.  
  
If the other posts are fresh in your mind, it's important to remember
that this post is focused on the standard implementation of `TestCase`.
After all, it's that implementation which creates the interface for test
authors. There are other implementations (e.g. `FunctionTestCase` and
`DocTestCase`) which provide completely different interfaces for test
authors, and one could write one's own implementation that provided
something else entirely.  

<div>

**Subclassing `TestCase`**

</div>

<div>

Almost all of the time that you want to write tests, you subclass
unittest.TestCase. It's not the only way to write unit tests with
unittest, but it's rather handy, particularly since the default test
loader looks for subclasses of `TestCase`.  
  
This is going to be much easier for all of us if I work from an example.

</div>

  

    class SomeTests(TestCase):  def setUp(self):    print "setUp"  def tearDown(self):    print "tearDown"  def test_a(self):    print "a"  def test_b(self):    print "b"

  

<div>

The test loader will make something that looks like
`unittest.TestSuite([SomeTests("test_a"), SomeTests("test_b")])`. That
is, it constructs an instance of `SomeTests` for each method beginning
with "test".  
  
The tests will only be run when `TestCase.run(result)` is called. The
tests do not get access to the result object, instead the run() method
mediates between the tests and the result.  
  
The default `TestCase.run(result)` method will run `setUp()`, then the
test method given in the constructor (e.g. `test_a`), then
`tearDown()`.  
  
If `setUp()` raises any exception, `tearDown()` will not be run. The
result object will have `addError` called on it with the test and the
error.  
  
If the test method raises an exception, one of two things can happen. If
the exception is an instance of `self.failureException`, then
`result.addFailure(test, exc_info)` is called, where test is the
`TestCase` instance and `exc_info` is the `sys.exc_info()` tuple.
Otherwise, `result.addError(test, exc_info)` is called. In either case,
`tearDown()` is then run.  
  
If `tearDown()` raises an exception, `result.addError(test, exc_info)`
is called.  
  
There are lots of built-in assertion methods on `unittest.TestCase`.
These all raise `self.failureException` if their assertion fails. These
are part of the interface for test authors, but they are already very
well documented. Just note that if you write your own, remember to raise
`self.failureException`, or better yet call `self.fail()`, rather than
raising `AssertionError` or something crazy like that.  
  
That's pretty much it.  
  
Of course, you could write your own object that implemented **`ITest`**
and **`ITestCase`**, and use your own test loader, and then you don't
have to care about anything in this post. But don't do that. Better to
subclass `unittest.TestCase`.  
  
As always, feedback welcome.

</div>
