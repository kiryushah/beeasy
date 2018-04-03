# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class LogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 40)

    def test_LogIn(self):
        self.driver.get("https://ico.beeasy.io")
        time.sleep(4)

        #login
        self.driver.find_element_by_xpath("//input[@name='user']").send_keys('alex')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('sda')
        self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-lg btn-block text-uppercase waves-effect waves-light']").click()
        wait_i = self.driver.implicitly_wait(30)
        time.sleep(3)

        #logout
        self.driver.find_element_by_xpath("//a[@class='nav-link account-link dropdown-toggle']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='mdi mdi-power']").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



