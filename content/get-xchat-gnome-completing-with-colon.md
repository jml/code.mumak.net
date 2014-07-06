Title: Get Xchat-Gnome completing with colon
Date: 2010-09-29 17:14
Author: Jonathan Lange (noreply@blogger.com)
Slug: get-xchat-gnome-completing-with-colon

Since the late nineties, I've had my IRC clients configured to complete
nicks with a colon. For example:  
  

    <jml> dash: there's an otherwise normal guy at work who uses tcl as his scripting language of choice

  
But during some Ubuntu upgrade at some point in the last couple of
years, Xchat-Gnome changed my settings without telling me. Now it
completes nicks like this:  
  

    <jml> itamar, a cunning, enviable balance between argument and unsupported assertion

  
Which is so clearly inferior to a colon-based nick-completion that I do
not have to list the reasons. There are many.  
  
In any case, today I figured out how to change it:  
  

    /set completion_suffix :

  
That's it. Xchat will take care of saving the configuration for you. I'm
so happy.  
  
**Update:** Actually, no, Xchat does *not* take care of saving the
configuration for you.  
  
You must open `~/.xchat2/xchat.conf`, find the line that says
`completion_suffix = ,` and change it to say `completion_suffix = :` and
then, crucially, *save* your changes to that file. You'll probably have
to restart Xchat as well.

