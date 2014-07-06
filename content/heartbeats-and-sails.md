Title: Heartbeats and Sails
Date: 2008-07-05 12:02
Author: Jonathan Lange (noreply@blogger.com)
Tags: Testing, Hacking
Slug: heartbeats-and-sails

[Mark Shuttleworth:](http://www.markshuttleworth.com/archives/125)  

> What’s good enough performance? Well, I like to think in terms of
> “heartbeat time”. If the major operations which I have to do regularly
> (several times in an hour) take less than a heartbeat, then I don’t
> ever feel like I’m waiting. Things which happen 3-5 times in a day can
> take a bit longer, up to a minute, and those fit with regular
> workbreaks that I would take anyhow to clear my head for the next
> phase of work, or rest my aching fingers.

  
Take this rule of thumb and apply it to unit tests:  

-   Tests for whatever chunk of code you are working on should take
    "less than a heartbeat".
-   Your *entire* testing suite (that you run 3-5 times in a day,
    right?) can take longer to run, up to a minute.

  
Authors of tests and testing frameworks, there's your challenge.  
  
Tests that take too long to run just won't get run. Programmers will
postpone running the suite until the last possible moment. When using
something like [PQM](https://launchpad.net/pqm) or
[Buildbot](http://buildbot.net), this can be disastrous. Other
developers might have to wait hours for their code to land on trunk.  
  
Gerard Mezsaros's new book, [*xUnit Test
Patterns*](http://xunitpatterns.com/) has some good ideas about what to
do and what *not* to do to make your tests run in a couple of
heartbeats.

