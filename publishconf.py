#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://jml.io'
RELATIVE_URLS = True


FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
FEED_MAX_ITEMS = 10  # dlvr.it has a cap on RSS feed size

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

GITHUB_URL = 'https://github.com/jml'
TWITTER_USERNAME = 'mumak'

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
