#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lars Kellogg-Stedman'
SITENAME = 'Odd Bits'
SITEURL = ''
SITESUBTITLE = 'One of these things is not like the others'

PATH = 'content'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 5
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'assets']

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'md-metayaml',
    'summary'
]

MENUITEMS = (
    ('Archive', '/archives.html'),
)

SOCIAL = (
    ('larsks@twitter', 'http://twitter.com/larsks'),
    ('larsks@github', 'http://github.com/larsks'),
    ('larsks@freenode', 'https://webchat.freenode.net/'),
)

DISPLAY_CATEGORIES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_URL = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'
AUTHOR_SAVE_AS = ''

SUMMARY_END_MARKER = '<!-- more -->'
SUMMARY_BEGIN_MARKER = '<!-- begin -->'

THEME = 'themes/tuxlite_tbs'
