Title: unittest API, part 2
Date: 2010-08-02 11:15
Author: Jonathan Lange (noreply@blogger.com)
Slug: unittest-api-part-2

In [part 1](http://code.mumak.net/2010/07/unittest-api-part-1.html) of
this humble attempt to document the interfaces and contracts that
unittest actually cares about, we talked about `TestSuite` and
`TestCase`, how they both implement a common interface that's used for
running tests, **`ITest`** and how they each implement their own
interfaces, **`ITestSuite`** and **`ITestCase`**.  
  
Now we're moving on to a much more complicated object, `TestResult`, to
see how we can pick apart the ways it interacts with the rest of the
system.  
  
**`TestResult`**  
  
A `TestResult` object is all about dealing with the results of tests, as
you might expect. However, it doesn't generally represent a *single*
test result. You could say it represents the results of a number of
tests, but I don't think that's terribly helpful.  
  
Better to think of a `TestResult` object as an event handler. A
`TestResult` object receives events from a test run and then does
something with them.  
  
Just as `TestCase` has a two-faced nature, presenting one interface to
the testing framework and another to test authors, so to `TestResult`
can be thought of has having many interfaces:  

1.  Its interface to a `TestCase`. This can be thought of as the *test
    event handling* interface
2.  A *result querying* interface, normally used by a test runner
3.  An interface for events that come from the test runner, the *runner
    event handling* interface.
4.  An *execution control* interface.

Note that the *result querying* interface and the *runner event
handling* interface together make up the interface between the
`TestResult` and test runner.  
  
Let's start with the *test event handling* interface. The methods below
are the interface between `TestCase.run()` and `TestResult`. (I guess
`TestCase.debug` too, but no one cares about it).  

`startTest(test)`
:   Called when `test` commences running. Although not enforced, it's
    impolite to provide any results for `test` before calling this.
`stopTest(test)`
:   Called when `test` is completely finished. Although not enforced,
    it's impolite to provide any more results for `test` after calling
    this, unless you call `startTest(test)` again first.
`addSuccess(test)`
:   Called when `test` has been shown to be successful. The default
    implementation does nothing.
`addError(test, err)`
:   Called when `test` raises an unexpected error. `err` is a tuple such
    as you might get from `sys.exc_info()`. Calling this method for the
    first time must change the result of `wasSuccessful()`.
`addFailure(test, err)`
:   Called when `test` has failed one of its assertions. `err` is a
    tuple such as you might get from `sys.exc_info()`.

The above interface is tightly coupled to the implementation of
`TestCase.run()`. In particular, if you wish to add more kinds of
results to your testing framework ("skip" results are a fairly common
addition), then you must change both `TestCase.run()` and the
`TestResult` interface.  
  
If you do something like that, I recommend making sure that your
modified `TestCase` can handle `TestResult` objects that do not provide
the extensions to the interface that you need. One common way of doing
this is to have the `TestCase` fall back to the primitive result types,
e.g. "skip" might become "success" for a `TestResult` that doesn't know
what skipping means.  
  
Importantly, the interface between `TestCase` and `TestResult` has been
fattened in Python 2.7.  

`addSkip(test, reason)`
:   Called when `test` is skipped. `reason` is a string explaining why
    the test was skipped.
`addExpectedFailure(test, err)`
:   Called when `test` failed in a way that was expected. `err` is a
    tuple such as the one returned by `sys.exc_info()`.
`addUnexpectedSuccess(test)`
:   Called when `test` was expected to fail, but didn't.

The following interface is a way of learning about test results after
they have happened, the *result querying* interface, and is part of the
contract between the test runner and the TestResult.  

`wasSuccessful()`
:   If there have been no errors and no failures, return `True`. Return
    `False` otherwise.
`testsRun`
:   An integer that is the number of tests that have been run.
`errors`
:   A list of tuples of `(test, error_message)` for all of the tests
    with unexpected errors, where `test` is an `ITestCase` and
    `error_message` is a string suitable for display to humans,
    generally containing a traceback.
`failures`
:   A list of tuples of `(test, error_message)` for all of the failing
    tests, where `test` is an `ITestCase` and `error_message` is a
    string suitable for display to humans, generally containing a
    traceback.

And of course, Python 2.7 fattens this interface again to have the
following:  

`skipped`
:   A list of tuples of `(test, reason)` for all of the skipped tests,
    where `test` is an `ITestCase` and `reason` is a string suitable for
    display to humans, generally containing a traceback.
`expectedFailures`
:   A list of tuples of `(test, error_message)` for all of the tests
    that were expected to fail and failed in the manner they were
    expected to, where `test` is an `ITestCase` and `error_message` is a
    string suitable for display to humans, generally containing a
    traceback.
`unexpectedSuccesses`
:   A list of all of the tests that unexpectedly succeeded. Members of
    the list are `ITestCase`s.

In Python 2.7, `TestResult` also extended its interface to the test
runner beyond simple result querying and into allowing the test runner
itself to send two very important events to the `TestResult`, behold the
*runner event handling* interface:  

`startTestRun()`
:   <div
    style="margin-bottom: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px;">

    Called before any tests have been run. It is impolite to provide any
    test results before calling this.

    </div>

`stopTestRun()`
:   <div
    style="margin-bottom: 0px; margin-left: 0px; margin-right: 0px; margin-top: 0px;">

    Called after all the tests have finished running. It is impolite to
    provide any test results after calling this. A `TestResult` object
    is generally not expected to handle any events at all after this
    method has been called.

    </div>

Some test runners rely on `TestResult`s to use those events to display
the results to the user. These runners frequently do not use the result
querying part of the interface.  
  
There is one more interface that `TestResult` implements: the *execution
control* interface:  

<dl>
<dt>
`stop()`

</dt>
<dd>
Signal that the execution of further tests should stop now. Sets
`shouldStop` to `True`.

</dd>
<dt>
`shouldStop`

</dt>
<dd>
If `True`, then test execution should stop. `TestSuite.run()` should
monitor this value and stop execution if ever it is `True`.

</dd>
<dt>
</dt>
</dl>
This interface is mostly used as a way of handling `KeyboardInterrupt`s
cleanly.  
  
**Summary**  
  
If you want your `TestResult` object to work with standard Python
`TestCase` objects, or any `TestCase` objects that try to stick close to
the standard, then you must provide the *test event handling* interface
described above. If you are writing your own test framework or test
runner, you care about this, because you want to run everyone's unit
tests.  
  
If you want your `TestResult` object to work with the standard Python
test runner before Python 2.7, then you must provide the *result
querying* interface. If you are using the standard Python test runner,
you care about this. For Trial or testtools, you must provide the
*runner event handling* interface. For anything else, I'm afraid you are
on your own.  
  
Always provide the *execution control* interface.  
  
**Comments**  
  
In this documentation, I've been trying to describe the various
interfaces without inserting too much of my own opinion about their
design. However, I think some commentary might actually help to make
things easier to understand.  
  
By providing a querying interface for `TestResult` to be used by a test
runner, the original designers of unittest practically insisted that
responsibility for displaying the results of a test run be split between
two different classes. The `TestResult` takes care of displaying
incremental feedback from the running tests and the test runner takes
care of displaying the summary. You can see evidence of this design in
Python 2.6's unittest.py, where there's a hidden `_TextTestResult`
subclass which has extra methods that are called only by a special
`TextTestRunner`.  
  
The addition of `startTestRun()` and `stopTestRun()` mean that now a
`TestResult` object can be fully in charge of displaying its results. As
such, providing a query interface and exposing details like the list of
test failures somewhat vestigial.  
  
I'm less happy with this post than the previous one. As such your
critique is even more welcome.  
  
Still to come: the interface for test authors and just what is a test
runner anyway?  
  
**Update:** Remove ambiguity in `expectedFailures` description (see
comments). Thanks Aaron.

