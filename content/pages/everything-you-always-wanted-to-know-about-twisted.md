Title: Everything You Always Wanted to Know about Twisted
Date: 2012-09-22 16:53
Author: Jonathan Lange (noreply@blogger.com)
Slug: everything-you-always-wanted-to-know-about-twisted
Status: hidden

*This paper was originally prepared as an introduction to Twisted for
the Launchpad development team, and was presented in London on October
30th, 2008. The version here has been edited for HTML, and has had
Launchpad-specific references and examples removed.*

By Jonathan M. Lange & Michael Hudson.

Abstract
========

Twisted has a bit of a reputation of being “magic” and some people seem
to be a bit scared of it. This talk will aim to explain the basic ideas
of Twisted in simple language and make it clear that it is not at all
magic. It will touch on the reactor, Deferreds, basic protocol structure
and dispell some common misconceptions.

Introduction
============

Twisted is, at its heart, an asynchronous I/O framework written in
Python. It comes bundled with application servers, defunct persistence
systems, protocol implementations, a testing framework and a quotes
file. Its size, scope and the unfamiliarity of its concepts make it
intimidating for newcomers. This paper aims to address the latter point,
by explaining the concepts of asynchronous programming as implemented by
Twisted.

This paper assumes that you know how to write Python code, that you know
roughly what an event loop is, and that you are comfortable with network
programming in general. When you are finished, you should know enough
about Twisted to start investigating how you can use it to solve your
specific problems.

A Result You Don't Have Yet
===========================

Imagine that you are writing a program where one API that you are using
returns placeholders for the actual results. You could think of each
placeholder as a promise that you will eventually get a result or you
could think of them as a result that you don't have yet.

Suppose one of these functions was order\_food(). This function places
an order for some food and then returns immediately. When we call it, it
returns a placeholder, like so:

``` {.python}
PLACEHOLDER = order_food()
```

We have the placeholder now and sometime later we'll get the actual
response (e.g. eggs benedict). How can we write a program that depends
on the outcome of ordering food? To do this, we would need to be able to
schedule actions for when we get the actual response. So, something
like:

``` {.python}
PLACEHOLDER = order_food()When PLACEHOLDER is ready, do ACTION
```

In Python, PLACEHOLDER is going to be a Python object, and the ACTION is
best represented as a callable, giving us::

``` {.python}
placeholder = order_food()placeholder.when_ready(do_action)
```

You can think of PLACEHOLDER as the source of a single event: "got a
value" and `do_action` a handler for that event. If order\_food just
returned its result immediately, the code would look like:

``` {.python}
value = order_food()do_action(value)
```

But our placeholder is not yet good enough. We need a way to use the
result of `do_action` to do other things. We need an equivalent of::

``` {.python}
value = order_food()x = do_action(value)do_something_else(x)
```

That is, our placeholder needs to do something like::

``` {.python}
placeholder = order_food()placeholder.when_ready(do_action)placeholder.when_ready(do_something_else)
```

Where the return value of `do_action` is passed to do\_something\_else.

To illustrate, let's extend our example to do something interesting with
the food we get back.

``` {.python}
    placeholder = order_food()    placeholder.when_ready(eat_meal)    placeholder.when_ready(compliment_chef)    def eat_meal(meal):        # I don't know how to do this in Python.        was_it_good = nom_nom_nom(meal)        return was_it_good    def compliment_chef(praiseworthy):        if praiseworthy:            print "Wuu chef!"        else:            print "I sneeze in your face!"
```

`eat_meal` and `compliment_chef` are both “callbacks”. `eat_meal` is run
as soon as we have a real result for `order_food()`. It's passed that
result (`meal` in the example), eats it and then returns a boolean
indicating whether or not it was any good. The key here is that *the
return value of a callback is passed as the first parameter to the next
callback.*

`compliment_chef` is run as soon as submit\_to\_pqm finishes. It is
passed the return value of `eat_meal`.

If `order_food` returned its result immediately, the code would look
like:

``` {.python}
meal = order_food()was_it_good = nom_nom_nom(meal):if was_it_good:    print "Wuu chef!"else:    print "I sneeze in your face!"
```

No Magic
--------

So far, there is no magic involved, just pure Python abstraction: no
threads, no I/O, no subprocesses, no signals, no concurrency.

In fact, here's an implementation:

``` {.python}
class Placeholder:    """A value you don't yet have."""    UNFIRED = object()    def __init__(self):        self._callbacks = []        self._result = self.UNFIRED    def already_fired(self):        return not self._result is self.UNFIRED    def when_ready(self, callable, *args,                   **kwargs):        self._callbacks.append((callable, args, kwargs))        if self.already_fired():            self._run_callbacks()        return self    def _run_callbacks(self):        while self._callbacks:            callable, args, kwargs = self._callbacks.pop()            self._result = callable(self._result, *args, **kwargs)    def fire(self, value):        if self.already_fired():            raise AlreadyFiredError(                self, value)        self._result = value        self._run_callbacks()
```

