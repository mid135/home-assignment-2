__author__ = 'mid'
# -*- coding: utf-8 -*-
import os

browser_environ = 'TTHA2BROWSER'
BROWSER = os.environ.get(browser_environ, 'CHROME')

LOGIN = 'ftest8@tech-mail.ru'
PASWWORD = 'Pa$$w0rD-8'
#PASSWORD = os.environ['TTHA2PASSWORD']

USERNAME = u'Степан Плюшкин'
PROFILE = '/profile/s.plyushkin/'

BLOG = u'Флудилка'
TITLE = u'Армия рядом'
MAIN_TEXT = u'Если кот - иди в морфлот!'
SOME_TEXT = u'некоторый текст'

TEST_LINK = 'http://vk.com/'
TEST_IMG = 'neobychno.com/img/2014/11/00-scary-breeds.jpg'
LOCAL_TEST_IMG = '/images/pic.jpg'

TITLE_BOUNDARY = 250
LINK_LINE = '[](http://mail.ru)'

IMG_LINE = '![]({})'.format(TEST_IMG)