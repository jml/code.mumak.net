---
layout: post
tags: haskell prometheus servant docker
date: 2016-10-16
title: servant-template: production-ready Haskell web services in 5 minutes
author: jml
---

If you want to write a web API in Haskell, then you should start by using my
new cookiecutter template at https://github.com/jml/servant-template. It'll
get you a production-ready web service in 5 minutes or less.

For some values of "production". And "ready".

Whenever you start any new web service and you actually care about getting it
working and available to users, you need to get a few things sorted out:

* logging
* monitoring
* continuous integration
* tests
* deployment
* command-line parsing

These are mostly boring, but essential. Logs and monitoring give you
visibility into the code's behaviour in production, tests and continuous
integration help you make sure you don't break it, and, of course, you need
some way of actually shipping code to users. As an engineer who cares deeply
about running code in production, all of these are pretty much the bare
minimum for me to be able to deploy something to my users.

The [cookiecutter](https://cookiecutter.readthedocs.io/) template
at [gh:jml/servant-template](https://github.com/jml/servant-template) creates
a simple Haskell web API service that does all of these things:

* logging with [logging-effect](http://hackage.haskell.org/package/logging-effect)
* monitoring with [Prometheus](https://prometheus.io/)
* continuous integration with [circleci](http://circleci.com/)
* tests with [Tasty](http://documentup.com/feuerbach/tasty)
* deployment by building a [Docker](https://docker.com) image
* command-line parsing with [optparse-applicative](http://hackage.haskell.org/package/optparse-applicative)

As the name suggests, all of this enables writing
a [servant](https://haskell-servant.readthedocs.io/en/stable/) server. Servant
lets you declaring web APIs at the type-level and then using those API
specifications to write servers. It's hard to overstate just how useful it is
for writing RESTful APIs.

Get started with:

```console
$ cookiecutter gh:jml/servant-template
project_name [awesome-service]: awesome-service
...
$ cd awesome-service
$ stack test
$ make image
...
sha256:30e4c9a5f29a2c4caa44e226859dd094c6ac9d297de0d1d2024e8a981a7c8f86
awesome-service:unversioned
$ docker run awesome-service:latest --help
awesome-service - TODO fill this in

Usage: awesome-service --port PORT [--access-logs ARG] [--log-level ARG]
                       [--ghc-metrics]
  One line description of project

Available options:
  -h,--help                Show this help text
  --port PORT              Port to listen on
  --access-logs ARG        How to log HTTP access
  --log-level ARG          Minimum severity for log messages
  --ghc-metrics            Export GHC metrics. Requires running with +RTS.
$ docker run -p 8080:80 awesome-service --port 80
[2016-10-16T20:50:07.983292987000] [Informational] Listening on :80
```

For this to work, you'll need to have Docker installed on your system. I've
tested it on my Mac with [Docker Machine](https://docs.docker.com/machine/),
but haven't yet with Linux.

You might have to run `stack docker pull` before `make image`, if you haven't
already used `stack` to build things from within Docker.

Once it's up and running, you can browse to http://localhost:8080/ (or
http://$(docker-machine ip):8080/) if you're on a Mac, and you'll see a simple
HTML page describing the API and giving you a link to the `/metrics` page,
which is where all the Prometheus metrics are exported.

There you have it, a production-ready web service.

Of course, the API it offers is really simple. You'll need to go in and edit
the
[API definition](https://github.com/jml/servant-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/%7B%7B%20cookiecutter.project_name%20%7D%7D-api/src/%7B%7B%20cookiecutter.module_name%20%7D%7D/API.hs) and
the
[server implementation](https://github.com/jml/servant-template/blob/master/%7B%7B%20cookiecutter.project_name%20%7D%7D/%7B%7B%20cookiecutter.project_name%20%7D%7D-server/src/%7B%7B%20cookiecutter.module_name%20%7D%7D/Server/Handlers.hs) to
make it really your own. Note these two are in separate libraries to make it
easier to
generate
[client code](http://haskell-servant.readthedocs.io/en/stable/tutorial/Client.html).

If you're so inclined, you could push the created Docker image to a repository
somewhere—it's around 25MB when built. Then, people could use it and no one
would have to know that it's Haskell, they'd just notice a fast web service
that works.

As the [README](https://github.com/jml/servant-template/blob/master/README.md)
says, I've made a few questionable decisions when building this. If you
disagree, or think I could have done anything better
I'd [love to know](https://github.com/jml/servant-template/issues/new). If you
use this to build something cool, or even something silly, please let me know
on [Twitter](https://twitter.com/mumak).
