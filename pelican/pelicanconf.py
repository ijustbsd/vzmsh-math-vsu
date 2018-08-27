# -*- coding: utf-8 -*- #
from os import listdir

SITENAME = {
    'full': 'Воронежская зимняя математическая школа',
    'short' : 'ВЗМШ'
}
SITEURL = 'vzmsh.math-vsu.ru'

AUTHOR = 'ijustbsd@gmail.com'
DESCRIPTION = 'Воронежская зимняя математическая школа «Современные методы теории функций и смежные проблемы»'
KEYWORDS = 'Воронежская зимняя математическая школа, ВЗМШ'
YEAR = '2019'

THEME = 'theme'

SLUGIFY_SOURCE = 'basename'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

PAGE_ORDER_BY = 'order'

STATIC_PATHS = ['files', 'albums']

PHOTOS = []
for year in listdir('content/albums'):
    PHOTOS.append((year, listdir('content/albums/' + year)))

# Disable generations some files
ARCHIVES_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
FEED_ALL_ATOM = None
TAGS_SAVE_AS = None
