=====================================
SPAKE2 in Haskell: How Haskell Helped
=====================================

:date: 2017-10-13
:tags: haskell, spake2
:slug: spake2-how-haskell-helped

Porting SPAKE2 from Python to Haskell helped me understand how SPAKE2 worked,
and a large part of that is due to specific features of Haskell.

What's this again?
==================

As a favour for Jean-Paul, I wrote a `Haskell library implementing SPAKE2`_,
so he could go about writing a magic-wormhole_ client.
This turned out to be `much more work than I expected`_.
Although there was a perfectly decent Python implementation for me to crib from,
my ignorance of cryptography and the lack of standards documentation for SPAKE2 made it difficult for me to be sure I was doing the right thing.

One of the things that made it *easier* was the target language: Haskell. Here's how.

Elliptic curves—how do they work?
=================================

The arithmetic around elliptic curves can be slow.
There's a trick where you can do the operations in 4D space, rather than 2D space, which somehow makes the operations faster.
Brian's code calls these "extended points". The 2D points are called "affine points".

However, there's a catch. Many of the routines can generate extended points that aren't on the curve for that we're working in, which makes them useless (possibly dangerous) for our cryptography.

The Python code deals with this using runtime checks and documentation.
There are many checks of ``isoncurve``, and comments like ``extended->extended``.

Because I `have no idea what I'm doing <{filename}/2017-05-27-spake2.rst>`_,
I wanted to make sure I got this right.

So when I defined ``ExtendedPoint``, I put whether or not the point is on the curve (in the group) into the type.

e.g.

.. code-block:: haskell

    -- | Whether or not an extended point is a member of Ed25519.
    data GroupMembership = Unknown | Member

    -- | A point that might be a member of Ed25519.
    data ExtendedPoint (groupMembership :: GroupMembership)
      = ExtendedPoint
      { x :: !Integer
      , y :: !Integer
      , z :: !Integer
      , t :: !Integer
      } deriving (Show)

This technique is called `phantom types`_.

It means we can write functions with signatures like this:

.. code-block:: haskell

    isExtendedZero :: ExtendedPoint irrelevant -> Bool

Which figures out whether an extended point is zero,
and we don't care whether it's in the group or not.

Or functions like this:

.. code-block:: haskell

    doubleExtendedPoint
      :: ExtendedPoint preserving
      -> ExtendedPoint preserving

Which says that whether or not the output is in the group is determined entirely by whether the input is in the group.

Or like this:

.. code-block:: haskell

    affineToExtended
      :: AffinePoint
      -> ExtendedPoint 'Unknown

Which means that we *know that we don't know* whether a point is on the curve
after we've projected it from affine to extended.

And we can very carefully define functions that decide whether an extended point is in the group or not, which have signatures that look like this:

.. code-block:: haskell

    ensureInGroup
      :: ExtendedPoint 'Unknown
      -> Either Error (ExtendedPoint 'Member)

This pushes our documentation and runtime checks into the type system.
It means the compiler will tell me when I accidentally pass an extended point that's not a member (or not proven to be a member) to something that assumes it is a member.

When you don't know what you are doing, this is hugely helpful.
It can feel a bit like a small child trying to push a star-shaped thing through the square-shaped hole.
The types are the holes that guide how you insert code and values.

What do we actually need?
=========================

Python famously uses "duck typing".
If you have a function that uses a value, then any value that has the right methods and attributes will work, probably.

This is very useful, but it can mean that when you are trying to figure out whether *your* value can be used, you have to resort to experimentation.

.. code-block:: python

    inbound_elem = g.bytes_to_element(self.inbound_message)
    if inbound_elem.to_bytes() == self.outbound_message:
       raise ReflectionThwarted
    pw_unblinding = self.my_unblinding().scalarmult(-self.pw_scalar)
    K_elem = inbound_elem.add(pw_unblinding).scalarmult(self.xy_scalar)

Here, ``g`` is a group. What does it need to support? What kinds of things are its elements?
How are they related?

Here's what the type signature for the corresponding Haskell function looks like:

.. code-block:: haskell

    generateKeyMaterial
      :: AbelianGroup group
      => Spake2Exchange group  -- ^ An initiated SPAKE2 exchange
      -> Element group  -- ^ The outbound message from the other side (i.e. inbound to us)
      -> Element group -- ^ The final piece of key material to generate the session key.

This makes it explicit that we need something that implements ``AbelianGroup``,
which is an interface with defined methods.

If we start to rely on something *more*, the compiler will tell us. This allows for clear boundaries.

When reverse engineering the Python code, it was never exactly clear whether a
function in a group implementation was meant to be public or private.

By having interfaces (type classes) enforced by the compiler, this is much more clear.

What comes first?
=================

The Python SPAKE2 code has a bunch of assertions to make sure that one method isn't called before another.

In particular, you really shouldn't generate the key until you've generated your message and received one from the other side.

Using Haskell, I could put this into the type system, and get the compiler to take care of it for me.

We have a function that initiates the exchange, ``startSpake2``:

.. code-block:: haskell

    -- | Initiate the SPAKE2 exchange. Generates a secret (@xy@) that will be held
    -- by this side, and transmitted to the other side in "blinded" form.
    startSpake2
      :: (AbelianGroup group, MonadRandom randomly)
      => Spake2 group
      -> randomly (Spake2Exchange group)

This takes a ``Spake2`` object for a particular ``AbelianGroup``,
which has our password scalar and protocol parameters,
and generates a ``Spake2Exchange`` for that group.

We have another function that computes the outbound message:

.. code-block:: haskell

    -- | Determine the element (either \(X^{\star}\) or \(Y^{\star}\)) to send to the other side.
    computeOutboundMessage
      :: AbelianGroup group
      => Spake2Exchange group
      -> Element group

This takes a ``Spake2Exchange`` as its input.
This means it is _impossible_ for us to call it unless we have already called ``startSpake2``.

We don't need to write tests for what happens if we try to call it before we call ``startSpake2``,
in fact, we cannot write such tests. They won't compile.

Psychologically, this helped me immensely. It's one less thing I have to worry about getting right, and that frees me up to explore other things.

It also meant I had to do less work to be satisfied with correctness.
This one line type signature replaces two or three tests.

We can also see that ``startSpake2`` is the only thing that generates random numbers.
This means we know that ``computeOutboundMessage`` will always return the same element for the same initiated exchange.

Conclusion
==========

Haskell helped me be more confident in the correctness of my code,
and also gave me tools to explore the terrain further.

It's easy to think of static types as being a constraint the binds you and prevents you from doing wrong things,
but an expressive type system can help you figure out what code to write.


.. _`Haskell library implementing SPAKE2`: https://github.com/jml/haskell-spake2
.. _magic-wormhole: https://github.com/warner/magic-wormhole
.. _`much more work than I expected`: {filename}/2017-05-27-spake2.rst
.. _`phantom types`: https://wiki.haskell.org/Phantom_type
