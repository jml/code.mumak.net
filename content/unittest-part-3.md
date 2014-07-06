Title: unittest, part 3
Date: 2010-08-14 14:34
Author: Jonathan Lange (noreply@blogger.com)
Slug: unittest-part-3

So far, we've talked about `TestSuite`s, `TestCase`s and `TestResult`s.
We've seen how these objects interact with each other  and how they can
generally be thought about as having more than one interface.
`TestResult` has an interface for the `TestCase` and an interface used
for querying the results, `TestCase` has an interface for test runners
and an interface for test authors, and so forth.  
  
Now we need to give some time to the bits that glue everything together:
the test runner and the test loader.  
  
**`TestRunner`**  
  
You will not find a class in unittest.py called `TestRunner`. A test
runner is simply something that takes user input about a test run – what
tests to run, what manner to run them in, how to display the results –
and does it.  
  
Essentially, it does something like this:

      test = TestLoader().loadTests(user_specified_test_string)  result = makeTestResult(options_specified_by_user)  result.startTestRun()  try:    test.run(result)  finally:    result.stopTestRun()

  
And that's it.  
  
You see that the test runner is responsible for instantiating the test
loader and the test result. It's perhaps excusable for a test runner to
be tightly bound to particular implementations of test loader and test
result. Certainly, before `TestResult` grew `startTestRun` and
`stopTestRun` it was inevitable: since the test runner was responsible
for summarizing the results of a test run, overall responsibility for
displaying the results was split between the runner and the result.  
  
Nowadays, the tight coupling can be limited. If your test runner has an
option to display stack traces as it gets them, then that's pretty much
going to force you to use a particular result. However, you can still
write your code internally such that someone could pass in a different
result that still works, even though it doesn't do exactly what the user
asked for.  
  
**`TestLoader`**  
  
From the point of view of interfaces and compatibility, this is a pretty
boring class, and that's a good thing. The test loader's job is to find
tests based on some user input and construct a single `ITest` object for
them.  
  
When it does more than this, one runs the risk of having the behaviour
of a test suite depend too much on the runner itself. The ideal is to
have the test suite run in any runner: trial, nose, unittest2, py.test,
whatever.  
  
Some `TestLoader`s provide hooks so that users with complicated test
suites can customize the way their tests are loaded. Whenever the Trial
`TestLoader` sees a `test_suite()` function in a module, it lets that
function take charge of the loading.  
  
The standard library in 2.7 has a new hook, inspired by an innovation in
bzrlib, but slightly different.
`load_tests(loader, standard_tests, pattern)` is given the loader used
by the test runner, the tests that the loader would have loaded, and if
appropriate, a glob used for matching test module files. The advantage
of this hook is that it reduces the danger of customizations made to the
loader, since the test suite has access to the same loader. It also
makes custom loading easier by giving the standard tests as a starting
point. bzrlib uses this to run the same set of tests against many
implementations.  
  
I *think* that's all I have to say about these two, which means that's
pretty much all I have to say about unittest's API for test frameworks.
Still one more post to go though: interfaces for test authors.  
  
Let me know if I've missed anything, if anything here surprises you or
contradicts something I said in the past or if things are unclear. The
comments on the previous two posts have really helped!

