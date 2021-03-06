# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
import random

class SignUp(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        wait = WebDriverWait(self.driver, 40)


    def test_SignUp(self):
        wait=WebDriverWait(self.driver, 30)
        self.driver.get("https://ico.beeasy.io")
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[@class='text-info m-l-5']").click()
        time.sleep(3)

        #signUp
        random_email = (''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(9)]))

        self.driver.find_element_by_xpath("//input[@formcontrolname='name']").send_keys('alex')
        self.driver.find_element_by_xpath("//input[@formcontrolname='email']").send_keys(random_email+'@mail.ru')
        self.driver.find_element_by_xpath("//input[@formcontrolname='password']").send_keys('12345678')
        self.driver.find_element_by_xpath("//input[@formcontrolname='confirmPassword']").send_keys('12345678')
        time.sleep(2)
        self.driver.find_element_by_xpath("//label[@class='styled_single_checkbox custom-control custom-checkbox']").click()
        time.sleep(4)
        terms=self.driver.find_element_by_xpath("//button[@id='termsModalAgreeButton']").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-lg btn-block text-uppercase waves-effect waves-light']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='btn btn-round-blue']").click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)