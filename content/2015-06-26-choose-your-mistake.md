Title: Choosing your mistakes
Date: 2015-06-26
Status: draft

It's the end of a long day. There are four hundred people in a room and sixty
of them are standing up because there's no room to sit. The speaker has just
thanked their sponsors, asked if there are any questions, and a brave, bearded
soul steps up to the mic and utters the dreaded words,

"Actually, this is more of a comment than a question..."

Valerie Aurora recently [posted about this on Google+](), and suggested a
better way of handling audience questions. Then someone on the comments said
"Ah, but if you do that, you'll miss out on such and such". Or something.

I'm not so interested in the specifics, but thought it made a good launching
point into something I've been thinking about recently: framing culture
questions as binary classification problems.

A binary classification problem is when you have a bunch of things and you
have some property that interests you and you want to find the things for
which the property holds. Does this patient have diabetes? Is the accused
guilty? Should we let this person on to the aeroplane? Is this email spam?
Should we merge this patch? Is this speech act tolerated within this group?
Should we hire this person? These are all binary classification problems.

You solve a binary classification problem by developing a _test_. For
diabetes, there's a blood test. For criminal guilt, the test is a series of
trials in court. For flying, there's a metal detector.

None of these tests are perfect. There are two kinds of errors that a binary
test can make: Type I or Type II. A Type I error is when you say "Yes, this
property holds" and it turns out that it's not. A Type II error is the
opposite, it's when you say "No, that couldn't possibly the case" and rather
embarrassingly, it is.

If a jury returns a verdict of guilty for an innocent person, then they've
made a Type I error. If they let a criminal go free, they've made a Type II
error.

The judicial example is particulary relevant because it shows that for social
things you can conciously choose to design your test to prefer one class of
error over another. A grand tradition of jurisprudence is that it is better
for a thousand guilty to go free than one innocent to be condemned. That is,
we'd much rather make Type II errors.

There's a knock-on effect from that. If the justice system works as intended,
we can act more freely because we aren't afraid of going to jail for no good
reason. Not only is that simply more pleasant for everyone concerned, it also
enriches society.

We can make decisions like this in our software projects. Would we rather
reject a good patch or accept a bad one?

* Precision
* Recall
* Improving the quality of tests
* Tests have a cost
* Return to speakers
* Ben Goldacre's thing on terrorists
* Link to wikipedia articles
