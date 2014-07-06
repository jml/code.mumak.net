Title: Unfiltered reflections on my first Juju charm
Date: 2012-06-22 13:03
Author: Jonathan Lange (noreply@blogger.com)
Slug: unfiltered-reflections-on-my-first-juju

<div>

I just finished up my first [Juju](https://juju.ubuntu.com/) charm,
designed to deploy the tiny and not-yet-useful
[libdep-service](https://launchpad.net/libdep-service/), which is going
to become a micro-service used by
[pkgme-service](https://launchpad.net/pkgme-service), which exists to
automatically package submissions by application developers to
[developer.ubuntu.com](http://developer.ubuntu.com/).

</div>

<div>

The charm works, insofar as it brings up a Django service that
implements the API. It's not really ready for others to use, as it
doesn't provide any interfaces and doesn't make good use of Juju's
configuration system.

</div>

<div>

It's very early days for me as a Juju user. The notes below are largely
about problems, but I'm actually fairly optimistic that having a charm
for my service will be very useful. Two big benefits so far:

</div>

<div>

1.  There's less code than in my equivalent fabric task for deploying to
    EC2
2.  I can deploy to LXC on my laptop, which means a fast, clean, local,
    production-like environment

<div>

Anyway, on with the notes.

</div>

</div>

<ul>
<li>
<span>\#juju is heaps better when America is awake</span>

</li>
<li>
<span>upgrading with apt requires a lot of options, but this is quite a
standard</span><span> action</span>

</li>
-   <span>e.g.
    `sudo DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -q -y`</span>
-   You get this by default if you don't use sudo, and you don't have to
    use sudo

<li>
<span>so many [things that are just warnings are marked
as` ERROR`](https://bugs.launchpad.net/juju/+bug/955209), makes
debugging </span><span>much harder</span>

</li>
<li>
<span>perhaps this is intrinsic, but there are almost always four to six
errors </span><span>to be debugged at once</span>

</li>
<li>
<span>Don't use lp: URLs to fetch branches because it generates
warnings. Use http://code.launchpad.net/ instead.</span>

</li>
<li>
<span>Is there a way to have a local apt mirror or something to make
iterating</span><span> faster?  Is this what I've got already?</span>

</li>
<li>
<span>When translating from fabric `run("cd X && Y")`, remember that
fabric </span><span>restores directory after `run`</span>

</li>
-   <span><span>Use</span>`(cd X && Y)`<span> in bash instead, runs in a
    subshell</span></span>

<li>
<span>**ACTION:** Look up 'man 8 apt-get' for --force-yes and why it's
bad</span>

</li>
<li>
<span>Long-ish iteration cycle (2-5 mins) makes it a bit slow
going</span>

</li>
-   <span>See also [Users not told when deploy actually
    completes](https://bugs.launchpad.net/juju/+bug/1015644)</span>
-   <span>Iterating with 'deploy --upgrade', watch 'debug-log',
    'destroy-service', </span><span>(sometimes 'bzr ci'; 'bzr
    push')</span>

-   <span>**ACTION:** Poke around more with 'juju debug-log' (see
    also </span>["juju debug-hooks -h" doesn't say what 'debug-hooks'
    does](https://bugs.launchpad.net/juju/+bug/1016003))

<li>
<span>After delegating to puppet, if that fails, the `install` hook
doesn't fail</span>

</li>
<li>
<span><span>Ended up putting the puppet stuff should be in the charm to
avoid having to commit &</span><span> push the branch up</span></span>

</li>
<li>
<span>A little bit surprised that hooks run as root.  I don't have a
credible </span><span>alternative to hand, but I thought that this was
what we wanted to get away</span><span> from with .debs.</span>

</li>
-   <span>How do I run things with less privilege</span>

<li>
<span>I do server-side changes a fair bit to fix things. It's easy to
forget a </span><span>step when applying them back to the charm /
manifest. No easy way of</span><span> checking either.</span>

</li>
<li>
<span>Bouncing on this command is heaps
better:</span><span>`juju deploy --repository=charms --upgrade \`</span>`  local:libdep-service && jitsu watch libdep-service \    --state=started --num-units=1`

</li>
</ul>
  
  

