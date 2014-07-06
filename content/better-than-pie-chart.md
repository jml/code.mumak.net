Title: Better than a pie chart
Date: 2010-06-25 11:26
Author: Jonathan Lange (noreply@blogger.com)
Slug: better-than-pie-chart

The bugs page for projects on Launchpad used to have a really ugly pie
chart on them. It was a strange little graph,  useful because it helped
you feel like you were making progress as you pushed bugs from New to
Triaged to In-progress to Fix Committed and then off the chart
completely with Fix Released.  
  
Pie charts suck though. They use two dimensions to represent one
dimension of data, and they are always 100% full. In the case of bugs,
there was no way to tell from the pie chart whether there were more or
fewer bugs than last week.  
  
Inspired by some sketches from mpt, I decided to implement what I think
would be a nice graph to have on Launchpad, but to do so using the
[webservice API](https://help.launchpad.net/API). I've put some code up
on [lp:everyday](https://edge.launchpad.net/everyday), and there's [an
example of the graph for the whole Launchpad
project](http://people.canonical.com/~jml/convergence/).  
  
The code works by sucking down all of the bug tasks associated with a
project over the API, then storing them in a desktopcouch database, then
using that to generate some timeline data. The graph is made using
[flot](http://code.google.com/p/flot/), which is excellent.  
  
For those of you who care about Launchpad API details, I've recently
added a parameter to `searchTasks`{.Apple-style-span} called
`modified_since`{.Apple-style-span} that lets you [fetch only bug tasks
for bugs that have changed since a particular
date](https://bugs.edge.launchpad.net/malone/+bug/590535). It makes
syncing so much faster.

