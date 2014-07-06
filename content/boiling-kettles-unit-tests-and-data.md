Title: Boiling kettles, unit tests and data
Date: 2010-11-26 13:34
Author: Jonathan Lange (noreply@blogger.com)
Tags: launchpad subunit data
Slug: boiling-kettles-unit-tests-and-data

The Launchpad test suite takes way too long to run: somewhere between
three and four hours.  Incidentally,
[Rob](http://rbtcollins.wordpress.com/) has just started [some
work](https://dev.launchpad.net/LEP/PersistenceLayer) that ought to make
it run a lot faster, for which I am truly thankful.  Anyway, over the
last three (almost four!) years, I've watched the test suite run many,
many times, waiting for it to finish or at least reveal a failure.  
  
It has been easy to see that not all tests are created equal. Some are
very slow, others are very fast. [Zope's terrible layer
mechanism](http://code.mumak.net/2009/09/layers-are-terrible.html) means
that these are often grouped together: slow with slow, fast with fast.
Watching the test suite churn away for the umpteenth time made me
wonder, exactly how are the tests distributed over time.  
  
Luckily, thanks to [subunit](https://launchpad.net/subunit), a [bit of
Python glue](http://paste.ubuntu.com/536368/), and OpenOffice it's
really easy to get a picture:  
  

  ----------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------
  [![](http://people.canonical.com/~jml/Tests-finished-each-minute.png)](http://people.canonical.com/~jml/Tests-finished-each-minute.png)
  ----------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------

That's a graph of the number of tests that complete within each minute
of the Launchpad test suite run.  What it means is that you are more
likely to see an actual test result if you watch at a random time during
the first half of the test run. It also means that we have a relatively
small number of very slow tests.  
  
Sometimes these graphs are more useful at lower granularity, so I made
this one:  

  --------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------
  [![](http://people.canonical.com/~jml/Tests-finished-each-ten-minutes.png)](http://people.canonical.com/~jml/Tests-finished-each-ten-minutes.png)
  --------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------

And this one:  

  ------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------
  [![](http://people.canonical.com/~jml/Tests-finished-each-hour.png)](http://people.canonical.com/~jml/Tests-finished-each-hour.png)
  ------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------

  
The [raw
data](http://people.canonical.com/~jml/testtools-experiment-r11753.subunit.gz)
is taken from a successful run of one of my recent branches. If you
download it and open it up, you'll see that the subunit output includes
a large number of "time:" statements. Each of these indicates that all
subunit statements following it should be considered as taking place at
the time given in the original statement.  
  
I used a [small Python script](http://paste.ubuntu.com/536368/) to
generate the CSVs, running it like this:  

    gzip -dc testtools-experiment-r11753.subunit.gz | python test-distribution.py 60 > /home/jml/Desktop/tests-each-minute.csv

  
Where "60" is the number of seconds of granularity.  
  
It was about twenty minutes work all up, and subunit made much of it
dead simple. subunit has its flaws, but it's a really good idea.  
  
That said, I can't help but feel that it should have been less
work. Partly, subunit should have a way to convert data to a format more
amenable to analysis by third party tools. Mostly though, those third
party tools ought to exist and be known to me.  
  
I can easily imagine a tool where I wouldn't have to run the script each
time to get a different level of granularity, but rather I could use a
slider in a UI and watch the graph update itself in real time. That
would be cool, and relatively easy. How come nobody has done that yet?  
  
Also, although OpenOffice's graphing thing is fairly nice, why isn't
there a better tool? One that makes it easier to share graphs as images
on the web without having to take crummy screenshots.

