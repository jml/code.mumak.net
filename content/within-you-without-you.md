Title: Within You Without You
Date: 2008-07-05 11:21
Author: Jonathan Lange (noreply@blogger.com)
Tags: Testing, Hacking, Twisted
Slug: within-you-without-you

Testing is hard, writing testing frameworks is easy. In an effort to
make testing easier, big projects like Twisted, Bazaar and Zope write
their own testing frameworks. That way they control both the test runner
and the tests that are run. It's actually quite convenient.

However, it's led to a significant problem:

> There are many similar implementations of xUnit in Python, each with
> subtle incompatibilities.


Running Twisted tests in the Zope test runner? Watch out for the threads
that the reactor maintains between tests. Running Bazaar tests with
Trial? On my machine, I get told that elementtree doesn't have an
'ElementTree' attribute. Hmm.

When talking about this problem, I often refer loosely to "PyUnit
compatibilty". The idea is that:

1.  Every Python test runner should support running vanilla Python
    standard library `unittest.TestCase` tests.
2.  Every Python unit test should be able to be run using the mechanisms
    in `unittest.py` in the Python standard library.


In other words, this code should Just Work:

```
import unittest
from yourframework import testing

class PythonTestCase(unittest.TestCase):
    def test_something(self):
        pass

class FrameworkTestCase(testing.TestCase):
    def test_something(self):
        pass

if __name__ == '__main__':
    python_test_result = unittest.TestResult()
    framework_test_result = testing.TestResult()
    FrameworkTestCase('test_something').run(python_test_result)
    FrameworkTestCase('test_something').run(framework_test_result)
    PythonTestCase('test_something').run(python_test_result)
    PythonTestCase('test_something').run(framework_test_result)
    # At this point, python_test_result and framework_test_result
    # should hold equivalent data.
```

If your framework is PyUnit compatible then the above fragment should
give the same results if run directly or if run in your runner. Things
get a little bit hazier when it comes to test discovery.

So, if your unit test requires that it be run inside a special suite
(e.g. `TrialSuite`) in order to work correctly, it is not PyUnit
compatible. If your test runner does some critical set up that enables
features that your tests need, then it is not PyUnit compatible.

This leads to a kind of thinking where certain features belong on the
base test case and others belong in the test runner. Putting features in
the wrong place might not lead to a strict incompatibility, but it can
lead to significant inconvenience. (And what are automated tests if not
a convenience?).

Two examples from Twisted:

**Temporary Working Directory**

Trial creates a `_trial_temp` working directory and changes into that
directory to run tests. In Trial, this feature is provided by the test
runner. It should be provided by the base `TestCase` class.

-   It's not clear that every test needs this feature.
-   Twisted tests now assume that they can create files with impunity.
    When Twisted tests are run in a different test runner, they leave
    garbage files everywhere.


**Timeouts**

By default, any Trial test that runs for more than two minutes will fail
with a timeout error. The timeout period can be configured on a
per-test, per-test-class, per-module or per-package basis. Trial
implements this feature on `TestCase`, it should be implemented on the
runner.

-   Even in the Twisted test runner, this makes debugging more painful.
    You must do all of your debugging in under two minutes.
-   Intuitively, you might think that the *runner* should control how
    tests are *run*.
-   Tests that don't descend from Trial's `TestCase` can still hang.
-   Two minutes might be good enough for me on a Monday, but I might be
    busier on Friday. I should be able to change the timeout without
    changing code.
