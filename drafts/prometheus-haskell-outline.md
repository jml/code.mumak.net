# Haskell eXchange 2016 - Presentation notes

* What is your Haskell server doing?
* Who here is passionate about monitoring?
  * Bored to tears by it?
  * Somewhere in the middle?
* For me, I'm somewhere in the middle. I don't care much about monitoring, but
  I love what it gets me.
* I'm not passionate about lamps, but I love being able to move confidently
  and quickly in the dark
* I love writing servers and I love *running* them. To run them effectively
  when they are out there on the Internet, I need to be able to see. I need to
  know what's going on. Even if they are written in Haskell.

* I want to show you one way of doing that
* Prometheus is a open source pull-based monitoring system made by a bunch of
  ex-Googlers and others based on the internal monitoring system used at
  Google. It's *great*.

* So let's use it:

* In particular, I need some sense of what my *users* are seeing
  * Is the site working?
  * Is it slow?
  * How many requests am I getting?
* My colleague Tom Wilkie talks about "the RED method"
  Requests
  Errors
  Duration
  * We think these are the most important things to know about on our servers
  * In particular, these are the things we want to alert on
* A great way to get this information is Prometheus
  [XXX - prometheus logo & url]
* 
