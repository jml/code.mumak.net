===================================================
Announcing graphql-api: Haskell library for GraphQL
===================================================

:date: 2017-01-30
:tags: haskell, graphql
:slug: graphql-api

Late last year, my friend `Tom <https://github.com/teh>`_ tried to convince me
that writing REST APIs was boring and repetitive and that I should give this
thing called `GraphQL <http://graphql.org/>`_ a try.

I was initially sceptical. `servant
<http://haskell-servant.readthedocs.io/en/stable/>`_, the REST library that
I'm most familiar with, is lovely. Its clever use of Haskell's type system
means that all the boring boilerplate I'd have to write in other languages
just goes away.

However, after watching `Lee Byron's Strange Loop talk on GraphQL
<https://www.youtube.com/watch?v=Oh5oC98ztvI>`_ I began to see his point.
Being able to get many resources with the same request is very useful, and as
someone who writes & runs servers, I very much want clients to ask only for
the data that they need.

The only problem is that there isn't really a way to write GraphQL servers in
Haskell—until now.

Introducing graphql-api
-----------------------

Tom and I put together a proof-of-concept GraphQL server implementation called
`graphql-api <https://github.com/jml/graphql-api>`_, which we released to
`Hackage <http://hackage.haskell.org/package/graphql-api>`_ today.

It lets you take a `GraphQL schema <http://graphql.org/learn/schema/>`_ and
translate it into a Haskell type that represents the schema. You can then
write handlers that accept and return native Haskell types. graphql-api will
take care of parsing and validating your user queries, and Haskell's type
system will make sure that your handlers handle the right thing.

Using graphql-api
-----------------

Say you have a simple GraphQL schema, like this:

.. code-block:: graphql

    type Hello {
      greeting(who: String!): String!
    }

which defines a single top-level type ``Hello`` that contains a single field,
``greeting``, that takes a single, required argument ``who``.

A user would query it with something like this:

.. code-block:: graphql

   {
     greeting("World")
   }

And expect to see an answer like:

.. code-block:: json

   {
     "data": {
       "greeting": "Hello World!"
     }
   }

To do this in Haskell with GraphQL, first we'd define the type:

.. code-block:: haskell

   type Hello = Object "Hello" '[]
     '[ Argument "who" Text :> Field "greeting" Text ]

And then a handler for that type:

.. code-block:: haskell

   hello :: Handler IO Hello
   hello = pure greeting
    where
      greeting who = pure ("Hello " <> who <> "!")

We can then run a query like so:

.. code-block:: haskell

   queryHello :: IO Response
   queryHello = interpretAnonymousQuery @Hello hello "{ greeting(who: \"World\") }"

And get the output we expect.

There's a lot going on in this example, so I encourage you to check out
`our tutorial
<http://haskell-graphql-api.readthedocs.io/en/latest/tutorial/Introduction.html>`_
to get the full story.

graphql-api's future
--------------------

Tom and I put graphql-api together over a couple of months in our spare time
because we wanted to actually use it. However, as we dug deeper into the
implementation, we found we really enjoyed it and want to make a library
that's genuinely *good* and helps other people do cool stuff.

The only way to do *that*, however, is to release it and get feedback from our
users, and that's what we've done. So please use graphql-api and tell us what
you think. If you build something cool with it, let us know.

For our part, we want to improve the error messages, make sure our handling
for recursive data types is spot on, and smooth down a few rough edges.

Thanks
------

Tom and I want to thank `J. Daniel Navarro <https://github.com/jdnavarro>`_
for his great GraphQL parser and encoder, which forms the basis for what we
built here.


About the implementation
------------------------

graphql-api is more-or-less a GraphQL compiler hooked up to type-based
executing (aka "resolving") engine that's heavily inspired by Servant and uses
various arcane type tricks from GHC 8.

We tried to stick to implementing the `GraphQL specification
<https://facebook.github.io/graphql/>`_. The spec is very well written, but
implementing it has taught us that GraphQL is not at all as simple as it looks
at first.

I can't speak very well to the type chicanery, except to point you at
`the code
<https://github.com/jml/graphql-api/blob/master/src/GraphQL/Resolver.hs>`_
and at the `Servant paper <http://alpmestan.com/servant/servant-wgp.pdf>`_.

The compiler mostly lives in the `GraphQL.Internal.Validation
<http://hackage.haskell.org/package/graphql-api-0.1.1/docs/GraphQL-Internal-Validation.html>`_
module. The main idea is that it takes the AST and translates it into a value
that cannot possibly be wrong.

All the syntax stuff is from the original `graphql-haskell
<https://github.com/jdnavarro/graphql-haskell>`_, with a few fixes, and a
tweak to guarantee that ``Name`` values are guaranteed to be correct.
