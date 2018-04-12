# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

class IcoRatings(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        wait = WebDriverWait(self.driver, 40)


    def IcoRatings(self):
        self.driver.get("https://beeasy.io")
        time.sleep(4)


        main_window = self.driver.current_window_handle


        #ico_ratings
        ico_rates=self.driver.find_elements_by_xpath("//a[@class='ratings__link']")
        for i in ico_rates:
            i.click()
            time.sleep(4)
            self.driver.find_element_by_link_text('BeEasy')
            self.driver.switch_to.window(main_window)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)



