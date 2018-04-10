# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest


class IcoRatings(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
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

if __name__ == "__main__":
    unittest.main()



