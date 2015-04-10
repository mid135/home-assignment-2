# coding=utf-8
import unittest
from pages.page import PageObject
import pages
import config
import os
from selenium.common.exceptions import NoSuchElementException

TITLE_BOUNDARY = 250

#true cases
class PostCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.topic = PageObject()
        self.topic.login(config.LOGIN)
        self.topic.go_to_topic_edit()

    def tearDown(self):
        try:
            self.topic.remove()
        except NoSuchElementException:
            pass
        self.topic.close()

    def test_create_ok(self):
        text = config.SOME_TEXT
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(text)
        self.topic.save()
        self.assertEqual(self.topic.get_content(), text)

    def test_create_title_boundary(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title('x' * TITLE_BOUNDARY)
        self.topic.set_main_text('sample text')
        self.topic.save()
        self.assertEqual(self.topic.get_title(), 'x' * TITLE_BOUNDARY)

######ERROOOR UNCOMENT TO FAIL TEST#################3WEB SITE IS BROKEN
    # def test_create_with_poll(self):
    #     self.topic.select_blog_by_id(config.BLOG)
    #     self.topic.set_title('test')
    #     self.topic.set_main_text('text very long')
    #     question = 'Question'
    #     answer1 = 'answer No. 1'
    #     answer2 = 'answer 7'
    #     self.topic.add_poll(question, answer1, answer2)
    #     self.topic.save()
    #     ans1, ans2 = self.topic.find_poll()
    #     self.assertEqual(ans1, answer1)
    #     self.assertEqual(ans2, answer2)

    def test_create_bold(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.select_text()
        self.topic.bold()
        self.topic.save()
        expected_str = '<strong>' + config.MAIN_TEXT + '</strong>'
        self.assertIn(expected_str,self.topic.get_text())

    def test_create_italic(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.select_text()
        self.topic.italic()
        self.topic.save()
        expected_str = '<em>' + config.MAIN_TEXT + '</em>'
        self.assertIn(expected_str,self.topic.get_text())

    def test_create_h4(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.select_text()
        self.topic.h4()
        self.topic.save()
        expected_str = '<h4>' + config.MAIN_TEXT + '</h4>'
        self.assertIn(expected_str,self.topic.get_text())

    def test_create_h5(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.select_text()
        self.topic.h5()
        self.topic.save()
        expected_str = '<h5>' + config.MAIN_TEXT + '</h5>'
        self.assertIn(expected_str,self.topic.get_text())

    def test_create_h6(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.select_text()
        self.topic.h6()
        self.topic.save()
        expected_str = '<h6>' + config.MAIN_TEXT + '</h6>'
        self.assertIn(expected_str,self.topic.get_text())

    def test_create_strike(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.select_text()
        self.topic.stroke()
        self.topic.save()
        expected_str = '<s>' + config.MAIN_TEXT + '</s>'
        self.assertIn(expected_str,self.topic.get_text())

    def test_create_quote(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.select_text()
        self.topic.quote()
        self.topic.save()
        expected_str = '<blockquote>' + config.MAIN_TEXT + '</blockquote>'
        self.assertIn(expected_str,self.topic.get_text())

    def test_create_code(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.select_text()
        self.topic.code()
        self.topic.save()
        expected_str = '<code>' + config.MAIN_TEXT + '</code>'
        self.assertIn(expected_str,self.topic.get_text())

    def test_create_ol(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        text = config.MAIN_TEXT + u'\n' + config.SOME_TEXT
        self.topic.set_main_text(text)
        self.topic.select_text()
        self.topic.ordered_list()
        self.topic.save()
        expected_n1= '<li>' + config.MAIN_TEXT +'</li>'
        expected_n2= '<li>' + config.SOME_TEXT +'</li>'
        self.assertIn(expected_n1,self.topic.get_ol_text())
        self.assertIn(expected_n2,self.topic.get_ol_text())
        self.assertIn('<ol>',self.topic.get_ol_text())
        self.assertIn('</ol>',self.topic.get_ol_text())

    def test_create_ul(self):
        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        text = config.MAIN_TEXT + u'\n' + config.SOME_TEXT
        self.topic.set_main_text(text)
        self.topic.select_text()
        self.topic.unordered_list()
        self.topic.save()
        expected_n1= '<li>' + config.MAIN_TEXT +'</li>'
        expected_n2= '<li>' + config.SOME_TEXT +'</li>'
        self.assertIn(expected_n1,self.topic.get_ol_text())
        self.assertIn(expected_n2,self.topic.get_ol_text())
        self.assertIn('<ul>',self.topic.get_ol_text())
        self.assertIn('</ul>',self.topic.get_ol_text())

    def test_create_uploadimage(self):
        path_to_image = unicode(os.path.dirname(__file__)) + '/images/pic.jpg'
        title = config.TITLE
        align = u'left'
        description = config.SOME_TEXT
        expected_tag = '<img'
        expected_align = 'align="' + align + '"'
        expected_description = 'title="' + description + '"'

        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(title)
        self.topic.upload_image(path_to_image, align, description)
        self.topic.save()

        inner_html=self.topic.get_text()
        self.assertIn(expected_tag, inner_html)
        self.assertIn(expected_align, inner_html)
        self.assertIn(expected_description, inner_html)

    def test_create_image_from_inet(self):
        title = config.TITLE
        align = u'left'
        description = config.SOME_TEXT
        expected_tag = '<img'
        expected_align = 'align="' + align + '"'
        expected_description = 'title="' + description + '"'

        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(title)
        self.topic.insert_image( align, description)
        self.topic.save()

        inner_html=self.topic.get_text()
        self.assertIn(expected_tag, inner_html)
        self.assertIn(expected_align, inner_html)
        self.assertIn(expected_description, inner_html)

    def test_create_image_as_link(self):
        title = config.TITLE
        align = u'left'
        description = config.SOME_TEXT

        expected_tag = '<img'
        expected_align = 'align="' + align + '"'
        expected_description = 'title="' + description + '"'
        expected_src = config.TEST_IMG

        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(title)
        self.topic.insert_image(align, description,as_link=True)
        self.topic.save()

        inner_html=self.topic.get_text()
        self.assertIn(expected_tag, inner_html)
        self.assertIn(expected_src, inner_html)
        self.assertIn(expected_align, inner_html)
        self.assertIn(expected_description, inner_html)

    def test_create_user(self):
        title = u'Добавление пользователя'
        main_text = u''
        user = u'Котегов'

        expected_attr = 'href='

        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.set_main_text(config.MAIN_TEXT)
        self.topic.add_user(user)
        self.topic.save()


        inner_html = self.topic.get_text()
        self.assertIn(expected_attr, inner_html)
        self.assertIn(user, inner_html)

    def test_create_link(self):

        self.topic.select_blog_by_id(config.BLOG)
        self.topic.set_title(config.TITLE)
        self.topic.add_link(u'http://tech-mail.ru', u'Технопарк')

        self.topic.save()
        self.assertIn('href="http://tech-mail.ru"', self.topic.get_text())
        self.assertIn(u'Технопарк', self.topic.get_text())