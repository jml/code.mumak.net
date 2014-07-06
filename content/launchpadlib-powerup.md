Title: launchpadlib powerup
Date: 2010-03-10 18:59
Author: Jonathan Lange (noreply@blogger.com)
Slug: launchpadlib-powerup

In my last post, I [introduced
launchpadlib](http://code.mumak.net/2010/03/get-started-with-launchpadlib.html)
and demonstrated a very simple script that uses it. In this post, I'd
like to build on that a bit and show you how to do something actually
interesting.  
  
In particular, I want to show you how to search for bugs, teach you a
bit about Launchpad's internal data model and help you help yourself
when it comes to figuring out Launchpad APIs.  
  
The script at
[lp:\~jml/+junk/bugstats](https://code.edge.launchpad.net/~jml/+junk/bugstats)
is designed to tell you how good you are at filing bugs. It uses a very
simple metric: out of the bugs that you've filed, how many actually have
been fixed.

    $ ./bugstats.py ubuntu jmljml is 22.22% successful on bugs in Ubuntu$ ./bugstats.py launchpad-code jmljml is 47.63% successful on bugs in Launchpad Code

To do that, we need to:

1.  get the "project" and person referred to on the command line
2.  search for all fixed bugs filed by that person
3.  search for all bugs in total by that same person
4.  count them both
5.  divide them
6.  print them!

I say "project", but I really should say "pillar", which is the
Launchpad technical term for a project (e.g. "bzr"), distribution (e.g.
"ubuntu") or project group (e.g. "gnome"). A pillar is anything in first
part of Launchpad URL that isn't a person.  
  
We get the pillar and person like this:

       pillar = launchpad.projects[pillar_name]  reporter = launchpad.people[reporter_name]

Pretty easy, huh? Now, how do we search for bug tasks?  
  
The first port of call is to go to the [Launchpad API
reference](https://launchpad.net/+apidoc) page. I'm going to look for
the string 'reporter', since that's the one thing I definitely know I
want to find.  
  
Eventually, I found the `searchTasks` method (named operation) that's on
pillars and takes a `bug_reporter` parameter and a `status` parameter.
It returns a collection of `bug_tasks`, which are the objects that
represent the rows in the table you see at the top of a bug page.  
  
I can find the bugtasks for the bugs I've reported that have been fixed
by doing:

       fixed_bugtasks = pillar.searchTasks(      bug_reporter=reporter, status=['Fix Released'])

It took me a while to figure out exactly how to spell "Fix Released". I
ended up using trial and error.  
  
Similarly, I can all the bugtasks for bugs I've filed by doing:

       total_bugtasks = pillar.searchTasks(      bug_reporter=reporter,      status=[          "New",          "Incomplete",          "Invalid",          "Won't Fix",          "Confirmed",          "Triaged",          "In Progress",          "Fix Committed",          'Fix Released'])

I cheated a bit for that one and looked at the launchpad code to get a
list of all bug statusus. The default for `searchTasks` is to only
return open bugs.  
  
Once we've got the collections of bug tasks, we need to get their
counts. In an ideal world, it would be `len(total_bugtasks)`, but sadly
[bug 274074](https://bugs.edge.launchpad.net/launchpadlib/+bug/274074)
means that `len` is really, really slow here.  
  
Instead, I wrote this helper function:

    def length(collection):  # XXX: Workaround bug 274074. Thanks wgrant.  return int(collection._wadl_resource.representation['total_size'])

With that, I can calculate & print my success rate at filing bugs:

       percentage = 100.0 * length(fixed_bugtasks) / length(total_bugtasks)  print "%s is %.2f%% successful on bugs in %s" % (      reporter.display_name, percentage, pillar.display_name)

Next up on the API, I'll talk about some of the gotchas and what you can
do about them.

