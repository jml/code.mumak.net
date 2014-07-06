Title: Simple made easy
Date: 2012-02-01 13:50
Author: Jonathan Lange (noreply@blogger.com)
Slug: simple-made-easy

Rich Hickey did a great talk at Strange Loop called "[Simple Made
Easy](http://www.infoq.com/presentations/Simple-Made-Easy)". You should
watch it.  
  
When I tried to explain the talk to someone, I stumbled a lot and it was
obvious to me that I didn't really understand it. So I'm going through
it again and turning it into a blog post, purely for my own gain.  
  
This is roughly the first half of the talk. Not much of my own analysis
or opinion is inserted, and I've pretty much stuck with Hickey's
illustrations and phrasings. Thus this post is pretty derivative. Oops.  
  
**Simple vs Easy**  
  
"Simple" means one thing, "easy" another. Simple is the opposite of
complex. A thing is simple if it has no interleaving, if it has one
purpose, one concept, one dimension, one task. Being simple does not
imply one instance or one operation: it's about interleaving, not
cardinality. Importantly, this means that simplicity is *objective*.  
  
Easy is the opposite of hard, or difficult. A thing is easy if it's near
to hand, if it's easy to get at (location), if it's near to our
understanding (familiarity) or skill set or if it's within our
capabilities. This means that ease is *relative*.  
  
Speaking English is dead easy for me, but that doesn't mean that
speaking English is intrinsically simple. I find French quite difficult.
Little French children speak French all the time, and there's always a
part of me that thinks, "Boy, those kids are clever, being able to speak
a foreign language at that age", but that's silly. It's easy for them,
it lies near to them.  
  
This distinction between simple & easy is good one, and is useful in all
sorts of areas. But how does it relate to software?  
  
**Constructs vs Artefacts**  
  
As programmers, when we make software we are working on *constructs*:
source code, libraries, language concepts and so forth. Rich contends
that we focus on the ease of use of those constructs: How many lines of
code? How much boilerplate? Will new developers be familiar with our
technology?  
  
But all of this is secondary. What actually matters is the *artefact*,
the running programs that users actually use. Does it do what it's
supposed to do? Does it do it well? Can we rely on it working well? Can
we fix problems when they occur? Can we change it? You know, the
interesting problems.  
  
Thus we need to be assessing our constructs – our code, our technology
choices – based on the attributes of the artefacts that we'll create,
not based on the experience of typing code in.  
  
**Limits**  
  
We can't make something reliable if we don't understand it. And,
actually, everyone's understanding is pretty limited. We can all only
hold a small number of things in our head at once.  
  
When things are complex, many parts are tied together by definition. You
can't pull out just one piece and consider it because it's intertwined
with other pieces. This creates an extra burden to understanding a
system and thus makes it difficult to reason about the system.  
  
You do need to reason about a system, both to know what to change and to
be able to do so without introducing defects. Tests, refactoring, rapid
deployment and all that are great, but to make a change to the system
safely & without fear still requires you to be able to reason about it.
Every bug in your product that was found in the field passed the type
checker and passed all of the tests.  Your type system doesn't tell you
what change to make next in order to get the software you want any more
than guard rails on a highway tell you how to get to Grandma's.  
  
**Speed**  
  
Focusing on ease and ignoring simplicity means that you'll go really
fast in the beginning, but will become slower and slower as the
complexity builds.  
  
Focusing on simplicity will mean that you'll go slower in the beginning,
because you'll have to do some work to simplify the problem space, but
making sure that you only have intrinsic complexity means that your rate
of development will remain at a high constant.  
  
There are no actual numbers for this.  
  
**Complicating constructs**  
  
Many complicating constructs are available, familiar, succinctly
described and easy to use. But none of that matters to end users. What
matters is the complexity they yield. This complexity is *incidental*,
it's not intrinsic to the problem.  
  
If we build things simply, then the resulting system is easier to debug,
easier to change and easier to understand.  
  
Compare a knitted castle to a castle made of Lego. The knitted castle
might have been great fun to make, and might have been really easy if
knitted using a loom and cutting edge knitting tools, but there's no way
that it's easier to change than a Lego castle. It's not about the *ease
of construction*, it's about the *simplicity of the artefact*.  
  
**How can we make software easier?**  
  
Well, we can install it to make it easier by location. We can learn it
and try it to make it easier by familiarity. We can't do much about our
capabilities though. If we want software to be easier to comprehend, we
are going to have to bring it down to our level. We have to make it
simpler.  
  
  
Take Lisp as an example. It's hard for many people because they don't
have a Lisp installed, or their editor doesn't support paren matching,
but they can make it easier by installing a Lisp and getting a plugin
for their editor. It's also hard because it's unfamiliar. Who'd have
thought that parens could go on that side of the function? But you can
gain that familiarity quickly enough.  
  
But parens in Lisp are used for functions and for grouping data. That's
hard to get your head around, and that's because it's complex. It braids
together two distinct notions.

