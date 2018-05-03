# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner


class BeEasyIcoPage(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        wait = WebDriverWait(self.driver, 40)


    def test_IcoPage(self):
        self.driver.get("https://beeasy.io/ru#ico")
        time.sleep(4)

        main_window = self.driver.current_window_handle

        self.driver.find_element_by_xpath("//h2[@class='ico__title']")
        self.driver.switch_to.window(main_window)

        self.driver.get("https://beeasy.io/en#ico")
        time.sleep(4)
        self.driver.find_element_by_xpath("//h2[@class='ico__title']")
        self.driver.switch_to.window(main_window)
        self.driver.switch_to.window(main_window)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)



