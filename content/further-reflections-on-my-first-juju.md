Title: Further reflections on my first Juju charm
Date: 2012-06-22 18:19
Author: Jonathan Lange (noreply@blogger.com)
Slug: further-reflections-on-my-first-juju

Since I wrote the notes that appear in my previous post, I've had a
chance to reflect further on my experience writing a Juju charm.  
<span>  
</span>  
<span>The thing is, even though the end result is very cool – I can just
deploy this code as a new service whenever I want without having to
think about it – the experience wasn't great. I wasn't having a fun time
getting it to work. I think there are a few reasons for this.</span>  
  
<span>First, I was on my own. I work from home and most days I sit down
in my office and plug away at my laptop. I generally like it, but there
are times when it's not great. Most of the time I'm doing things I
already know how to do: debugging strange production problems; deleting
unnecessary Python code; encouraging people to get to the point in
meetings and [despairing over voice communication
technologies](https://plus.google.com/115348217455779620753/posts/J8to9rW8Ef8).</span>  
<span>  
</span>  
<span>Juju is still a fairly new technology. The [published
documentation](http://juju.ubuntu.com/docs/) is still a bit raw, the
website isn't the easiest to navigate and the tools could do a better
job at being self-documenting. It's demotivating to want to do a thing,
not know how to do it and not know how to find out how to do it. That's
one of the reasons I mentioned that \#juju is a much better place when
the US is awake: that's when the experts are around. T</span><span>he
Juju shamans know about these problems and are working now to the whole
learning experience much better.</span>  
  
Tangent: I'd very much encourage you to go to a [Charm
School](https://juju.ubuntu.com/CharmSchool) if you get the chance. The
Juju guys are super-helpful, fun to be around, and the whole thing is
much more pleasant when you're with other people and not the only one
asking dumb questions. I went to one, but I didn't do the
[preparation](https://juju.ubuntu.com/CharmSchool#Necessary_Software),
and had a dodgy laptop, so I spent all of my time head-butting network
issues rather than actually writing charms. [Do the
preparation](https://juju.ubuntu.com/docs/getting-started.html#configuring-a-local-environment).  
  
Second, the core feedback loop wasn't that great. I'm a bit spoiled.
Most of the time, I run tests, they run very quickly, I get very nicely
formatted results in colour, I fix the small, known number of failures,
I run the tests, everything works and I get a visual sweetie from
laptop. Automating the deploymment of pre-alpha software is not like
that at all.  
  
The feedback loop is longish, about 2-5 minutes. By default, you have to
sit watching the debug-log to tell when it's done or when it hits a
fatal error. <span>If you accidentally run an interactive command in
your install hook, then deployment will stall. </span><span>You don't
get any notice of success or failure, and certainly nothing that you
could integrate into your desktop (e.g. beep when done). Over two
minutes is long enough for me to get distracted, but under five minutes
is short enough that I won't switch to any task that requires
concentration. It doesn't make for a pleasant day.</span>  
<span>  
</span>  
<span>Oh, I should mention that I got stuck for a while at the very
outset, redeploying the same version of my charm because I forgot to
update the revision file and didn't realize that I actually wanted to
run deploy with the `--upgrade` option.</span>  
  
<span>When you do get errors, there are likely to be many of them, and
they are messily strewn about the debug log in hard to find places,
cluttered with useless stuff. This is largely not Juju's fault: it's the
fault of the system tools that you have to call to get things set up.
Juju's debug-log does give an option to limit output to just "ERROR"
level message, but that includes noise from things like GPG and Bazaar
(which emit to stderr as part of normal behaviour, [which Juju
interprets as ERROR](https://bugs.launchpad.net/juju/+bug/955209)). It
also doesn't give you enough context to debug the real errors. There are
also some [formatting
glitches](https://bugs.launchpad.net/juju/+bug/1015655), and it doesn't
have colour.</span>  
<span>  
</span>  
I mentioned these things about the feedback loop to a colleague. He
rightly pointed out that I was speaking very much as a programmer,
accustomed to bouncing on `make check`. For a sysadmin, being able to
redeploy on a fresh machine from scratch and see all the errors in one
place in under five minutes is a huge improvement.  
  
  
<span>Third, I have to pass on some of this knowledge to *my* users. Or
at least, people who are contributing to my project ought to be able to
quickly learn how to fire up the charm. At the moment, there are still a
few too many ifs, buts, maybes and perhaps-try-thises that I'm
[compelled to include](http://paste.ubuntu.com/1054697/). I'll probably
turn the documentation into a script at some point, as others seem to
[have](https://gist.github.com/2050525)
[done](https://gist.github.com/1406018).</span>  
<span>  
</span>  
<span>That's it. It's a *much* longer post than I expected. Sorry. I
hope it helps some.</span>  

