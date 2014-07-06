Title: unittest API, part 1
Date: 2010-07-29 16:56
Author: Jonathan Lange (noreply@blogger.com)
Slug: unittest-api-part-1

It's a little known fact, but unittest actually has an API.  
  
This isn't the API that you deal with when you write tests, but rather
an API that unittest itself uses when running tests. You could think of
it as two interfaces: one for test frameworks and one for test authors.
Both APIs are real, but both are poorly documented and often
misunderstood or abused.  
  
**`TestCase`**  
  
An instance of `TestCase` represents a single test. What you think of as
a single test is up to you, but most of the time it's a unit test.  
  
A `TestCase` object *must* provide the following methods.  
  
This first list of methods can be thought of as a single interface,
which these blog posts will call **`ITest`** given the lack of any
better name.  

`countTestCases()`
:   A method that returns the number of test cases this represents. It
    should always return 1.
`run(result=None)`
:   Calling this method actually runs the test. `result` is a
    `TestResult` object. `run` must call `result.startTest(self)` when
    it commences running the test and `result.stopTest(self)` when it is
    finished. Between these calls it must call a method on `result` to
    signal the result of the test. `run` must never raise an exception,
    and its return value is ignored. If `result` is not provided, the
    `TestCase` is obliged to make one.
`__call__(result)`
:   Identical to `run(result)`, provided for backwards compatibility.
`debug()`
:   Calling this method runs the test without collecting its results. It
    may raise exceptions. This method is rarely called by test
    frameworks.

  
The following methods are specific to individual test case objects. We
call this interface **`ITestCase`**.  
  

`id()`
:   Should return a string that uniquely identifies the test. For Python
    tests, the fully-qualified Python name works well. The uniqueness of
    the id is not enforced.
`shortDescription()`
:   Should return a string that describes the test. Many test frameworks
    use this value to display test results.
`__str__`
:   Should return a string that describes the test. Frequently the same
    as either `shortDescription()` or `id()`. Many test frameworks use
    this value to display test results.

There is also a second interface, one that matters to code that
subclasses `TestCase`. We'll deal with that in a later post.  
  
**`TestSuite`**  
  
A `TestSuite` represents nothing more or less than a bunch of tests.  
  
A `TestSuite` must provide the `ITest` interface described above, with
the differences that you would expect from something that represents
many tests: `countTestCases` returns the number of tests in the suite;
`run` runs many tests and thus calls `result.startTest` and kin many
times over; `debug` is the same and can explode anywhere.  
  
One difference is that `TestSuite.run` must stop running tests as soon
as it detects that `result.shouldStop` is true.  
  
In addition, `TestSuite` implements the following interface, which I'm
giving the completely arbitrary non-existent name of `ITestSuite`.  

`addTest(test)`
:   Takes an `ITest` and adds it to the suite.
`addTests(tests)`
:   Takes an iterable of `ITest`s and adds them to the suite. Normally
    equivalent to `[suite.addTest(test) for test in tests]`.
`__iter__`
:   All test suites must be iterable. Iterating over a test suite yields
    `ITest`s. These may differ from the `ITest`s provided to `addTest`
    and `addTests`.

In later posts, I hope to document `TestResult`, the subclassing
interface of `TestCase` and tell you exactly what I think about test
loaders, test runners and the like.  
  
I'm blogging this partly because I don't know where else to write this
up, but mostly because I need your help to make sure that I'm being
clear and correct. Please comment with questions and corrections, and
let me know if you find this at all helpful.

