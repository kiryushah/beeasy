# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner


class Presentations(unittest.TestCase):


    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        #self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 40)


    def test_Presentations(self):
        self.driver.get("https://beeasy.io")
        time.sleep(4)


        main_window = self.driver.current_window_handle


        #presentation_russian
        self.driver.get("https://beeasy.io/BeEasy_3.2_Rus.pdf")
        self.driver.find_element_by_class_name('textLayer')
        self.driver.switch_to.window(main_window)


        #presentation_english
        self.driver.get("https://beeasy.io/BeEasy_3.2_Eng.pdf")
        self.driver.find_element_by_class_name('textLayer')
        self.driver.switch_to.window(main_window)



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
