The End of Object Inheritance
#############################

:date: 2016-01-13 10:17
:tags: python, object-orientation, inheritance, composition
:slug: end-of-object-inheritance
:status: hidden


Foreword
========

This is an adaptation of Augie Fackler and Nathaniel Manista's excellent talk,
"The End of Object Inheritance and the Beginning of a New Modularity" (XXX:
link).

I've often exhorted people to watch The Talk (as Glyph calls it, XXX: link),
but have found that many would prefer to read an article. Likewise, I've often
wanted to refer to something in the talk, but referring to video is a bit of a
hassle.

Thus, I offer this article. It is not a straight transcript of the talk, but
rather my attempt to faithfully render its ideas as text.


Introduction
============

This page is about inheritance in Python. Its aim is partly to convince you to
stop using inheritance, but mostly to show *how* you can stop using it, and
to paint one picture of what a world without inheritance might look like.


Assumptions
===========

Before we begin, we need to document a few assumptions.

1. Types are nouns
------------------

XXX file this in

2. We express ourselves structurally
------------------------------------

Not only is programming a structured form of expression, but when we program
we express ourselves in structures: functions, methods, classes, conditionals.

When we have an idea or concept that is present in our program, we shouldn't
settle for documenting it, or putting it in a comment. Instead, we ought to
try to give that concept a symbolic name and a Python definition.

For example, rather than write:

.. code-block:: python

  # calculate the cube of x
  y = x * x * x

We should prefer to write:

.. code-block:: python

  y = cube(x)

A good way to think of this is, "if you're explaining, you're losing".

The converse also holds. If we have an idea or concept or state that we do
*not* want in our program, we should create structures that make it impossible
to represent that idea, concept, or state.

3. Most programming is parametric
---------------------------------

The vast majority of programs or "chunks of code" depend on something else.
That is, they take some sort of input. We should be as explicit as possible
about this input, and, given Assumption #2, we should express this
structurally.

In Python, this means parameters to functions.

XXX: Explain this better.


Subclassing and inheritance
===========================

Let's start with this example:

.. code-block:: python

  class MyAbstractBase(object):
      """Subclass me."""

      def orange(self):
          """Does some concrete things."""

      def green(self):
          raise NotImplementedError(self.green)

      def blue(self):
          """Does some other concrete thing."""

This contains all the ingredients of a typical base class. It has two concrete
methods, ``orange`` and ``blue``, and one abstract method, ``green``, which is
intended to be overridden by the child classes [#]_.

XXX: Describe the calling interface, how MyAbstractBases are meant to be used

.. [#] A familiar example is :py:class:`unittest.TestCase`, which is intended
       to be subclassed, and has concrete methods like ``run``,
       ``countTestCases``, and ``assertEqual``, and abstract methods like
       ``setUp`` and ``tearDown``.

Suppose we subclass this:

.. code-block:: python

   class MyConcreteClass(MyAbstractBase):
       def green(self):
           print "It's not easy being green"

Then instances of ``MyConcreteClass`` have access to the entire namespace of
``MyAbstractBase``.

XXX: Continue with namespace pollution.

Although we say ``MyConcreteClass`` inherits from ``MyAbstractBase``, there is
actually a two-way relationship between the two structures. An instance of
``MyConcreteClass`` calls methods defined in ``MyAbstractBase``, and methods
defined in ``MyAbstractBase`` can call methods defined (or overridden) in
``MyConcreteClass``.

If we are looking inside a method of a class that's part of an inheritance
hierarchy and we see:

.. code-block:: python

   def some_method(self):
       self.foo()

And ``foo`` is not defined on that class, then we don't have any way of
reasoning about its behavior. Maybe ``foo`` is on the base class, maybe ``foo`
is meant to be defined by a child class.

The only way out is to document what is supposed to call what. We have to
*explain* what's going on in *prose*, of all things. But we can do better than
that, we can express ourselves in *code*.


Unsorted notes
==============

* Composition = pass one layer into another
* Interfaces at each stage. Provide implementation. (@ ~11 mins on video;
  transcribe)
* Be crystal clear on what the first example is trying to do
* Be crystal clear on what has to be explained in the first example
* Try to find small, consistent set of things to tag: too many synonyms in
  talk
* Something interesting at ~13:40
* What we want is fault intolerance: call immediate attention to a programming
  defect
* "Composition: impossible for higher layers..." -- what does this mean
* Minsky says "Make Illegal States Unrepresentable" we want to make Illegal
  Behaviour Interactions Impossible
* To break up code:
  * minimize XXX something among resulting (?) pieces
  * remove bidirectional relationship
* Resulting code changes
  * types everywhere!
  * these types are interfaces
  * clients use interfaces not classes
    * jml: depend on abstractions, not concretions
      * XXX: find out who said this
  * public classes start to stick out
  * constructors evaporate and turn into factory functions
  * modules become things that expose (abstract!) types & functions
  * some functions become very powerful
    * XXX: Need example
  * value types peek out
    * some disagreement between Fackler & Manista here
    * cite pyrsistent
* ~22:20 they talk about how to connect
  * write code in terms of the dependencies you wish you had
  * return the things you wish you were being asked for


* http://code.google.com/a/google.com/p/end-of-object-inheritance
