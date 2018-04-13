# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner


class ClcikToAll(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        wait = WebDriverWait(self.driver, 40)

    def ClickToAll(self):
        self.driver.get("https://ico.beeasy.io")
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@name='user']").send_keys('alex')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('sda')
        self.driver.find_element_by_xpath(
            "//button[@class='btn btn-info btn-lg btn-block text-uppercase waves-effect waves-light']").click()
        wait_i = self.driver.implicitly_wait(30)
        time.sleep(3)

        wait_i
        self.driver.find_element_by_xpath("//a[@href='/transactions']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@href='/about']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@href='/kyc']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='navbar-brand']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@class='btn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@id='open-language']").click()
        wait_i
        self.driver.find_element_by_xpath("//a[@id='language-en']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@id='open-language']").click()
        wait_i
        self.driver.find_element_by_xpath("//a[@id='language-ru']").click()
        time.sleep(2)

        self.driver.find_element_by_xpath("//a[@class='nav-link account-link dropdown-toggle']").click()
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        time.sleep(2)

        #logout
        self.driver.find_element_by_xpath("//a[@class='nav-link account-link dropdown-toggle']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='mdi mdi-power']").click()
        time.sleep(4)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)


