__author__ = 'mid'
import unittest
from pages.page import PageObject
import config


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.page = PageObject()
        self.page.login(config.LOGIN)

    def tearDown(self):
        self.page.close()

    def test_open_edit(self):
        self.page.open_create_topic()
        self.assertTrue(self.page.has_text_field())

