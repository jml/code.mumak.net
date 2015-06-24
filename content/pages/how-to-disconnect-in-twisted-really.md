Title: How to disconnect in Twisted, really
Date: 2012-09-22 16:51
Author: Jonathan Lange (noreply@blogger.com)
Slug: how-to-disconnect-in-twisted-really
Alias: stuff/twisted-disconnect.html
Status: hidden

Twisted's unit testing framework Trial is quite strict on tests that
don't clean up after themselves. In particular, any test that doesn't
properly close all of its connections is fails with ugly errors.

If you are already glazing over with apathy towards unit tests, unglaze
now. Disconnecting is a little more involved than you might expect, and
there's every chance you aren't doing it correctly.

Thanks to [moshez](http://moshez.livejournal.com) and teratorn for
reviewing this document. Any errors are still my fault.

----

You are writing a test for some network code. You have already written
many unit tests for the protocol and the protocol factories, and you
assume that the lower level socket calls all work. You have deep
confidence in your code, but you need more.

You yearn to write an end-to-end test. To set up the server, have it
*really* listen, have the client *really* connect. You want data to zoom
back and forth over the wire like luxury sportscars on the Autobahn.

Fine.

You start with a server and a client.

You want the client to connect to the server. You want things to happen.
When things have happened, you want to assert stuff.

After the assertions, you want to disconnect the client and you want the
server to go away.

Good.

I'm not going to help you set things up, I'm not going to help you make
things happen. I *am* going to help you make all your connections just
go away.

Let me lay down the law:

1.  The server must stop listening.
2.  The client connection must disconnect.
3.  The server connection must disconnect.

You have to make each of these things happen. That's easy. Here's the
tricky part: **you have to *wait* for each of these things to happen.**

To make the server stop listening:

        port = reactor.listenTCP(portNumber, factory)    ...    port.stopListening()

You can effect the last two with one stroke, using either of the
following commands:

        protocol.transport.loseConnection()

OR

        connector = reactor.connectTCP(host, port, factory)    ...    connector.disconnect()

Now, just running these commands is *not* enough. Twisted is
asynchronous: you have to wait for it to call you.

The way to wait for something in a Trial test is to return a `Deferred`
from the test method.

`stopListening` is easy. It returns a `Deferred` if it is going to take
a while. The others are harder. There is only one way to know when the
connection has truly been lost: override `connectionLost` on a
`Protocol` instance. Pass a `Deferred` to your `Protocol` and have
`connectionLost` call `callback` on that `Deferred`. You will need to do
this for *both* the client *and* the server protocols. Once you have
your three `Deferred`s, return them in a `DeferredList`.

Simple.

**UPDATE:** [exarkun](http://jcalderone.livejournal.com) tells me that
there are two ways to know when the connection has truly been lost on
the client side. ClientFactory.clientConnectionLost is the other one.

### Summary

**In order to clean up a test that connects a client to a server, you
need to wait on three `Deferred`s: one for the listening port, one for
the server protocol and one for the client protocol.**

Below is an example demonstrating how to disconnect. As you can see, it
is quite verbose. Trial does not provide any shortcuts, even though it
should.

    from twisted.internet import defer, protocolfrom twisted.trial import unittestclass ServerProtocol(protocol.Protocol):    def connectionLost(self, *a):        self.factory.onConnectionLost.callback(self)class ClientProtocol(protocol.Protocol):    def connectionMade(self):        self.factory.onConnectionMade.callback(self)    def connectionLost(self, *a):        self.factory.onConnectionLost.callback(self)class TestDisconnect(unittest.TestCase):    def setUp(self):        self.serverDisconnected = defer.Deferred()        self.serverPort = self._listenServer(self.serverDisconnected)        connected = defer.Deferred()        self.clientDisconnected = defer.Deferred()        self.clientConnection = self._connectClient(connected,                                                    self.clientDisconnected)        return connected    def _listenServer(self, d):        from twisted.internet import reactor        f = protocol.Factory()        f.onConnectionLost = d        f.protocol = ServerProtocol        return reactor.listenTCP(0, f)    def _connectClient(self, d1, d2):        from twisted.internet import reactor        factory = protocol.ClientFactory()        factory.protocol = ClientProtocol        factory.onConnectionMade = d1        factory.onConnectionLost = d2        return reactor.connectTCP('localhost',                                  self.serverPort.getHost().port,                                  factory)    def tearDown(self):        d = defer.maybeDeferred(self.serverPort.stopListening)        self.clientConnection.disconnect()        return defer.gatherResults([d,                                    self.clientDisconnected,                                    self.serverDisconnected])    def test_disconnect(self):        pass
