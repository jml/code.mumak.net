Title: Undistract me
Date: 2012-01-23 17:44
Author: Jonathan Lange (noreply@blogger.com)
Slug: undistract-me

Here's a thing that happens a lot to me: I'm doing some work, and as
part of that work I need to run a command in my terminal that takes a
little while. I run the command, look at it for about a second and then
switch to doing something else – checking email, perhaps. I get deeply
involved in my email checking, and then about twenty minutes later I
switch back to the terminal and see the command has finished. For all I
know, it finished nineteen minutes ago, and I was just too engrossed to
notice it.  
  
This is a big productivity sink for me, especially if the command
happened to fail and need retrying. I'm not disciplined enough to just
sit and watch the command, and I'm not prescient enough to add something
to each invocation telling me when a command is done. What I want is
something that alerts me whenever long running commands finish.  
  
Well, that thing now exists, thanks to
[glyph](http://glyph.twistedmatrix.com/)'s [script that provides precmd
and postcmd support to
bash](http://glyph.twistedmatrix.com/2006/11/bash-shell-is-now-fully-operational.html) and
a lot of help from [Chris Jones](http://www.tenshu.net/) of
[Terminator](http://www.tenshu.net/p/terminator.html).  
  
To use it right now:  
` $ bzr co lp:~jml/+junk/shell-tools`  
` $ . shell-tools/long-running.bash`  
` $ notify_when_long_running_commands_finish_install`  
  
You'll see that if you run a command that takes over 30 seconds to
complete, it will pop up a notification, which should hopefully take you
away from whatever it was you are doing and back to the task at hand.  
  
If you [look at the
code](http://bazaar.launchpad.net/~jml/+junk/shell-tools/view/head:/long-running.bash),
you'll see that it installs two hooks: `precmd` and `preexec`. `preexec`
runs just before the shell launches a command, and `precmd` runs just
before it prompts for the next command. Our `preexec` stores when the
command was launched and the `precmd` checks to see if it finished
within a certain time frame. If not, it sends out a notification.  
  
Currently, you'll get a notification when you finish reading a long
document, since the command finishes a long time after the command
starts. Obviously this isn't ideal. I think the fix is to only send
notifications when the shell doesn't have focus. Unfortunately, that's a
little tricky and I think is going to be highly terminal specific.  
  
Anyway, I'm a total shell newbie, so I'd love to know if there's any way
this could be done better.  Also let me know if you find this useful, or
you know of someone who has already done this.

