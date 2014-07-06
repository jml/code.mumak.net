Title: Python testing goodies
Date: 2010-01-05 00:21
Author: Jonathan Lange (noreply@blogger.com)
Slug: python-testing-goodies

Just found out that there's [a PPA with the latest releases of a whole
bunch of Python testing
goodies](https://edge.launchpad.net/~subunit/+archive/ppa), including:

<div>

-   [testtools](https://launchpad.net/testtools) - Extensions to
    unittest that make real extensions possible
-   [testresources](https://launchpad.net/testresources) - Safely re-use
    expensive resources in tests without paying massive set-up costs
-   [subunit](https://launchpad.net/subunit) - Manipulate, exchange and
    analyze test results without writing code
-   [testscenarios](https://launchpad.net/testscenarios) - Run the same
    tests against many different implementations

<div>

If you are running Ubuntu 9.10 or later, then
`sudo add-apt-repository ppa:subunit` will add it to your apt sources.

</div>

<div>

We're starting to grow a lot of useful, small testing tools that become
even more useful when combined. I really like the "small pieces, loosely
joined" approach, but sometimes that can make deployment & dependency
management a colossal pain. Happily, Ubuntu,
[Rob](http://rbtcollins.wordpress.com/) and [Launchpad
PPAs](https://edge.launchpad.net/ubuntu/+ppas) to the rescue.

</div>

</div>
