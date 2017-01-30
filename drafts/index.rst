Blog ideas
##########

One section for each idea for a blog post in my backlog.

Each section has:

 * short summary
 * intended audience
 * what I hope the audience will get out of it
 * effort estimate from 1 (easy) to 5 (major project)


Parallel ``for`` loops in Rust
------------------------------

Take well-known parallel ``for`` loop patterns from Go and translate them into
Rust.

Audience: Go programmers who are curious about Rust, Rust programmers who want
to feel smug.

Effort: 4 (I've already tried doing this and found it too hard. Turns out I've
forgotten Rust.)

Outcome:
 * Go programmers feel tempted to use / explore Rust more
 * Rust programmers learn about parallelism
 * I learn about Rust

Parallel ``for`` loops in Haskell
---------------------------------

Take well-known parallel ``for`` loop patterns from Go and translate them into
Haskell.

Unlike Rust post, this would not be focusing on the merits of Haskell quite as
much, but instead using it as a vehicle for thinking about patterns in a
structured way.

Audience: ???

Effort: 3

Outcome:
 * Go programmers feel tempted to use / explore Haskell more
 * Haskell programmers learn more about parallelism
 * Haskell programmers better equipped to contend with Haskell

haskell-cli-template
--------------------

Finish up my work on the Haskell CLI template that I've made and announce it.

Audience: Haskell developers

Effort: 2

Outcome:
 * Haskell developers are better equipped to use Haskell in contexts where
   they might have previously reached for Python / Go

Trying Haskell again
--------------------

This would be a summary of what I've learned doing Haskell development over
the last four years. I don't think this is very interesting.

Highlights:

* type classes
* pattern matching
* partial application and function composition
* has a learning curve
* miss literal dict syntax

Could be spun up into Haskell vs Python.

Choose Your Mistake
-------------------

Lots of software processes come down to deciding "Yes" or "No". When you build
such processes, you should choose the kind of mistake you'd rather make, and
you should be aware of the secondary repercussions of that sort of mistake.

Audience: Software engineers in general, I guess?

Effort: 2

Outcome:
 * people design processes better?
 * people revisit their processes?


Pros & Cons of Office vs Remote
-------------------------------

I've worked remotely and in an office for a long time now. I could probably
write something interesting about this.

Not sure what the angle would be.

Audience: Software engineers in general.

Pre-merge testing
-----------------

Specifically about the trade-offs in strict "Not rocket science" pre-merge
testing, drawing on the example of Launchpad taking 4hrs to build.

Why "Why?"
----------

Start with "Why?". There's already a TED talk on this but it doesn't get said
often enough.

People seem to get this wrong all the time and it drives me up the wall.

LEPs
----

I have a "design" template that I've been shuffling around from job to job.
It's actually not a design template so much as a thing to help people get
clear on what they want.

End of Object Inheritance write-up
----------------------------------

Lots of people won't watch the video, so *someone* should write up the talk.

Effort: 5 (I tried this before and gave up)

GitHub notifications
--------------------

Simple post on how to set up GitHub notifications to maximize your
productivity.

In essence, don't watch repositories by default, *do* watch repositories that
you're the maintainer of.

GTD braindump
-------------

I wrote this already:
https://gist.github.com/jml/2d693f1e846ed0cbc116bce2b1f7d341

Polish it up.

Effort: 1

Developer UX: Our Beautiful Model
---------------------------------

I've noticed this a lot. A lot of developers will reject a user's feedback
because it will make their code uglier. "What you’re trying to do doesn’t
match our beautiful model"

Calendars
---------

They're the source of truth. Only put actual events in there.

Productivity vs Deep Work
-------------------------

Basically riff on Cal Newport's stuff, but adding a personal perspective. My
own journey through GTD and what I'm trying to do now.

Benchmarking
------------

It's really hard. How do you do this as an open source project.

What you want:
 * reproducible / stable results
 * red / green answer for incoming PRs
 * very low false positives
 * very little infrastructure overhead

And all of this is even if you are using something like ``go bench`` or
``cargo bench``.

checkState pattern
------------------

pro tip: checkState() method that asserts that all the internal state of a
data structure is consistent; call it before & after every mutation; run unit
tests

Kubernetes as a hobbyist
------------------------

Report on the labs.jml.io experiment.

GraphQL API
-----------

Announce the release. Needs to explain & justify GraphQL.

Audience: Haskell developers. Web developers.

Haskell "Validation" pattern
----------------------------

The GraphQL API uses a very simple API for handling the validation logic.
Explain how this can translate into Python.

GraphQL validation without types
--------------------------------

Notes for GraphQL wonks about how validation works without types.

Working on an open-source side-project
--------------------------------------

Jot down my experiences working on GraphQL library with Tom.

Proof by constructions
----------------------

The validation stuff goes to some effort to build values that can only
possibly be "correct" by construction. See if this idea can be generalised
usefully, perhaps even to non-typed languages.

