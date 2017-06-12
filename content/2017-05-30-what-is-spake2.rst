==================================
SPAKE2 in Haskell: What is SPAKE2?
==================================

:date: 2017-06-04
:tags: haskell, cryptography, spake2
:slug: what-is-spake2
:status: draft

`Last post`_, I discussed how I found myself implementing `SPAKE2 in Haskell`_.
Here, I want to discuss what SPAKE2 is, and why you might care.

I just want to send a file over the internet
============================================

Long ago, Glyph lamented that all he wanted to do was send a file over the internet.
Since then, very little has changed.

If you want to send a file to someone,
you either attach it to an email,
or you upload it to some central, cloud-based service that you both have access to:
Google Drive; Dropbox; iCloud; etc.

But what if you don't want to do that?
What if you want to send a file directly to someone, without intermediaries?

First, you need to figure out where they are. That's not what SPAKE2 does.

Once you have figured out where they are, you need:

1. Their permission
2. Assurance that you are sending the file to the right person
3. A secure channel to send the actual data

SPAKE2 helps with all three of these.

What is SPAKE2?
===============

SPAKE2 is a *password-authenticated key exchange* (PAKE) protocol.

This means it is a set of steps (a protocol)
to allow two parties to share a session key ("key exchange")
based on a password that they both know ("password-authenticated").

There are many such protocols,
but as mentioned `last post`_, I know next to nothing about cryptography,
so if you want to learn about them, you'll have to go elsewhere.

SPAKE2 is designed under a certain set of assumptions and constraints.

First, we don't know if the person we're talking to is the person we think we are talking to,
but we want to find out.
That is, we need to *authenticate* them,
and we want to use the password to do this (hence "password-authenticated").

Second, the shared password is expected to be weak,
such as a PIN code,
or a couple of English words stuck together.

What does this mean?
====================

These assumptons have a couple of implications.

First, we want to give our adversary as few chances as possible to guess the password.
The password is precious, we don't want to lose it.
If someone discovers it,
they could impersonate us or our friends,
and gain access to precious secrets.

Specifically, this means we want to prevent *offline dictionary attacks*
(where the adversary can snapshot some data and run it against all common passwords at their leisure)
against both *eavesdropping adversaries*
(those snooping on our connection)
and *active adversaries*
(people pretending to be our friend).

Second, we don't want to use the password as the key that encrypts our payload.
We need to use it to generate a new key, specific to this session.
If we re-use passwords, eventually we'll send some encrypted content for which the plaintext content is known,
the eavesdropper will find this and be able to brute force at their leisure.

How does SPAKE2 solve this?
===========================

To explain how SPAKE2 solves this,
it can help to go through a couple of approaches that definitely do *not* work.

For example, we could just send the password over the wire.
This is a terrible idea.
Not only does it expose the password to eavesdroppers,
but it also gives us no evidence that the other side knows the password.
After all, we could send them the password, and they could send it right back.

We need to send something over the wire that is *not* the password,
but that could only have been generated *with* the password.

So perhaps our next refinement might be that we send our name,
somehow cryptographically signed with password.

This is better than just sending the password,
but still leaves us exposed to offline dictionary attacks.
After all, our name is well-known in plain text,
so an eavesdropper can look out for it in the protocol,
snaffle up the ciphertext,
and then run a dictionary against it at their leisure.
It also leaves open the question of how we will generate a session key.

SPAKE2 goes a few steps further than this.
Rather than sending a signed version of some known text,
each side sends an "encrypted" version of a *random value*,
using the password as a key.

Each side then decrypts the value it receives from the other side,
and then uses its random value and the other random value
as inputs to a hash function that generates a session key.

If the passwords are the same, the session key will be the same,
and both sides will be able to communicate.

That is the shorter answer for "How does SPAKE2 work?".
The longer answer involves rather a lot of mathematics.

Show me the mathematics
=======================

When I was learning SPAKE2, this was a bit of a problem for me.
I hit three major hurdles.

1. Notation—maths just has obscure notation
2. Terminology—maths uses non-descriptive words for concepts
3. Concepts—some are merely unfamiliar, others genuinely difficult

In this post, I want to help you over all of these hurdles,
such that you can go and read papers and blog posts
by people who actually understand what they are talking about.
This means that I'll try to go out of my way to explain the notation and terminology
while also going through the core concepts.

I want to stress that I am not an expert.
What you're reading here is me figuring this out for myself,
with a little help from my friends and the Internet.

Overview
--------

We can think of SPAKE2 as having five stages:

