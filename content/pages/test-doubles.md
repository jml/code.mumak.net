Title: Test Doubles
Date: 2012-09-22 16:48
Author: Jonathan Lange (noreply@blogger.com)
Slug: test-doubles

Test Doubles
============

Dummy
-----

Dummy objects are passed around but never actually used. Usually they
are just used to fill parameter lists. In Python, `None` is the ultimate
Dummy.

Fake
----

Fake objects actually have working implementations, but usually take
some shortcut which makes them not suitable for production (an in memory
database is a good example).

Stub
----

Stubs provide canned answers to calls made during the test, usually not
responding at all to anything outside what's programmed in for the test.
Stubs may also record information about calls, such as an email gateway
stub that remembers the messages it 'sent', or maybe only how many
messages it 'sent'.

Mock
----

Mocks are objects that are pre-programmed with expectations which form a
specification of the calls they are expected to receive.

*Lifted from [Mocks aren't
Stubs](http://martinfowler.com/articles/mocksArentStubs.html) and
derived from the excellent [xUnit patterns
book](http://xunitpatterns.com/).*

