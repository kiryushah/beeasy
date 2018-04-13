# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class LogIn(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
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


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
