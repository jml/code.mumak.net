Title: Emacs keybinding of (Dvorak) death
Date: 2009-01-05 01:45
Author: Jonathan Lange (noreply@blogger.com)
Slug: emacs-keybinding-of-dvorak-death

From the Emacs help  

> C-x C-- runs the command text-scale-adjust, which is an interactive
> autoloaded  
> Lisp function.  
>   
> It is bound to C-x C-+, C-x C--, C-x C-=, C-x C-0.  
>   
> (text-scale-adjust &optional INC)  
>   
> Increase or decrease the height of the default face in the current
> buffer.  
>   
> The actual adjustment made depends on the final component of the  
> key-binding used to invoke the command, with all modifiers removed:  
>   
>  +, = Increase the default face height by one step  
>  - Decrease the default face height by one step  
>  0 Reset the default face height to the global default  

C-x C-- is really, really close to C-x C-s on a Dvorak keyboard. If ever
you hit it by accident, hit C-x C-0 to get your Emacs looking right.

