# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
import random

class SignUp(unittest.TestCase):

    def setUp(self):
        display = Display(backend='xvnc', visible=True, rfbport=5900, size=(1440, 900))
        display.start()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
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
    unittest.main()



