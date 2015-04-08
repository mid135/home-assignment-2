# coding=utf-8
import os
import unittest
import config
from pages.page import PageObject


#fail cases
class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.topic = PageObject()
        self.topic.login(config.LOGIN)
        self.topic.go_to_topic_edit()

    def tearDown(self):
        self.topic.close()

    def test_create_without_blog(self):
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.save()
        self.assertTrue(self.topic.has_error())

    def test_create_without_title(self):
        self.topic.select_blog_by_id('Флудилка')
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.save()
        self.assertTrue(self.topic.has_error())

    def test_create_without_text(self):
        self.topic.select_blog_by_id('Флудилка')
        self.topic.set_title(config.TITLE)
        self.topic.save()
        self.assertTrue(self.topic.has_error())

    def test_create_title_long(self):
        self.topic.select_blog_by_id('Флудилка')
        self.topic.set_title('x' * (config.TITLE_BOUNDARY + 1))#loooooong
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.save()
        self.assertTrue(self.topic.has_error())


