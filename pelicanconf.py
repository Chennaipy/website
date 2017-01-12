#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vijay Kumar B.'
SITENAME = u'Chennaipy'
TAGLINE = u'Chennai Python User Group'
SITEURL = ''
FAVICON_URL = 'https://www.python.org/static/favicon.ico'

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
SOCIAL = (('group', 'http://meetup.com/chennaipy/'),
          ('comments', 'https://mail.python.org/mailman/listinfo/chennaipy'),
          ('twitter', 'http://twitter.com/chennaipy'),
          ('rss', 'feeds/all.atom.xml'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "theme"
COVER_IMG_URL = "/static/images/vkottam.jpg"
LOGO_IMG_URL = "/static/images/logo.png"
STATIC_PATHS = ["static"]

MENUITEMS = [
    ("Events", "tag/events.html"),
    ("Meeting Minutes", "tag/meeting-minutes.html"),
    ("Credits", "pages/credits.html"),
    ("Team", "pages/team.html"),
    ("General Announcements", "tag/general-announcements.html"),
]

#
# Use the article's filename instead of the article's title for the
# URL. This way conflict due to similar titles can be avoided
#
SLUGIFY_SOURCE = "basename"

CUSTOM_CSS = "static/css/custom.css"

