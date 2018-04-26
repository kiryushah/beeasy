# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner


class PresentationsAndWP(unittest.TestCase):


    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('headless')
        #chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        #self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 40)


    def test_PresentationsAndWP(self):
        self.driver.get("https://beeasy.io")
        time.sleep(4)


        main_window = self.driver.current_window_handle


        #presentation_russian
        self.driver.find_element_by_xpath("//a[@class ='page-header__button page-header__button--presentation button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='BeEasy']")
        time.sleep(2)
        self.driver.switch_to.window(main_window)


        #whitepaper_russian
        self.driver.find_element_by_xpath("//a[@class ='page-header__button button mod']").click()
        time.sleep(4)
        self.driver.find_elements_by_xpath("//section[@class='linkAnnotation']")
        self.driver.switch_to.window(main_window)


        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='locales__active']").click()
        self.driver.find_element_by_xpath("//a[@class='locales__item']").click()


        #presentation_english
        self.driver.find_element_by_xpath("//a[@class ='page-header__button page-header__button--presentation button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='BeEasy']")
        time.sleep(2)
        self.driver.switch_to.window(main_window)


        #whitepaper_english
        self.driver.find_element_by_xpath("//a[@class ='page-header__button button mod']").click()
        time.sleep(4)
        self.driver.find_elements_by_xpath("//section[@class='linkAnnotation']")
        self.driver.switch_to.window(main_window)



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
