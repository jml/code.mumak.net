Title: Local Juju
Date: 2012-03-02 16:45
Author: Jonathan Lange (noreply@blogger.com)
Slug: local-juju

I have a bit of a fetish for being able to hack offline. It's becoming
increasingly old-fashioned, I know, but I'd like to think that
eventually it will become a quirky and charming eccentricity, such as
one might find in a British amateur sleuth.  
  
I wanted to get up and running with [Juju](https://juju.ubuntu.com/),
[Canonical](http://www.canonical.com/)'s funky cloud orchestration
thingy. We're doing a lot more service-oriented stuff in recent months,
and it's very handy to be to just deploy something without having to
faff about for a couple of hours. Since I'd like to stand a chance of
doing this without a net connection, I set it up locally.  
  
With the help of the [Charm School](https://juju.ubuntu.com/CharmSchool)
page, the [local provider
docs](https://juju.ubuntu.com/docs/provider-configuration-local.html)
and the kind folk at \#juju on Freenode, I got something up and running.
Some notes about the experience:  

-   I did all of this in precise, and it seemed to work just fine. I
    substituted 'precise' for 'oneiric' wherever I saw it.
-   I had to manually add my user to the `libvirtd` group. The
    instructions implied that this was not necessary.
-   `juju bootstrap` finished very quickly for me and without any actual
    evidence that it had debootstrapped the whole OS.
-   When I deployed services, I didn't get any feedback that anything
    was going on. The recommended `debug-log` command showed very little
    output for a while. My guess is that this was while packages were
    downloading.

<div>

All in all, pretty impressive. I'm really looking forward to mucking
around with this a bit more

</div>