1. Public system parameters, established before any exchange takes place
2. A secret password shared between two parties
3. An exchange of data
4. Using that exchange to calculate a key
5. Generating a session key

We'll deal with each in turn.

System parameters
-----------------

First, we start with some system parameters.
These are things that both ends of the SPAKE2 protocol need to have baked into their code.
As such, they are public.

These parameters are:

* a group, :math:`G`, of prime order :math:`p`
* a generator element, :math:`g`, from that group
* two arbitrary elements, :math:`M`, :math:`N`, of the group

What's a group? A group :math:`(G, +)` is a set together with a binary operator such that:

* adding any two members of the group gets you another member of the group
  (closed under :math:`+`)
* the operation + is associative, that is :math:`X + (Y + Z) = (X + Y) + Z` (associativity)
* there's an element, :math:`0`,
  such that :math:`X + 0 = X = 0 + X` for any element x in the group (identity)
* for every element, :math:`X`, there's an element :math:`-X`,
  such that :math:`X + (-X) = 0` (inverse)

It's important to note that :math:`+` stands for a generic binary operation with these properties,
not necessarily any kind of addition,
and :math:`0` stands for the identity, rather than the numeral 0.

To get a better sense of this somewhat abstract concept,
it can help to look at a few concrete examples.
These don't have much to do with SPAKE2 per se,
they are just here to help explain groups.

The integers with addition form a group with :math:`0` as the identity,
because you can add and subtract (i.e. add the negative) them and get other integers,
and because addition is associative.

The integers with multiplication are *not* a group, because what's the inverse of 2?

But the rational numbers greater than zero with multiplication *do* form a group,
with 1 as the identity.

Likewise, `integers with multiplication modulo some fixed number`_ do form a group—a finite group.
For example, for integers with multiplication modulo 7,
the identity is 1, multiplication is associative,
and the inverse of 2 is 4, because :math:`(2 \cdot 4) \mod 7 = 1`.

But but! When we are talking about groups in the abstract,
we'll still call the operation :math:`+` and the identity :math:`0`,
even if the implementation is that the operation is multiplication.

But but but! This is not at all a universally followed convention,
so when you are reading about groups, you'll often see the operation
written as a product (e.g. :math:`XY` or :math:`X \cdot Y` instead of :math:`X + Y`)
and the identity written as :math:`1`.

Still with me?

.. topic:: Why groups?

   You might be wondering why we need this "group" abstraction at all.
   It might seem like unnecessary complexity.

   Abstractions like groups are a lot like the programming concept of an abstract interface.
   You might write a function in terms of an interface
   because you want to allow for lots of different possible implementations.
   Doing so also allows you to ignore details about specific concrete implementations
   so you can focus on what matters—the external behaviour.

   It's the same thing here. The group could be an elliptic curve,
   or something to do with prime numbers, or something else entirely—SPAKE2 doesn't care.
   We want to define our protocol to allow lots of different underlying implementations,
   and without getting bogged down in how they actually work.

For SPAKE2, we have an additional requirement for the group:
it is finite and has a prime number of elements.
We'll use :math:`p` to refer to this number—this is what is meant by "of prime order :math:`p`" above.

