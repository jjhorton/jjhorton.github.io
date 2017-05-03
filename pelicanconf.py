#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'James Horton'
SITENAME = u'My Little Site of Randomness'
SITEURL = 'http://jjhorton.co.uk'

PATH = 'content'
GITHUB_URL = 'http://github.com/jjhorton/'

TIMEZONE = 'Europe/London'
THEME = "/home/jjh/Documents/website/pelican-theme/"
DISPLAY_PAGES_ON_MENU = True

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('About', '/pages/about.html'),
    ('CV', '/pages/cv.html'),
)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/jjhorton'),
          ('Twitter', 'http://twitter.com/jamesjhorton'),
	  ('LinkedIn', 'http://linkedin.com/in/jjhorton'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
