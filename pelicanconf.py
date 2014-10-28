#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vijay Kumar B.'
SITENAME = u'Chennaipy'
SITEURL = ''

SITE_LICENSE = 'Text is available under the Creative Commons Attribution-ShareAlike License.'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('ILUGC', 'http://ilugc.in/'),
         ('Python', 'http://python.org/'),
         ('PSSI', 'http://python.org.in/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/chennaipy/'),
          ('group', 'http://meetup.com/chennaipy/'),
          ('comments', 'https://mail.python.org/mailman/listinfo/chennaipy'),
          ('rss', 'feeds/all.atom.xml'),
          ('twitter', 'http://twitter.com/chennaipy'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "theme"
COVER_IMG_URL = "/static/images/rangoli.jpg"

STATIC_PATHS = ["static"]

MENUITEMS = [
    ("Events", "tag/events.html"),
    ("Meeting Minutes", "tag/meeting-minutes.html"),
    ("Credits", "pages/credits.html"),
]

#
# Use the article's filename instead of the article's title for the
# URL. This way conflict due to similar titles can be avoided
#
SLUGIFY_SOURCE = "basename"

CUSTOM_CSS = "static/css/custom.css"
