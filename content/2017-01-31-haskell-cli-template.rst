===============================
Announcing haskell-cli-template
===============================

:date: 2017-01-31
:tags: haskell

Last October, I `announced
<https://jml.io/2016/10/servant-template-production-ready-haskell-web-services-in-5-minutes.html>`_
`servant-template <https://github.com/jml/servant-template>`_, a `cookiecutter
<https://cookiecutter.readthedocs.io/>`_ template for creating
production-ready Haskell web services.

Almost immediately after making it, I wished I had something for building
command-line tools quickly. I know `stack
<https://docs.haskellstack.org/en/stable/README/>`_ comes with a heap of them,
but:

* it's hard to predict what they'll do
* adding a new template requires submitting a PR
* cookiecutter has existed for ages and is pretty much better in every way

So I made `haskell-cli-template
<https://github.com/jml/haskell-cli-template>`_. It's very simple, it just
makes a Haskell command-line project with some tests, command-line parsing,
and a CircleCI build.

I wanted to integrate `logging-effect
<https://hackage.haskell.org/package/logging-effect>`_, but after a few months
away from it my tired little brain wasn't able to figure it out. I like
command-line tools with logging controls, so I suspect I'll add it again in
the future.

Let me know if you use haskell-cli-template to make anything cool, and please
feel free to fork and extend.