Nothing special, just loops, lists and first-class functions.

The reader will notice three things about this implementation:

1.  If a callback takes a long time to execute, the \_run\_callbacks
    loop will block.
2.  There is no error handling.
3.  If a callback returns a placeholder itself, the callbacks of
    \*that\* placeholder will never be run

The first is a deliberate design decision: there is no magic here. The
second is the subject of the next section. The third is left as an
exercise to the reader (hint: you can cheat by looking inside
twisted/internet/defer.py).

Errors
------

Actually, a placeholder is the source of two events: success and
failure, which correspond to 'return' and 'raise'. Any placeholder can
stand for a successful result or for a raised error.

This means that we need the equivalents of::

``` {.python}
# 1. Handle error then do the action anyway.try:    value = order_food()except:    handle_error()do_action(value)
```

``` {.python}
# 2. Handle the error but do the action only if the error doesn't occur.try:    value = order_food()except:    handle_error()else:    do_action(value)
```

``` {.python}
# 3. Handle the error for the entire operation.try:    value = order_food()    do_action(value)except:    handle_error()
```

``` {.python}
# 4. Do something regardless of success or failure.try:    value = order_food()finally:    do_cleanup()
```

We simply cannot use Python's built-in exception handling structures
because the result is not known yet. We need to extend our placeholder
to be able to replicate any error handling that we can do with
try/except/else/finally. Luckily, Twisted has already implemented such a
placeholder, calling it a Deferred. The 'when\_ready' operation
described above is called 'addCallback', and is analogous to 'do this on
next success'. The example from the previous section becomes:

``` {.python}
deferred = order_food()deferred.addCallback(eat_meal)deferred.addCallback(compliment_chef)
```

addCallback has a sibling, 'addErrback', which is 'do this on next
failure'.

The four clauses above become:

``` {.python}
# 1. Handle error then do the action anyway.deferred = order_food()deferred.addErrback(handle_error)deferred.addCallback(do_action)
```

``` {.python}
# 2. Handle the error but do the action only if# the error doesn't occur.deferred = order_food()deferred.addCallbacks(do_action, handle_error)
```

``` {.python}
# 3. Handle the error for the entire operation.deferred = order_food()deferred.addCallback(do_action)deferred.addErrback(handle_error)
```

``` {.python}
# 4. Do something regardless of success or failure.deferred = order_food()deferred.addBoth(do_cleanup)
```

Again, *none of this requires magic.* We could make the "Placeholder"
example above handle all of these cases without introducing any
concurrency, threading or non-blocking I/O.

We now have everything we need to write programs that use results that
we don't have yet. The only thing we lack is a *reason* for using such
results. For that we need a way of implementing asynchronous operations.

The Reactor
===========

The reactor is Twisted's event loop. You use the reactor to register
sources of events and handlers for these events, and then the reactor
calls those handlers.

In this sense, the simplest possible Twisted program is:

``` {.python}
from twisted.internet import reactorprint 'Hello'reactor.run()
```

This will print 'Hello' and then run until it is interrupted with a
signal (another event).

We can make the program a little more complex by registering our own
event:

``` {.python}
from twisted.internet import reactordef print_world():    print 'World!'print 'Hello ',reactor.callWhenRunning(print_world)reactor.run()
```

The reactor will print 'Hello', and then print 'World!' once it starts
running, and then it will loop forever as before. The next simplest form
of event is based on elapsed time:

``` {.python}
from twisted.internet import reactordef print_world():    print 'World!'    reactor.callLater(5, reactor.stop)print 'Hello ',reactor.callWhenRunning(print_world)reactor.run()
```

This will print "Hello, World!" as above, and then wait five seconds
before shutting down the reactor and exiting cleanly.

Note that the reactor calls your code and when your code is done,
control returns to the reactor.

Deferreds are used in order to turn event handlers into APIs that are
independent of those events:

``` {.python}
from twisted.internet import defer, reactordef run_later(seconds, function, *args, **kwargs):    d = defer.Deferred()    def fire():        value = function(*args, **kwargs)        d.callback(value)    reactor.callLater(seconds, fire)    return ddef print_stuff(message):    # Because 'print' is a *statement*.    print messaged = run_later(2, print_stuff, 'Hello')d.addCallback(lambda ignored: run_later(3, print_stuff, 'World'))run_later(3, print_stuff, 'Beautiful')reactor.run()
```

This will print "Hello" at two seconds, "Beautiful" at three seconds and
"World" three seconds after "Hello".

The deferreds here make sure that one thing happens after another. The
'World' callback runs only after the deferred returned by the 'Hello'
run\_later is fired.

The "concurrency" here, such as it is, only works because everything
runs very quickly. If any method called by the reactor blocks, then the
entire application blocks:

