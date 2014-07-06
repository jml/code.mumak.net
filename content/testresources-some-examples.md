Title: testresources: some examples
Date: 2010-05-18 10:37
Author: Jonathan Lange (noreply@blogger.com)
Slug: testresources-some-examples

There's been a clamor for more documentation on how to use
[testresources](https://launchpad.net/testresources). While I'm not
qualified to show you the <span>best</span> way to use it, I can show
you the way that I would begin to use it.  
  
The linked files are a bunch of unit tests for database code that uses
[Storm](http://storm.canonical.com/). Where a real test suite might use
an in-memory database, this test suite uses on on-disk sqlite database
to better illustrate testresources. This database needs to be removed
and built again after each test to guarantee test isolation.  
  
You'll need testresources, Storm and testtools in your Python import
path to run these examples.  
  
The first file,
[complex-example.py](http://static.mumak.net/complex-example.py), shows
how I might do this without testresources. I create a DatabaseService
class that has a setUp and tearDown of its own, and a get\_store()
method that tests are likely to use. This might not be the best thing
for databases, but is very close to what I'd do for network services in
tests, where I would need to start the service, stop it and have methods
to get URLs, clients and other information about the service. If you run
the file, you'll see that the database is <span>created</span> at the
start of each test, and <span>destroyed</span> before the test finishes.
In total, it's created and destroyed three times.  
  
The second file,
[complex-example-2.py](http://static.mumak.net/complex-example-2.py),
shows how to switch to using testresources. To do this I,  

-   added a TestResource subclass called DatabaseResource that
    implements make() and clean() by delegating to a DatabaseService.
-   changed the test case to subclass ResourcedTestCase
-   added 'resources = [('database', DatabaseResource())] as a class
    variable of the test case.

Instead of using DatabaseService() in the test, I could have, and
perhaps should have, declared a module level instance of
DatabaseResource. In that case, the code would have looked like:  

    class _DatabaseResource(TestResource):...DatabaseResource = _DatabaseResource()class TestPerson(unittest.TestPerson):...resources = [('database', DatabaseResource)]...

  
Running the file shows that the behaviour is the same as the first
example: the database is <span>created</span> and <span>destroyed</span>
in each test.  
  
The third file,
[complex-example-3.py](http://static.mumak.net/complex-example-3.py),
shows how to take advantage of OptimisingTestSuite (sic). We load the
test suite as usual, <span>adsorb</span> (sic) them into an
OptimisingTestSuite and return that. We also have to explicity declare
when a test <span>dirties</span> the DatabaseResource. I chose to do
this by adding a dirtied() method to the DatabaseService. If I had used
a singleton (as above), then I would have just called dirtied on that.  
  
Anyway, if you run the third example, you'll see that the database is
<span>created</span> and <span>destroyed</span> outside the tests and
that its only done <span>twice</span>. The test suite has been optimized
by sharing resources between tests when possible.  
  
I hope this helps explain how to use testresources. Certainly writing
has been a useful exercise for me, it's highlighted that:  

-   a list of 2-tuples isn't quite right for declaring which resources a
    test uses.
-   the dirtied API is inconvenient
-   TestResource remains a confusing name for the class, as it conflates
    the resource acquisition and cleanup with the actual
    <span>resource</span>.
-   Some of the API docs are wrong (notably the ones for
    ResourcedTestCase).
-   The pattern of "resource object with setUp, tearDown, dirtied (and
    addCleanup)" should perhaps be turned into Python code.

I long for your thoughts.  
  
Examples:  
  
[complex-example.py](http://static.mumak.net/complex-example.py)  
[complex-example-2.py](http://static.mumak.net/complex-example-2.py)  
[complex-example-3.py](http://static.mumak.net/complex-example-3.py)  
  
**Update:** Correct links to example Python files.

