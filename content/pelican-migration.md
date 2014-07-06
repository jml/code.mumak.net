Title: Migrated to Pelican
Date: 2014-07-05 15:21
Tags: pelican, blog
Summary: code.mumak.net now powered by Pelican

A while ago, I got sick of Blogger, so I switched to Octopress.

I really could not be bothered learning how to manage Ruby virtual
environments, and kept running into version issues, so I have followed
[glyph's example](https://glyph.twistedmatrix.com/2014/01/and-now-for-something-completely-different.html)
and migrated to [Pelican](http://blog.getpelican.com/).

No comments yet, and still quite a few things that ought to be done.  If you
notice something broken or missing, [please file a bug](https://github.com/jml/code.mumak.net/issues).

I'm afraid I have neither the energy nor the inclination to do a full write-up
of the migration process. However, I'll provide the following notes in case
they help anyone who wants to do the same thing.

## Patches required

* [Handle unicode authors](https://github.com/getpelican/pelican-plugins/pull/235)
* [Basic blogger import](https://github.com/getpelican/pelican/pull/1390)
* Comment support for blogger
* [Post-processing of extracted HTML](https://gist.github.com/jml/106e87af1bbf6067a94c)

## Make the blog

    :::console
    $ pelican-quickstart
    Welcome to pelican-quickstart v3.3.1.dev.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.


    > Where do you want to create your new web site? [.] code-blog
    > What will be the title of this web site? Mere Code
    > Who will be the author of this web site? Jonathan M. Lange
    > What will be the default language of this web site? [en]
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) Y
    > What is your URL prefix? (see above example; no trailing slash) http://code.mumak.net
    > Do you want to enable article pagination? (Y/n) Y
    > How many articles per page do you want? [10] 20
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
    > Do you want to upload your website using FTP? (y/N) n
    > Do you want to upload your website using SSH? (y/N)
    > Do you want to upload your website using Dropbox? (y/N)
    > Do you want to upload your website using S3? (y/N)
    > Do you want to upload your website using Rackspace Cloud Files? (y/N)
    > Do you want to upload your website using GitHub Pages? (y/N) Y
    > Is this your personal page (username.github.io)? (y/N) N


## Extract the things

    :::console
    $ pelican-import --blogger -m markdown \
      -o output-directory/ --wp-custpost --dir-page \
      blog-08-29-2013.xml

## Transfer the things

    :::console
    $ cp output-directory/* blog-directory/content/
    $ rm -rf blog-directory/content/settings blog-directory/content/templates/
    $ mv blog-directory/content/comments blog-directory

## Tweak the blog

Only
[basic tweaks](https://github.com/jml/code.mumak.net/commit/4ed1bdf23811d01de8d2ed2392350dd63f3ecd8a).
Note that the `pelican_comment_system` plugin is used in order to nicely
render the imported blogger comments.

I had to
[manually tweak the theme](https://github.com/jml/pelican-themes/commit/ae3c4d3e78d75180a4c25a22de01790b7e502bab)
to support the comment system.
