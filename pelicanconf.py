#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Unique Karki'
SITENAME = 'Unique Karki'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['extra', 'assets']
	
THEME = 'themes/attila'
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'post_stats', 'feed_summary']


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

HOME_COVER = 'https://i.pinimg.com/originals/43/2b/a1/432ba1b6206dfa853b89ceb05cfcfae7.jpg'

HOME_COLOR = 'black'
COLOR_SCHEME_CSS = 'github.css'

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/karki_nick'),
          ('github', 'https://github.com/uniquekarki'),
          ('facebook','https://www.facebook.com/unique.karki.90s'),
          ('linkedin','https://www.linkedin.com/in/unique-karki/'),
          ('envelope','mailto:unikarki@gmail.com'))

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



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

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# HOME_HIDE_TAGS = True
FEED_USE_SUMMARY = True
