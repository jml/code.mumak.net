#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jonathan Lange'
SITENAME = u'jml :: Jonathan Lange'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

INDEX_SAVE_AS = 'blog/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = (
    ('Blog', '/blog/'),
)

# XXX: Do something with these once basic publishing is back.
#
# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'pelican_alias',
    'pelican_comment_system',
    'related_posts',
]
PELICAN_COMMENT_SYSTEM = True

# Theme
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_FLUID = True
SHOW_ARTICLE_CATEGORY = True
ABOUT_ME = '''
Programmer in London, UK
'''
AVATAR = '/images/jml.png'
SOCIAL = (
    ('github', 'http://github.com/jml'),
    ('twitter', 'http://twitter.com/mumak'),
    ('google-plus', 'https://plus.google.com/+JonathanLange/'),
    ('linkedin', 'https://www.linkedin.com/profile/view?id=5746961'),
)
DISPLAY_TAGS_ON_SIDEBAR = False
CC_LICENSE = "CC-BY-NC-SA"
GITHUB_USER = 'jml'
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Don't want author pages
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = 'blog/archives/index.html'
ARCHIVES_URL = 'blog/archives/'

STATIC_PATHS = [
    'extra/CNAME',
    'images',
]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
