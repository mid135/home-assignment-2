# coding=utf-8
__author__ = 'mid'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
import config
from selenium.webdriver.support.ui import Select
import os



_menu_key = '//div[@class="blogs"]/descendant::li[contains(@class, "editor-{}")]/a'

H4 = _menu_key.format("h4")
H5 = _menu_key.format("h5")
H6 = _menu_key.format("h6")
BOLD = _menu_key.format("bold")
ITALIC = _menu_key.format("italic")
STROKE = _menu_key.format("stroke")
UNDERLINE = _menu_key.format("underline")
QUOTE = _menu_key.format("quote")
CODE = _menu_key.format("code")
UL = _menu_key.format("ul")
OL = _menu_key.format("ol")
IMG = _menu_key.format("picture")
LINK = _menu_key.format("link")
USER = _menu_key.format("user")

class PageObject():

    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor=config.EXECUTOR,
            desired_capabilities=getattr(DesiredCapabilities, config.BROWSER)
        )
        self.driver.get(config.HOST)

    def show_login_form(self):
        show_button = self.driver.find_element_by_css_selector('.login-button>a')
        show_button.click()

    def login(self, login):
        self.show_login_form()
        login_field = self.driver.find_element_by_css_selector('input[name=login]')
        password_field = self.driver.find_element_by_css_selector('input[name=password]')
        form = self.driver.find_element_by_id('popup-login-form')
        login_field.send_keys(login)
        password_field.send_keys(config.PASSWORD)
        form.submit()
        wait = WebDriverWait(self.driver, 10)
        user = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'username')))
        return user.is_displayed()

    def close(self):
        self.driver.quit()

    def open_create_topic(self):
        button = self.driver.find_element_by_id('modal_write_show')
        button.click()
        wait = WebDriverWait(self.driver, 10)
        button_write = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.write-item-type-topic>.write-item-link')))
        button_write.click()

    def has_text_field(self):
        wait = WebDriverWait(self.driver, 10)
        field = wait.until(
            EC.visibility_of_element_located((By.XPATH, config.TEXT_FIELD_X)))
        return field.is_displayed()

    def select_blog_by_id(self, num):
        select = self.driver.find_element_by_xpath('//a[@class="chzn-single"]')
        select.click()
        option = self.driver.find_element_by_xpath('//li[text()="{}"]'.format(num))
        option.click()

    def go_to_topic_edit(self):
        self.driver.get(config.HOST+'blog/topic/create/')

    def set_title(self, title):
        field = self.driver.find_element_by_id('id_title')
        field.send_keys(title)


    def set_main_text(self, text):
        field = self.driver.find_element_by_xpath(config.TEXT_FIELD_X)
        ActionChains(self.driver).click(field).send_keys(text).perform();

    def get_content(self):
        content = self.driver.find_element_by_css_selector('.topic-content')
        return content.text

    def get_title(self):
        title = self.driver.find_element_by_css_selector('h1.topic-title>a')
        return title.text

    def save(self):
        form = self.driver.find_element_by_css_selector('.blogs-left>form')
        form.submit()

    def remove(self):
        remove_link = self.driver.find_element_by_xpath('//a[@class="actions-delete"]')
        remove_link.click()
        remove_form = self.driver.find_element_by_xpath('//input[@value="Удалить"]')
        remove_form.submit()

    def has_error(self):
        error = self.driver.find_element_by_class_name('system-message-error')
        return error.is_displayed()

    def bold(self):
        btn = self.driver.find_element_by_xpath(BOLD)
        btn.click()

    def italic(self):
        btn = self.driver.find_element_by_xpath(ITALIC)
        btn.click()

    def h4(self):
        btn = self.driver.find_element_by_xpath(H4)
        btn.click()

    def h5(self):
        btn = self.driver.find_element_by_xpath(H5)
        btn.click()

    def h6(self):
        btn = self.driver.find_element_by_xpath(H6)
        btn.click()

    def quote(self):
        quote_btn = self.driver.find_element_by_xpath(QUOTE)
        quote_btn.click()

    def stroke(self):
        btn = self.driver.find_element_by_xpath(STROKE)
        btn.click()

    def code(self):
        btn = self.driver.find_element_by_xpath(CODE)
        btn.click()

    def unordered_list(self):
        btn = self.driver.find_element_by_xpath(UL)
        btn.click()

    def ordered_list(self):
        btn = self.driver.find_element_by_xpath(OL)
        btn.click()

    def link(self, link):
        btn = self.driver.find_element_by_xpath('//*[@id="container"]//a[@class="markdown-editor-icon-link"][1]')
        btn.click()
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()

    def insert_image(self, link):
        btn = self.driver.find_element_by_xpath('//*[@id="container"]//a[@class="markdown-editor-icon-image"][1]')
        btn.click()
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()


    def insert_user(self):
        btn = self.driver.find_element_by_xpath('//*[@id="container"]//a[@class="markdown-editor-icon-link"][2]')
        btn.click()


    def preview(self):
        btn = self.driver.find_element_by_css_selector('#container .markdown-editor-icon-preview')
        btn.click()

    def add_poll(self, question, answer1, answer2):
        poll_checkbox = self.driver.find_element_by_xpath('//*[@class="input-checkbox add-poll"]')
        poll_checkbox.click()
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="id_question"]')))
        elem.send_keys(question)
        ans1 = self.driver.find_element_by_xpath('(//*[@id="id_form-{}-answer"])'.format(0))
        ans2 = self.driver.find_element_by_xpath('(//*[@id="id_form-{}-answer"])'.format(1))
        ans1.send_keys(answer1)
        ans2.send_keys(answer2)

    def get_editor_text(self):
        wait = WebDriverWait(self.driver, 10)
        field = wait.until(
            EC.element_to_be_clickable((By.XPATH, config.TEXT_FIELD_X)))
        return field.text

    def find_poll(self):
        ans1 = self.driver.find_element_by_xpath('(//*[@id="id_form-0-answer"])').text
        ans2 = self.driver.find_element_by_xpath('(//*[@id="id_form-1-answer"])').text
        return ans1, ans2

    def get_text(self):
        try:
            text = self.driver.find_element_by_xpath('//div[@class="topic-content text"]').get_attribute("innerHTML")
        except NoSuchElementException:
            return None
        return text


    def get_ol_text(self):
        try:
            text = self.driver.find_element_by_xpath('//div[@class="topic-content text"]').get_attribute("innerHTML")
        except NoSuchElementException:
            return None
        return text

    def get_ul_text(self):
        try:
            text = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]/ul').text
        except NoSuchElementException:
            return None
        return text

    def get_img_text(self):
        try:
            url = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]//img').get_attribute('src')
        except NoSuchElementException:
            return None
        return url

    def get_link(self):
        try:
            link = self.driver.find_element_by_xpath('//*[contains(@class, "topic-content")]//a').get_attribute('href')
        except NoSuchElementException:
            return None
        return link

    def select_text(self):
        # ActionChains(self.driver).click(self.driver.find_element(by, value)).\
        #     key_down(Keys.CONTROL).send_keys('a').send_keys('A').key_up(Keys.CONTROL).perform()
        elem = self.driver.find_element_by_xpath('//textarea[@id="id_text"]')
        elem.click()
        self.driver.execute_script("arguments[0].select();", elem)


    def upload_image(self, path_to_file, align='', description=''):
        self.driver.find_element_by_xpath('(//*[contains(text(),"изображение")])[2]').click()
        WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="window_upload_img"]'))
        )
        self.driver.find_element_by_xpath('//*[contains(text(), "С компьютера")]').click()
        self.driver.find_element_by_xpath('//*[@id="img_file"]').send_keys(path_to_file)
        align_selector = Select(self.driver.find_element_by_xpath('//*[@id="form-image-align"]'))
        align_selector.select_by_value(align)
        self.driver.find_element_by_xpath('//*[@id="form-image-title"]').click()
        self.driver.find_element_by_xpath('//*[@id="form-image-title"]').send_keys(*description)
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('.//*[@id="submit-image-upload"]').is_displayed()
        )
        self.driver.find_element_by_xpath('.//*[@id="submit-image-upload"]').click()
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: description in d.find_element_by_xpath('//*[@id="id_text"]').get_attribute('value')
        )
    def insert_image(self, align='', description='',as_link=False):
        self.driver.find_element_by_xpath('(//*[contains(text(),"изображение")])[2]').click()
        WebDriverWait(self.driver, 10, 0,1).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="window_upload_img"]'))
        )
        self.driver.find_element_by_xpath('//*[contains(text(), "Из интернета")]').click()
        self.driver.find_element_by_xpath('.//*[@id="img_url"]').send_keys(config.TEST_IMG)
        align_selector = Select(self.driver.find_element_by_xpath('//*[@id="form-image-url-align"]'))
        align_selector.select_by_value(align)
        self.driver.find_element_by_xpath('.//*[@id="form-image-url-title"]').click()
        self.driver.find_element_by_xpath('.//*[@id="form-image-url-title"]').send_keys(*description)
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath('//*[@id="submit-image-upload-link-upload"]' ).is_displayed()
        )
        if as_link:
            self.driver.find_element_by_xpath('.//*[@id="submit-image-upload-link"]' ).click()
        else:
            self.driver.find_element_by_xpath('//*[@id="submit-image-upload-link-upload"]').click()
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: description in d.find_element_by_xpath('//*[@id="id_text"]').get_attribute('value')
        )
    def add_user(self,user):
        self.driver.find_element_by_xpath('(//*[contains(text(),"Пользователь")])[2]').click()
        self.driver.find_element_by_xpath('.//*[@id="search-user-login-popup"]').click()
        self.driver.find_element_by_xpath('.//*[@id="search-user-login-popup"]').send_keys(user)
        choose_user = '//*[contains(text(), "' + user + '")]'

        WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, choose_user))
        )
        self.driver.find_element_by_xpath(choose_user).click()
        WebDriverWait(self.driver, 10, 0,1).until(
            lambda d: user in d.find_element_by_xpath('//*[@id="id_text"]').get_attribute('value')
        )

    def add_link(self,link,name):
        self.driver.find_element_by_xpath('(//*[contains(text(),"Ссылка")])[2]').click()
        WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(link)
        alert.accept()
        self.driver.find_element_by_xpath('//*[@id="id_text"]').send_keys(name)