``` {.python}
import timefrom twisted.internet import defer, reactordef sleep_then_print(seconds, value):    time.sleep(seconds)    print valued = run_later(2, print_stuff, 'Hello')d.addCallback(lambda ignored: sleep_then_print(3, 'World'))run_later(3, print_stuff, 'Beautiful')reactor.run()
```

Although this *looks* like it might do the same thing as the previous
program, it will actually display:

    HelloWorldBeautiful

What happens is that after 'Hello' is printed, the 'sleep\_then\_print'
callback is fired, blocking processing for three seconds. The reactor
only gets a chance to execute the 'Beautiful' print statement after
sleep\_then\_print has exited.

This is about as much as can be said about the reactor without
introducing Twisted's abstractions for I/O.

Separate Concerns
=================

Twisted is fundamentally about doing asynchronous I/O — the fundamental
purpose of deferreds and the reactor is to make it easier to write
programs that communicate over the network asynchronously.

The first necessary part is an interface for handling very low-level
events and operations: this socket just got some data; the remote end
disconnected; write some data etc. In Twisted terminology, this is a
*transport*. There are transports for TCP, UDP, UNIX sockets, processes
and SSL. Each of these knows how to read and write bytes to the wire.

The second part is an object that can provide meaning to the low-level
byte operations: a *protocol* object. The protocol is a state machine
that responds to events that the transport sends it, events like:
`dataReceived`; `connectionMade` and `connectionLost`.

The third is an object that can be used to create new protocol objects
as new connections are required and to bind these protocol objects to
their transports (not strictly true -- other parts of Twisted do the
binding. Still, it's a helpful lie). Twisted calls these *protocol
factories*.

Now, let's combine all of these together to write a toy server and a
client to go with it.

``` {.python}
from twisted.internet import protocol, reactorfrom twisted.protocols.basic import (   LineReceiver)class ReverseLineProtocol(LineReceiver):    """Line-based protocol that echoes any lines it receives in reverse.    Disconnects the client when ten lines have been received.    """    def __init__(self):        self._lines_received = 0    def lineReceived(self, line):        self.sendLine(''.join(reversed(line)))        self._lines_received += 1        if self._lines_received >= 10:            self.transport.loseConnection()class ReverseLineFactory(    protocol.ServerFactory):    protocol = ReverseLineProtocolreactor.listenTCP(9999, ReverseLineFactory())reactor.run()
```

The protocol is a LineReceiver, which is a simple helper built on top of
the base protocol that buffers bytes until they become lines, and then
sends those lines to lineReceived.

The call to listenTCP binds that instance of the factory to listen on
port 9999. When a new connection is made, Twisted constructs an instance
of the protocol and binds it to the socket opened for that connection.

Here's the client:

``` {.python}
from twisted.internet import defer, reactor, protocol as protofrom twisted.protocols.basic import LineReceiverclass ReverseClientProtocol(LineReceiver):    def __init__(self, deferred, string):        self._deferred = deferred        self._string = string    def connectionMade(self):        self.sendLine(self._string)    def lineReceived(self, line):        if self._deferred is None:            return        d, self._deferred = self.deferred, None        d.callback(line)class RemoteReverser:    def __init__(self, host, port):        self._host = host        self._port = port    def reverse(self, some_string):        """Send 'some_string' to the host to be reversed."""        d = defer.Deferred()        client_creator = proto.ClientFactory(            reactor, ReverseClientProtocol, d, some_string)        client_creator.connectTCP(self._host, self._port)        return ddef print_stuff(message):    print messagereverser = RemoteReverser('localhost', 9999)d = reverser.reverse('Hello')d.addCallback(print_stuff)d.addBoth(reactor.stop)reactor.run()
```

The ReverseLineProtocol implements the details of talking to the server:
it sends a line on connection and then fires its deferred as soon as it
receives a line back.

The dance with setting self.\_deferred to None is actually quite
important. If lineReceived naively fired the deferred every time it was
called, then it would raise an AlreadyFiredError.

RemoteReverser is a user-defined class with no explicit place in
Twisted. It provides an API for reversing a string. 'reverse' returns a
deferred that will fire with the first line returned from the server.

Again, by calling 'reverse' and using the deferred, callers can avoid
knowing *anything* about how the protocol works or what events are
involved. As far as a caller is concerned, a call to 'reverse' simply
returns a placeholder for a value that you don't have yet.

Conclusion
==========

Twisted provides tools for building libraries and applications that are
built around asynchronous I/O. It tries hard not to make decisions for
you so that you can write whatever application you need.

This paper hasn't described the way Deferred lets you return Deferreds
from callbacks and errbacks, nor has it described Twisted's `Failure`
object, which abstracts Python exceptions and provides many useful
helper methods for writing asynchronous programs. If you'd like to read
such a thing, [email me](mailto:jml+twistedpaper@mumak.net), and I'll
consider writing a follow-up paper.

