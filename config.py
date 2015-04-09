__author__ = 'mid'
# -*- coding: utf-8 -*-
import os

browser_environ = 'TTHA2BROWSER'
BROWSER = os.environ.get(browser_environ, 'CHROME')


LOGIN = 'ftest8@tech-mail.ru'
PASSWORD = os.environ['TTHA2PASSWORD']
HOST = 'http://ftest.stud.tech-mail.ru/'

USERNAME = u'Степан Плюшкин'
PROFILE = '/profile/s.plyushkin/'

BLOG = 'Флудилка'
TITLE = u'Армия рядом'
MAIN_TEXT = u'Если кот - иди в морфлот!'
SOME_TEXT = u'некоторый текст'

TEST_LINK = 'http://vk.com/'
TEST_IMG = 'neobychno.com/img/2014/11/00-scary-breeds.jpg'
LOCAL_TEST_IMG = '/images/pic.jpg'

TITLE_BOUNDARY = 250
LINK_LINE = '[](http://mail.ru)'

IMG_LINE = '![]({})'.format(TEST_IMG)

TEXT_FIELD_X = '//textarea[@id="id_text"]'
BLOGSELECT_X = '//a[@class="chzn-single"]'
OPTION_X = '//li[text()="{}"]'
TITLE_X = '//input[@name="title"]'
MAIN_TEXT_X = '//textarea[@id="id_text"]'
CREATE_BUTTON_X = '//button[contains(text(),"Создать")]'
COMMENT_X = '//input[@id="id_forbid_comment"]'
POLL_X = '//input[@name="add_poll"]'