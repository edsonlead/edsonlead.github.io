#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Edson Araújo'
SITENAME = 'Edson Araújo'
SITEURL = ''

#THEME PURE-SINGLE
THEME = 'theme'
TAGLINE = 'Entusiasta Python'
COVER_IMG_URL = ''
PROFILE_IMG_URL = '/images/logo.jpg'
DISQUS_SITENAME = 'earaujo'
DISQUS_ON_PAGES = 'True'
GOOGLE_ANALYTICS = 'UA-64489934-1'
##

PATH = 'content'

TIMEZONE = 'America/Belem'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'extras/CNAME', 'extras/robots.txt']
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/robots.txt': {'path': 'robots.txt'}
        }

PLUGIN_PATHS = [    
        'pelican-plugins'
        ]

PLUGINS = [
#        'gravatar',
#        'sitemap',
#        'json_articles'
        ]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.3
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
    }

# Blogroll
MENUITEMS = (('Archives', '/pages/archives.html'),
        ('Downloads', '/pages/downloads.html'),
        ('My projects', '/pages/projects.html'),
        ('About me', '/pages/about.html'),)

TEMPLATE_PAGES = {
        '../theme/templates/archives.html' : 'pages/archives.html',
        '../theme/templates/categories.html': 'pages/categories.html'
        }

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('linkedin', 'https://in.linkedin.com/in/edson-ara%C3%BAjo-81b10434'),
          ('twitter', 'https://twitter.com/earaujopy'),
          ('github', 'http://github.com/edsonlead'),
          ('envelope', 'mailto:edsonlead@gmail.com'),
          ('rss', 'feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 6
RANDOM_ARTICLES = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
