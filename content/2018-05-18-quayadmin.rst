=====================
Announcing quay-admin
=====================

:date: 2018-05-18
:tags: python, quay, devops
:slug: announcing-quay-admin

We use `quay.io`_ a fair bit at `work`_—all our internal Docker images are stored there.
I like it a lot, but the website makes it really hard to see who can access your repositories.

In particular, if someone ever leaves your organization, you have to click through all of your repositories one at a time
to see whether they have been granted access to a repository as an individual, rather than as a member of a team.
This might be OK if you have two or three repositories, but not if you have hundreds.

I had some spare time today, so I wrote a tool to help with this.
It's called `quay-admin`_ and you can install it now:

.. code-block:: console

   $ pip install quayadmin

This will give you a command-line tool called ``quay-admin`` that you can run to see
which users outside of your organization have access to your repositories.

I originally tried to write it in Go, basing it off my colleague's excellent `quay-exporter`_ project—a tool that turns security vulnerability warnings into Prometheus metrics so you can get alerted.
Unfortunately, getting Go to work well with Swagger APIs is a bit fiddly, and I didn't have *that* much spare time.
So I tried Python, knowing that it has excellent libraries for working with RESTful services.

First cut used `requests`_, which helped me figure out which APIs I needed and how they gave me the data I wanted.
Next version used `treq`_, which allowed me to parallelize, which saves precious seconds of my only life.

It's been an age since I've written Twisted code, but it all comes rushing back fairly quickly.
I've found that I miss certain things from Haskell's `async`_ library, notably `mapConcurrently`_,
but they are easy enough to add.

Releasing Python code is way different though. At `Glyph`_'s recommendation, I tried `flit`_, which seems to work OK.

Thanks to dstufft, glyph, dreid, AlexGaynor, wsanchez, Alex_Gaynor and others
who patiently answered my questions while I was writing this,
and who in some cases wrote much of the actual software I am building on top of.

Thanks also to quay.io for actually publishing their API docs. It genuinely helps.

.. _`quay.io`: https://quay.io
.. _`work`: https://weave.works
.. _`quay-admin`: https://github.com/jml/quay-admin
.. _`quay-exporter`: https://github.com/dlespiau/quay-exporter
.. _`requests`: http://docs.python-requests.org/en/master/
.. _`treq`: https://treq.readthedocs.io/
.. _`async`: https://hackage.haskell.org/package/async
.. _`mapConcurrently`: https://hackage.haskell.org/package/async-2.2.1/docs/Control-Concurrent-Async.html#v:mapConcurrently
.. _`Glyph`: https://glyph.twistedmatrix.com/
.. _`flit`: https://github.com/takluyver/flit
