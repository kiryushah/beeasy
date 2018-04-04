# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time


import unittest

class InvestBTC(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 40)

    def test_InvestBTC(self):
        self.driver.get("https://ico.beeasy.io")
        time.sleep(4)

        #login
        self.driver.find_element_by_xpath("//input[@name='user']").send_keys('alex')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('sda')
        self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-lg btn-block text-uppercase waves-effect waves-light']").click()
        wait_i = self.driver.implicitly_wait(30)
        time.sleep(3)

        #Buy ETKN by BTC
        self.driver.find_element_by_xpath("//a[@routerlink='/transactions/new/btc']").click()
        time.sleep(3)
        btc=self.driver.find_element_by_xpath("//input[@id='input-currency']")
        time.sleep(1)
        btc.clear()
        btc.send_keys('100')
        self.driver.find_element_by_xpath("//button[@id='button-buy']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@class='btn-copy text-white input-group-addon btn-info']").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
