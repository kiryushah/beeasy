# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import unittest
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

class Kyc(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('no-sandbox')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        wait = WebDriverWait(self.driver, 40)

    def test_Kyc(self):
        self.driver.get("https://ico.beeasy.io")
        time.sleep(4)

        #login
        self.driver.find_element_by_xpath("//input[@name='user']").send_keys('k1ch.ka@yandex.ru')
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys('12345678')
        self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-lg btn-block text-uppercase waves-effect waves-light']").click()
        wait_i = self.driver.implicitly_wait(30)
        time.sleep(3)

        #link to kyc
        self.driver.find_element_by_xpath("//a[@routerlink='/kyc']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@formcontrolname='name']").send_keys('Alex')
        self.driver.find_element_by_xpath("//input[@formcontrolname='country']").send_keys('Russia')
        self.driver.find_element_by_xpath("//input[@formcontrolname='address']").send_keys(u'ул. Пушкина 136577')
        self.driver.find_element_by_xpath("//input[@formcontrolname='work']").send_keys('WORK HARD LIKE VLADIMIR PUTIN!')
        self.driver.find_element_by_xpath("//input[@formcontrolname='passport']").send_keys('123456 1212')
        self.driver.find_element_by_xpath("//input[@formcontrolname='city']").send_keys(u'Санкт-Petersburg')
        self.driver.find_element_by_xpath("//input[@formcontrolname='phone']").send_keys('+799991234678')
        self.driver.find_element_by_xpath("//input[@formcontrolname='income']").send_keys('Hustle&Flow')
        self.driver.find_element_by_xpath("//button[@class='btn btn-round-blue']")


        #logout
        self.driver.find_element_by_xpath("//a[@class='nav-link account-link dropdown-toggle']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//i[@class='mdi mdi-power']").click()
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)



