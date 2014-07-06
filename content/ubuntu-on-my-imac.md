Title: Ubuntu on my iMac
Date: 2011-07-10 13:52
Author: Jonathan Lange (noreply@blogger.com)
Slug: ubuntu-on-my-imac

Long time readers will know of my attempts to get Ubuntu running on my
iMac. Now that I'm working within the Ubuntu Engineering team at
Canonical, I figured it would be a good time to try again.  
  
Installing natively fails on 11.04 in the same way that it failed on
10.10: the installer sends output to the Mini DisplayPort rather than
the actual screen. I don't have an external monitor that I can hook up
to the DisplayPort, so that's pretty much that.  
  
I can still run a VM, right? VirtualBox is pretty good, and I got me a
running install of Ubuntu with the Unity shell without too much fuss.
Problem comes with keyboard configuration. The literal keypresses Cmd+H
and Cmd+Q are not passed through to the guest OS. With a Dvorak layout
these become Cmd+D and Cmd+", and if one maps Cmd to Meta then you
cannot easily kill-word in Emacs. That means for me to have a useful
environment, I'd have to make do with Super and Meta swapped around from
the usual PC layout.  
  
VM Fusion doesn't have this problem and has a nicer UI, but I can't run
Unity or compiz under it. This makes Ubuntu feel really old and clunky,
and I'd rather not do that.  
  
Parallels, well, at this point I'm running out of the will.  
  
Think I'll settle on VirtualBox for the time being.

