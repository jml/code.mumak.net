Title: launchpadlib gotchas
Date: 2010-03-12 14:43
Author: Jonathan Lange (noreply@blogger.com)
Slug: launchpadlib-gotchas

I've shown you how to [get started with
launchpadlib](http://code.mumak.net/2010/03/get-started-with-launchpadlib.html)
and have shown a [slightly more complex launchpadlib
script](http://code.mumak.net/2010/03/launchpadlib-powerup.html).  
  
Before I cry “The power is yours!” and return to my home within the
earth, I'm going to warn you about the things that can trip you up when
using launchpadlib.  

### Bugs

[launchpadlib](https://bugs.launchpad.net/launchpadlib/) has bugs. There
are also bugs in [lazr.restful](https://bugs.launchpad.net/lazr.restful)
and [lazr.restfulclient](https://bugs.launchpad.net/lazr.restfulclient)
– two libraries that are core to launchpadlib's behaviour.

<div>

Welcome to software engineering.  
### Documentation

It's [on the wiki](https://help.launchpad.net/API), and it's good, but
it could always be better. There's a page of [as well as
a](https://help.launchpad.net/API/Examples) [guide on
launchpadlib](https://help.launchpad.net/API/launchpadlib).  
  
The [reference documentation](https://launchpad.net/+apidoc/) isn't
written for Python programmers. It's written for REST programmers.
Actually, it's not written at all but rather auto-generated from our
source code. Sometimes this can be confusing, and I frequently find
myself consulting the [Launchpad source
code](http://bazaar.launchpad.net/~launchpad-pqm/launchpad/db-devel/files)
to get things done with the API.  
### Error messages

I'm told this has got better with recent releases, but often when you
get an error in launchpadlib, it looks like an HTTP error and you have
very little help on how to debug it. Unfortunately, I don't have an
example ready.  
  
If you come across an error like this, file a bug and head straight to
\#launchpad-dev on freenode to get help.  
### Potato programming

It's really easy to write code with launchpadlib that does this:
      for thing in bunch_of_things:    thing.do_something_on_launchpad()

Code like this is really slow. It will do one round-trip per “thing”,
which can be quite expensive. Twisted folks sometimes call this “[potato
programming](http://divmod.org/trac/wiki/PotatoProgramming)”.  
### Exposure

Not all of the code within Launchpad is exposed through the API. We have
to expose things manually and we haven't done it all yet. Sorry.  
  
If you come across something that you want, then please [file a
bug](https://bugs.launchpad.net/launchpad/+filebug) and tag it with
“api”.  
  
In general, exposing something of the API is really easy or almost
impossible. If the thing you want falls into the first category, you can
probably patch Launchpad yourself.  
### Testing

Testing launchpadlib apps is hard. You do not want your unit tests to
run against launchpad.net and running your own instance of Launchpad
simply to run unit tests is masochistically stupid.  
  
I think the situation here has improved recently too, but I haven't
heard much about it or explored it myself.  
### Conclusion

There you have it, all of the gotchas for writing code with
launchpadlib. As you can see, it's not really any worse than writing for
any Python library – I'm just being up-front with you because I like
you.  
  
If any of these gotchas no longer apply, please correct me and I will
shout your good news from the rooftops.  
  
Until then, happy hacking.  

</div>
