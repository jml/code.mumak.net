Title: conda and binstar: initial experiences
Date: 2014-07-08

A while ago my friend [teh](https://github.com/teh) recommended that I use
[conda](http://conda.pydata.org/) for Python package management, because of
its intrinsic superiority to [pip](http://pip.readthedocs.org/en/latest/) &
[virtualenv](http://virtualenv.readthedocs.org/en/latest/). I'm no fan of
either, and teh generally has pretty good taste, so I thought I'd check it
out.

I haven't formed an overall opinion yet, but I *can* say without reservation
that the overall experience for someone who has become used to pip &
virtualenv is very frustrating.

What I found myself wanting was a one pager explaining conda & binstar to
someone familiar with pip & virtualenv, which are unquestionably vastly more
popular.  Alas, there's none to be found.

There are some guidelines here and there on the net about how to install a
package that's available on PyPI into a conda system, but they don't always
work.

For example, I'd like to play around with
[pyrsistent](http://pyrsistent.readthedocs.org/en/latest/). The recommended
approach is to do the following:

    :::console
    $ conda skeleton pypi pyrsistent
    $ conda build pyrsistent
    $ binstar upload //anaconda/conda-bld/osx-64/pyrsistent-0.3.1-py27_0.tar.bz2
    $ conda install pyrsistent

Everything works fine up until the `build` step, but the upload fails because
someone has already uploaded the package. Fine. So `conda install pyrsistent`
should work, right?

    :::console
    $ conda install pyrsistent
    Fetching package metadata: ...
    Error: No packages found matching: pyrsistent

Wut.

Searching [binstar](https://binstar.org/dashboard) finds pyristent. Apparently
I have to add some kind of channel (a concept that's not well explained, and
that does not seem to appear at all on the binstar UI).

I try this way:

    :::console
    $ conda config --add channels https://binstar.org/auto

But apparently that's not a channel:

    :::console
    $ conda install pyrsistent
    Fetching package metadata: ....Error: HTTPError: 404 Client Error: NOT FOUND: https://binstar.org/auto/osx-64/


So I try this way:

    :::console
    $ conda config --add channels https://binstar.org/auto

And that _is_ a channel, but pyrsistent it doth not find:

    :::console
    $ conda install pyrsistent
    Error: No packages found matching: pyrsistent

I take a look at the
[files page for pyrsistent](https://binstar.org/auto/pyrsistent/0.1.0/files)
and it looks like the only file is `linux-64/pyrsistent-0.1.0-py27_0.tar.bz2`.
I'm running OS X (for my sins) and my _guess_ is that the "No packages found
matching" error refers to a lack of binary builds.

So, what am I supposed to do? At this point, the documentation and the error
messages from the tools leave me with no obvious way forward. Perhaps there's
some underlying concept that would illuminate all for me, if only I could
grasp it. Perhaps it's simply a bug.

In any case, I'm not abandoning conda yet (in part because I have no idea how
to extricate it from my system), but it has some way to go before it is
properly better than pip & virtualenv.
