Title: How to write docstrings for tests
Date: 2012-12-22
Author: Jonathan Lange <me@jml.io>
Slug: test-docstrings
Alias: test-docstrings/index.html
Status: hidden

**This page**: [https://jml.io/test-docstrings/](https://jml.io/test-docstrings/)

A lot of projects I contribute to insist that tests have comments or
docstrings in them. If ever you're working on a project that has a similar
requirement, and you're struggling to write docstrings for your tests, here's
a handy five-step guide:

1. Write the first docstring that comes to mind. It will almost certainly be:

        """Test that input is parsed correctly."""

2. Get rid of "Test that" or "Check that". We know it's a test.

        """Input should be parsed correctly."""

3. Seriously?! Why'd you have to go and add "should"? It's a test, it's all
about "should".

        """Input is parsed correctly."""

4. "Correctly", "properly", and "as we expect" are all redundant. Axe them
too.

        """Input is parsed."""

5. Look at what's left. Is it saying anything at all? If so, great. If not,
   consider adding something specific about the test behaviour and perhaps
   even _why_ it's desirable behaviour to have.

        """
        Input is parsed into an immutable dict according to the config
        schema, so we get config info without worrying about input
        validation all the time.
        """

Happy hacking!﻿

Originally published as a
[post on Google+](https://plus.google.com/+JonathanLange/posts/YA3ThKWhSAj).
