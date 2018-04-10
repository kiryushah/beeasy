# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest


class ClickToPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 40)


    def test_ClickToPages(self):
        self.driver.get("https://beeasy.io")
        time.sleep(4)


        pages=self.driver.find_elements_by_xpath("//a[@class='page-navigation__link link']")
        for i in pages:
            i.click()
            time.sleep(2)


        #ico
        self.driver.find_element_by_xpath("//a[@href='#ico']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//h2[@class='ico__title']")


        #roadmap
        self.driver.find_element_by_xpath("//a[@href='#roadmap']").click()
        time.sleep(2)
        self.driver.find_elements_by_xpath("//li[@class='roadmap__stage']")


        #team
        self.driver.find_element_by_xpath("//a[@href='#team']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//h2[@class='team__title subtitle']")
        self.driver.find_element_by_xpath("//div[@class='team-card__header']").click()
        time.sleep(2)

        #Media and events
        self.driver.find_element_by_xpath("//a[@href='#about']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@id='slick-slide-control01']").click()


        #Contacts
        self.driver.find_element_by_xpath("//a[@href='#contacts']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//h2[@class='contacts__title subtitle']")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



