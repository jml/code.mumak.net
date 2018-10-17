======================
Notes on test coverage
======================

:date: 2018-10-17
:tags: haskell, testing, coverage, notes

These are a few quick notes to self, rather than a cogent thesis. I want to
get this out while it's still fresh, and I want to lower my own mental barrier
to publishing here.

I've been thinking about test coverage recently, inspired by conversations
that followed `DRMacIver's recent post`_.

Here's my current working hypothesis:

 * every new project should have 100% test coverage
 * every existing project should have a ratchet that enforces increasing coverage
 * "100% coverage" means that every line is either:
   * covered by the test suite
   * *or* has some markup in code saying that it is explicitly not covered, and why that's the case
 * these should be enforced in CI

The justification is that "the test of all knowledge is experiment" [0]_.
While we should absolutely make our code easy to reason about, and prove as
much as we can about it, we need to check what it does against actual reality.

`Simple testing really can prevent most critical failures`_. It's OK to not
test some part of your code, but that should be a conscious, local, recorded
decision. You have to explicitly opt out of test coverage. The tooling should
create a moment where you either write a test, or you turn around and say
"hold my beer".

Switching to this for an existing project can be prohibitively expensive,
though, so a ratchet is a good idea. The ratchet should be "lines of uncovered
code", and that should only be allowed to go down. Don't ratchet on
percentages, as that will let people add new lines of uncovered code.

Naturally, all of this has to be enforced in CI. No one is going to remember
to run the coverage tool, and no one is going to remember to check for it
during code review. Also, it's almost always easier to get negative feedback
from a robot than a human.

I tagged this post with Haskell, because I think all of this is theoretically
possible to achieve on a Haskell project, but requires *way* too much tooling
to set up.

 * ``hpc`` is great, but it is not particularly user friendly.
 * Existing code coverage SaaS services don't support expression-level coverage.
 * ``hpc`` has mechanisms for excluding code from coverage, but it's not by marking up your code
 * ``hpc`` has some theoretically correct but pragmatically unfortunate
   defaults, e.g. it'll report partial coverage for an ``otherwise`` guard,
   because it's never run through when ``otherwise`` is ``False``
 * There are no good ratchet tools

As a bit of an experiment, I set up a test coverage ratchet with
`graphql-api`_. I wanted both to test out my new enthusiasm for aiming for
100% coverage, and I wanted to make it easier to review PRs.

The ratchet script is some ad hoc Python, but it's working. External
contributors are actually writing tests, because the computer tells them to do
so. I need to think less hard about PRs, because I can look at the tests to
see what they actually do. And we are slowly improving our test coverage.

I want to build on this tooling to provide something genuinely good, but I
honestly don't have the budget for it at present. I hope to at least write a
good README or user guide that illustrates what I'm aiming for. Don't hold
your breath.


.. [0] *The Feynman Lectures on Physics*, Richard Feynman
.. _`DRMacIver's recent post`: https://www.drmaciver.com/2018/02/can-you-write-correct-software-in-a-statically-typed-language/
.. _`Simple testing really can prevent most critical failures`: http://www.eecg.toronto.edu/~yuan/papers/failure_analysis_osdi14.pdf
.. _`graphql-api`: https://github.com/haskell-graphql/graphql-api