Due to the magic of group theory [#]_, this gives :math:`G` some bonus properties:

* it is *cyclic*, we can generate all of the elements of the group by picking one (not the identity) and adding it to itself over and over
* it is `abelian`_, that is :math:`X + Y = Y + X`,
  for any two elements :math:`X`, :math:`Y` in :math:`G` (commutativity)

Which explains what we mean by "a generator element", :math:`g`,
it's just an element from the group that's not the identity.
We can use it to make any other element of the group by adding it to itself.
If the group weren't cyclic, we could, in general, only use :math:`g` to generate a subgroup.

The process of adding an element to itself over and over is called *scalar multiplication* [#]_.
In mathematical notation, we write it like this:

.. math::

   Y = nX

Or slightly more verbosely like:

.. math::

   Y = n \cdot X

Where :math:`n` is an integer
and :math:`X` is a member of the group,
and :math:`Y` is the result of adding :math:`X` to itself :math:`n` times.

If :math:`n` is 0, :math:`Y` is :math:`0`. If :math:`n` is 1, :math:`Y` is :math:`X`.

Just as sometimes the group operator is written with product notation rather than addition,
so to scalar multiplication is sometimes written with exponentiation,
to denote *multiplying* a thing by itself n times. e.g.

.. math::

  Y = X^n

I'm going to stick to the :math:`n \cdot X` notation in this post,
and I'm always going to put the scalar *first*.

Also, I am mostly going to use upper case (e.g. :math:`X`, :math:`Y`) to refer to group elements
(with the exception of the generator element, :math:`g`)
and lower case (e.g. :math:`n`, :math:`k`) to refer to scalars.
I'm going to try to be consistent, but it's always worth checking for yourself.

Because the group :math:`G` is cyclic,
if we have some group element :math:`X` and a generator :math:`g`,
there will always be a number, :math:`k`, such that:

.. math::

   X = k \cdot g

Here, :math:`k` would be called the discrete log of :math:`X` with respect to base :math:`g`.
"Log" is a nod to exponentiation notation,
"discrete" because this is a finite group.

Time to recap.

SPAKE2 has several public parameters, which are

* a group, :math:`G`, of prime order :math:`p`,
  which means it's cyclic, abelian, and we can do scalar multiplication on it
* a generator element, :math:`g`, from that group,
  that we will do a lot of scalar multiplication with
* two arbitrary elements, :math:`M`, :math:`N`, of the group,
  where `no one knows the discrete log`_ [#]_ with respect to :math:`g`.

Shared secret password
----------------------

The next thing we need to begin a SPAKE2 exchange is a shared secret password.

In human terms, this will be a short string of bytes, or a PIN.

In terms of the mathematical SPAKE2 protocol, this must be a scalar, :math:`pw`.

How we go from a string of bytes to a scalar is completely out of scope for the `SPAKE2 paper`_.
This `confused`_ me when trying to implement SPAKE2 in Haskell,
and I don't claim to fully understand it now.

We `HKDF`_ expand the password in order to get a more uniform distribution of scalars [#]_.
This still leaves us with a byte string, though.

To turn that into an integer (i.e. a scalar), we simply base256 decode the byte string.

This gives us :math:`pw`, which we use in the next step.

Data exchange
-------------

At this point, the user has entered a password and we've converted it into a scalar.

We need some way to convince the other side that we know the password
without *actually sending* the password to them.

This means two things:

1. We have to send them something *based on* the password
2. We get to use all of the shiny mathematics we introduced earlier

The process for both sides is the same, but each side needs to know who's who.
One side is side A, and other is side B,
and how they figure out which is which happens outside the protocol.

Each draw a random scalar between :math:`0` and :math:`p`: :math:`x` for side A, :math:`y` for side B.
They then use that to generate an element: :math:`X = x \cdot g` for side A,
:math:`Y = y \cdot g` for side B.

They then "blind" this value by adding it to one of the elements that make up the system parameters,
scalar multiplied by :math:`pw`, our password.

Thus, side A makes :math:`X^{\star} = X + pw \cdot M`
and side B makes :math:`Y^{\star} = Y + pw \cdot N`.

They then each send this to the other side and wait to receive the equivalent message.

Again, the papers don't say how to encode the message,
so `python-spake2`_ just base-256 encodes it
and has side A prepend the byte ``A`` (``0x41``)
and side B prepend ``B`` (``0x42``).


Calculating a key
-----------------

Once each side has the other side's message, they can start to calculate a key.

Side A calculates its key like this:

.. math::

   K_A = x \cdot (Y^{\star} - pw \cdot N)

The bit inside the parentheses is side A recovering :math:`Y`,
since we defined :math:`Y^{\star}` as:

.. math::

   Y^{\star} = Y + pw \cdot N

We can rewrite that in terms of :math:`Y` by subtracting :math:`pw \cdot N` from both sides:

.. math::

   Y = Y^{\star} - pw \cdot N

Which means, as long as both sides have the same value for :math:`pw`,
can swap in :math:`Y` like so:

.. math::

   K_A& = x \cdot Y \\
      & = x \cdot (y \cdot g) \\
      & = xy \cdot g

Remember that when we created :math:`Y` in the first place,
we did so by multiplying our generator :math:`g` by a random scalar :math:`y`.

Side B calculates its key in the same way:

.. math::

   K_B& = y \cdot (X^{\star} - pw \cdot N) \\
      & = y \cdot X \\
      & = y \cdot (x \cdot g) \\
      & = yx \cdot g \\
      & = xy \cdot g

Thus, if both sides used the same password, :math:`K_A = K_B`.

Generating a session key
------------------------

Both sides now have:

- :math:`X^{\star}`
- :math:`Y^{\star}`
- Either :math:`K_A` or :math:`K_B`
- :math:`pw`, or at least their own opinion of what :math:`pw` is

To these we add the heretofore unmentioned :math:`A` and :math:`B`,
which are meant to be identifiers for side A and side B respectively.
Each side presumably communicates these to each other out-of-band to SPAKE2.

We then hash all of these together, using a hash algorithm, :math:`H`,
that both sides have previously agreed upon, so that:

.. math::

   SK = H(A, B, X^{\star}, Y^{\star}, pw, K)

Where :math:`K` is either :math:`K_A` or :math:`K_B`.

I don't really understand why this step is necessary—why not use :math:`K`?
Nor do I understand why each of the inputs to the hash is necessary—:math:`K`
is already derived from :math:`X^{\star}`, why do we need :math:`X^{\star}`?

In the code, we change this ever so slightly:

.. math::

   SK = H(H(pw), H(A), H(B), X^{\star}, Y^{\star}, K)

Basically, we hash all of the variable length fields to make them fixed length
to avoid collisions between values. [#]_

python-spake2 uses SHA256 as the hash algorithm for this step.
I've got no idea why this and not, say, HKDF.

And this is the session key. SPAKE2 is done!


Did SPAKE2 solve our problem?
=============================

We wanted a way of authenticating a remote connection using a password,
without having to share that password,
and without using that password to encrypt known plaintext. We've done that.

The SPAKE2 protocol above will result in two sides negotiating a shared session key,
sending only randomly generated data over the wire.

Is it vulnerable to offline dictionary attacks? No.
The value we send over the wire is just a random group element encrypted with the password.
Even if an eavesdropper gets that value and runs a dictionary against it,
they'll have no way of determining whether they've cracked it or not.
After all, one random value looks very much like another.


Where to now?
=============

I'm looking forward to learning about elliptic curves,
and to writing about what it was like to use Haskell in particular to implement SPAKE2.

I learned a lot implementing SPAKE2,
then learned a lot more writing this post,
and have much to learn still.

But perhaps the biggest thing I've learned is that although maths isn't easy,
it's at least possible, and that sometimes,
if you want to send a file over the Internet,
what you really need is a huge pile of math.

Let me know if I've got anything wrong,
or if this inspires you do go forth and implement some crypto papers yourself.

Thanks
======

This post owes a great deal to `Brian Warner's "Magic Wormhole" talk <https://www.youtube.com/watch?v=oFrTqQw0_3c>`_,
to `Jake Edge's write-up of that talk <https://lwn.net/Articles/692061/>`_,
and to `Michel Abdalla and David Pointcheval's paper "Simple Password-Based Encrypted Key Exchange Protocols"
<http://www.di.ens.fr/~pointche/Documents/Papers/2005_rsa.pdf>`_.

`Bice Dibley <http://life.metagnome.net/>`_,
`Chris Halse Rogers <https://twitter.com/raof_47>`_,
and `JP Viljoen <https://keybase.io/froztbyte>`_
all read early drafts and provided helpful suggestions.
This piece has been much improved by their input.
Any infelicities are my own.

I wouldn't have written this without being inspired by `Julia Evans <https://jvns.ca/>`_.
Julia often shares what she's learning as she learns it,
and does a great job at making difficult topics seem approachable and fun.
I highly recommend her blog, especially if you're into devops or distributed systems.

.. _`Last post`: {filename}/2017-05-27-spake2.rst
.. _`SPAKE2 in Haskell`: https://github.com/jml/haskell-spake2
.. _magic-wormhole: https://github.com/warner/magic-wormhole
.. _`integers with multiplication modulo some fixed number`: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
.. _`no one knows the discrete log`: http://www.lothar.com/blog/54-spake2-random-elements/
.. _`Simple Password-Based Encrypted Key Exchange Protocols`: http://www.di.ens.fr/~pointche/Documents/Papers/2005_rsa.pdf
.. _`SPAKE2 paper`: `Simple Password-Based Encrypted Key Exchange Protocols`_
.. _`confused`: {filename}/2017-05-27-spake2.rst#protocols-ain-t-protocols
.. _`HKDF`: https://tools.ietf.org/html/rfc5869
.. _`python-spake2`: https://github.com/warner/python-spake2
.. _`abelian`: https://en.wikipedia.org/wiki/Abelian_group

.. [#] I used to know the proof for this but have since forgotten it, so I'm taking this on faith for now.
.. [#] With scalar multiplication, we aren't talking about a group, but rather a :math:`\mathbb{Z}`-module.
       But at this point, I can't even, so `look it up on Wikipedia <https://en.wikipedia.org/wiki/Module_(mathematics)>`_ if you're interested.
.. [#] Taking this on faith too.
.. [#] Yup, faith again.
.. [#] I only sort of understand why this is necessary.
