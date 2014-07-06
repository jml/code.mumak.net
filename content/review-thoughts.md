Title: Review Thoughts
Date: 2008-11-15 02:09
Author: Jonathan Lange (noreply@blogger.com)
Slug: review-thoughts

So, I think I've figured out what it is I dislike about Twisted's review
process: reviews aren't thorough enough.  
  
This sounds a little weird, since it's actually <span>really hard</span>
to get a patch into Twisted: it almost always takes me at least three
round trips just to get something in. But I think the number of
round-trips is actually a symptom of this lack of completeness.  
  
In Launchpad, reviews are done as in-line replies to diffs. A reviewer
is obliged to note each chunk of code that needs to be changed, along
with exactly what needs to be changed. In Twisted, reviews are done as
Trac comments and generally provided as bullet points. In Launchpad, a
reviewer would say, "You need to change foo\_bar to fooBar, because our
coding standards require camel case". In Twisted, a reviewer might say
"There are some naming convention issues".  
  
This obviously varies between reviewers and even between reviews, but I
think that the difference in technologies encourages differences in
review style.  
  
As a patch submitter, I find the in-line-comments-on-diff form much more
helpful. It provides me with a convenient todo list, and it lets me know
that the reviewer has looked through and tried to understand all of my
code. It essentially turns the review into a series of mini bug reports
with "observed, expected, how to reproduce" sections (where "how to
reproduce" is "where to find").  
  
I also like it as a reviewer, since it means less typing.

