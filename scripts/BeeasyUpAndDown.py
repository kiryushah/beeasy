# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest


class ClickToAllElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 40)

    def test_ClickToAllElements(self):
        self.driver.get("https://beeasy.io")
        time.sleep(4)

        main_window = self.driver.current_window_handle

        #presentation
        self.driver.find_element_by_xpath("//a[@class ='page-header__button page-header__button--presentation button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='BeEasy']")
        time.sleep(2)
        self.driver.switch_to.window(main_window)

        #whitepaper
        self.driver.find_element_by_xpath("//a[@class ='page-header__button button mod']").click()
        time.sleep(2)
        self.driver.switch_to.window(main_window)

        #login to ico
        self.driver.find_element_by_xpath("//a[@class ='button button--user button--round']").click()

        time.sleep(2)
        self.driver.switch_to.window(main_window)

        # buy_tokens_1
        self.driver.find_element_by_xpath("//a[@class ='sale-description__button button button--white']").click()

        time.sleep(2)
        self.driver.switch_to.window(main_window)

        #buy_tokens_2
        self.driver.find_element_by_xpath("//a[@class ='promo-buttons__join button button--white']").click()

        time.sleep(2)
        self.driver.switch_to.window(main_window)

        #ico_ratings
        ico_rates=self.driver.find_elements_by_xpath("//a[@class='ratings__link']")
        for i in ico_rates:
            i.click()
            time.sleep(4)
            self.driver.switch_to.window(main_window)


        pages=self.driver.find_elements_by_xpath("//a[@class='page-navigation__link link']")
        for i in pages:
            i.click()
            time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



