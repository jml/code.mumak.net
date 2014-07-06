Title: Documenting a Python project
Date: 2009-07-19 04:22
Author: Jonathan Lange (noreply@blogger.com)
Slug: documenting-python-project

I've recently started contributing a little to
[GTG](http://gtg.fritalk.com/), a GTD-inspired todo list application
that's hosted on [Launchpad](https://edge.launchpad.net/gtg).  
  
So far, I've made [a few UI
tweaks](https://bugs.edge.launchpad.net/gtg/+bugs?search=Search&field.assignee=jml)
and have done a bit of [infrastructural
work](https://code.edge.launchpad.net/%7Ejml/gtg/+branches?field.lifecycle=MERGED&field.lifecycle-empty-marker=1&field.sort_by=most+recently+changed+first&field.sort_by-empty-marker=1).
I'm still trying to figure out how the code fits together. Since it's
such a small code base, I don't mind writing a few docstrings for it.
And if I'm going to write docstrings, I might as well generate some API
docs, right?  
  
And so the journey begins.  
  
[Everyone
knows](http://farmdev.com/thoughts/7/housecall-from-the-pydoctor-finally-a-doc-generator-that-works-/)
that [pydoctor](http://codespeak.net/%7Emwh/pydoctor/) is the best way
to generate API docs for Python code. So I fetched it from Launchpad and
ran it according to the instructions:  

    $ bzr branch lp:pydoctor$ cd GTG$ ../pydoctor/bin/pydoctor --add-package GTG --make-html

This failed, saying it couldn't find zope.interfaces. I know I have
zope.interfaces on my system:  

    $ sagi python-zopeinterface...python-zopeinterface is already the newest version.

But, ah, this is karmic, and pydoctor is insisting on running with
Python 2.4, which is completely broken on karmic. I tweaked the
bin/pydoctor file to use the default Python and then ran the command
again.  

    $ ~/src/pydoctor/trunk/bin/pydoctor --add-package GTG --make-html

Success, I think. There's a lot of output, so it's hard to tell. Trying
again with a quiet option:  

    $ ~/src/pydoctor/trunk/bin/pydoctor --add-package GTG --make-html -qWARNING: guessing GTG for project name/home/jml/src/Divmod/trunk/Nevow/formless/annotate.py:730: DeprecationWarning: object.__new__() takes no parametersrv = cls = InterfaceClass.__new__(cls, name, bases, dct)/home/jml/src/Divmod/trunk/Nevow/nevow/testutil.py:7: DeprecationWarning: The popen2 module is deprecated.  Use the subprocess module.from popen2 import Popen3/home/jml/src/Divmod/trunk/Nevow/nevow/guard.py:15: DeprecationWarning: the md5 module is deprecated; use hashlib insteadimport md5these 6 objects' docstrings are not proper epytext:GTG.core.tagstore.Tag.__init__GTG.core.tagstore.Tag.set_attributeGTG.core.tagstore.Tag.get_all_attributesGTG.core.requester.Requester.new_taskGTG.core.requester.Requester.get_tasks_listGTG.core.requester.Requester.get_active_tasks_list

Hmm. The WARNING sucks, but I can work around that by specifying the
project name on the command line. The deprecation warnings also suck,
but I'm not quite sure what to do about them. For now, I'll invoke
python with '-W ignore::DeprecationWarning'.  
  
This is as good a point as any to point out that I had Nevow trunk
already in my PYTHONPATH. I don't know what version of Nevow you will
need.  
  
The 'not proper epytext' warnings are more worrisome. I thought I'd been
writing proper docstrings. Also, it doesn't tell me what the actual
problems are: I need to drop the '-q' option for that. This gets me too
much information. Oh hello, there's a '--verbose-about' option. Digging
into the source doesn't enlighten immediately, but bzr-grep eventually
reveals '--verbose-about=epydoc2stan2'. If I repeat '-q' twice and the
'--verbose-about' option twice, I get precisely the output I want.  

    python -W ignore::DeprecationWarning ~/src/pydoctor/trunk/bin/pydoctor \--add-package GTG --make-html --project-name=GTG \-q -q \--verbose-about=epydoc2stan2 \--verbose-about=epydoc2stan2

What I really want is a
[pyflakes](http://www.divmod.org/trac/wiki/DivmodPyflakes)-style checker
for my docstrings that I can [hook up to
flymake](http://www.plope.com/Members/chrism/flymake-mode). That way, I
can be warned about my poorly-formed docs as I'm writing them. Looking
at the pydoctor help, it doesn't look like such a thing exists. The
command above is close, but it writes too much output to disk and takes
far too long to run.  
  
Also, it's not quite right. It seems I've been writing my docstrings in
the style we use in Launchpad, rather than in epytext style. So if I use
'--docformat=restructuredtext', my docstrings are formatted properly and
I get fewer errors:  

    python -W ignore::DeprecationWarning ~/src/pydoctor/trunk/bin/pydoctor \--add-package GTG --make-html --project-name=GTG \--docformat=restructuredtext -q -q \--verbose-about=epydoc2stan2 --verbose-about=epydoc2stan2

This leaves only two formatting errors, both valid. It takes a full
second longer to generate the docs, which sucks. Still, we've got doc
generation, and we've got valid errors.  
  
The output is good, but it's not great. Take a look at the [Twisted API
docs](http://starship.python.net/crew/mwh/apidocs/), for example. I
can't quite put my finger on it, but I wish that someone with a vision
and the kind of CSS skills that you have to buy from the devil at a
crossroads at midnight would set themselves the task of making the API
docs look great.  
  
So where does this leave us:  

-   I can generate pretty good API docs easily and get told only about
    interesting errors
-   I need a pyflakes-like docstring formatting checker
-   I need a simple docstring coverage checker. I do <span>not</span>
    want to make it part of my test suite or build process.
-   I had to tweak the pydoctor source before being able to run it from
    trunk  
-   The output is OK, but it ought to be beautiful  

