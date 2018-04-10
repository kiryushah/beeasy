# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest


class IcoAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 40)


    def IcoAccount(self):
        self.driver.get("https://beeasy.io")
        time.sleep(4)


        main_window = self.driver.current_window_handle


        #login to ico
        self.driver.find_element_by_xpath("//a[@class ='button button--user button--round']").click()
        time.sleep(5)

        self.driver.switch_to.window(main_window)

        # buy_tokens_1
        self.driver.find_element_by_xpath("//a[@class ='sale-description__button button button--white']").click()

        time.sleep(2)
        self.driver.switch_to.window(main_window)

        #buy_tokens_2
        self.driver.find_element_by_xpath("//a[@class ='promo-buttons__join button button--white']").click()

        time.sleep(2)
        self.driver.switch_to.window(main_window)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



