# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

class ChangePassword(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        wait = WebDriverWait(self.driver, 40)

    def test_ChangePassword(self):
        self.driver.get("https://ico.beeasy.io")
        time.sleep(4)
        #login
        self.driver.find_element_by_xpath("//input[@name='user']").send_keys('Grimebossr22@yandex.ru')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('12345678')
        self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-lg btn-block text-uppercase waves-effect waves-light']").click()
        wait_i = self.driver.implicitly_wait(30)
        time.sleep(3)

        #link to settings, change password
        self.driver.find_element_by_xpath("//a[@routerlink='/settings']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@formcontrolname='oldPassword']").send_keys('12345678')
        self.driver.find_element_by_xpath("//input[@id='input-newpassword']").send_keys('12345678')
        self.driver.find_element_by_xpath("//input[@id='input-newpasswordconfirm']").send_keys('12345678')
        self.driver.find_element_by_xpath("//button[@id='button-change']").click()
        time.sleep(2)

        #logout
        self.driver.find_element_by_xpath("//a[@class='nav-link account-link dropdown-toggle']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='mdi mdi-power']").click()
        time.sleep(4)

        #login
        self.driver.find_element_by_xpath("//input[@name='user']").send_keys('Grimebossr22@yandex.ru')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('12345678')
        self.driver.find_element_by_xpath(
            "//button[@class='btn btn-info btn-lg btn-block text-uppercase waves-effect waves-light']").click()

        time.sleep(5)



    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)




