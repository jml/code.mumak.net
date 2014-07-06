Title: Are single letter variable names evil?
Date: 2013-02-11 10:49
Author: Jonathan Lange (noreply@blogger.com)
Slug: are-single-variable-names-evil

A colleague recently asked the question, "Are single letter variable
names evil?". He was trolling, and I kind of knew it, but gosh, what an
excuse to rant about code clarity! My comments ended up being multiple
pages long, so taking one of [Mary
Gardiner](http://mary.gardiner.id.au/)'s suggestions to heart (although
I'm sure she regrets it now), I've turned it into a blog post.  
  
In a nutshell, I don't think single variable names are evil. Lots of the
time they are a bad idea though.  

<div>

The classic rule of thumb I've heard is that "the length of the variable
name should be proportional to the log of the size of the scope". I
can't find who said that originally. My [best guess is Mike
Haertel](http://www.jetcafe.org/jim/c-style.html). It seems to be a good
rule of thumb.

</div>

<div>

But the corollary is that sometimes when the code is confusing, the
problem isn't short variable names, it's that the scope is too large.

</div>

<div>

Perhaps there's also something to be said for shorter names being more
useful for really generic code? I'm OK with an implementation of `map`
taking either `f` and `xs` or `function` and `things`. I don't think
either is better or worse.

</div>

<div>

And maybe single letter variable names are acceptable when they are the
standard terms for the problem domain. `(x, y)` might be clearer than
`(horizontal_position, vertical_position)`. 

</div>

<div>

Finally, Python's idiomatic filtering strongly encourages short names,
because you have to repeat it three times within the scope of one
expression:

</div>

    [x for x in meaningfully_named_list_of_things if x.relevance > THRESHOLD]

<div>

vs:

</div>

    [meaningful_name 

     for meaningful_name in meaningfully_named_list_of_things 

     if meaningful_name.relevance > THRESHOLD]

<div>

It's probably subjective, but I think the second one is less clear,
since it obscures what's going on.﻿ Bice Dibley points out that in these
list comprehensions, `x` functions much like a pronoun in English.

</div>

<div>

As is the case when writing prose, being clear is hard. Rules can help –
taking knowledge and distilling it into formal principles is one of the
best ways for us to progress as a species! – but as Orwell said:

</div>

> Break any of these rules sooner than say anything outright barbarous.

<div>

(And [asking](http://mumak.net/stuff/your-code-sucks.html)
[someone](http://blog.labix.org/2013/02/06/ethics-for-code-reviewers) to
[look
over](http://www.codinghorror.com/blog/2006/01/code-reviews-just-do-it.html)
it soon will probably spare [troubles
later](http://www.osnews.com/story/19266/WTFs_m))

</div>
