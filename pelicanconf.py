#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'unique karki'
SITENAME = 'Inside My Brain'
SITEURL = ''
SITEURL = 'http://localhost:8000'
# SITETITLE = 'Unique Karki'
# SITESUBTITLE = 'Ideas and Thoughts'
FAVICON = '/content/extra/favicon.ico'

PATH = 'content'
STATIC_PATHS = ['images', 'extra', 'pdfs']

ICONS_PATH = 'images/icons'

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugin Path
PLUGIN_PATHS = ['./pelican-plugins']

#Plugins
PLUGINS = ['sitemap', 'post_stats', 'feed_summary','neighbors', 'assets']
  

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widge
SOCIAL = (('twitter', 'https://twitter.com/karki_nick'),
          ('github', 'https://github.com/uniquekarki'),
          ('facebook','https://www.facebook.com/unique.karki.90s'),
          ('linkedin','https://www.linkedin.com/in/unique-karki/'),
          ('envelope','mailto:unikarki@gmail.com'))	

THEME = 'themes/attila'

HOME_COVER = 'https://i.pinimg.com/originals/ad/68/aa/ad68aaf3aba030a1386f72a3b7162024.jpg'

HOME_COLOR = 'black'
COLOR_SCHEME_CSS = 'github.css'

DEFAULT_PAGINATION = 5

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Main Menu Items
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'))

# Code highlighting the theme
PYGMENTS_STYLE = 'friendly'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

AUTHORS_BIO = {
  "unique karki": {
    "name": "Unique Karki",
    #"cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
    "image": "images/potrait.jpg",
    "twitter": "karki_nick",
    "linkedin": "unique-karki",
    "github": "uniquekarki",
    "location": "Kathmandu",
    "bio": "Hi. I like programming and thinking about the absudities of life."
  }
}

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# HOME_HIDE_TAGS = True
FEED_USE_SUMMARY = True

#Custom Tag
AUTHOR_NAME = 'unique karki'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True