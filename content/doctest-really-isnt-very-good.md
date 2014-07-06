Title: doctest really isn't very good
Date: 2011-09-09 17:39
Author: Jonathan Lange (noreply@blogger.com)
Slug: doctest-really-isnt-very-good

<span>I just got sick of trying to decode obtuse doctest diff errors
when using NORMALIZE\_WHITESPACE and ELLIPSIS options. Although doctest
gives you hooks to do something about this, it's really hard to actually
write the logic.</span>  
<span>  
</span>  
<span>See, NORMALIZE\_WHITESPACE also normalizes line breaks, and '...'
can match across multiple lines. That means that you can't take a
line-based approach, which makes it really hard to clean up a diff.
Anyway, here's my
attempt: </span><https://code.launchpad.net/~jml/testtools/better-doctest-output-checker/+merge/74842>  
<span>  
</span>  
<span>It's a pain, because both of them would be very useful without
their line-spanning behaviour. I guess without the line-spanning
behaviour of '...' there'd be no way to indicate multiple lines of crap
in output.</span>  
<span>  
</span>  
<span><span>My suggestion in the mean time? Don't use
doctest.</span></span>

