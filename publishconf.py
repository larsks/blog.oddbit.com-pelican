#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = '//blog.oddbit.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_ATOM = None
TAG_FEED_RSS = 'tag/%s/rss/index.html'
TAG_FEED_ATOM = 'tag/%s/atom/index.html'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "oddbit"
GOOGLE_ANALYTICS = "UA-45791426-1"
