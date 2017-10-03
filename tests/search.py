# -*- coding: utf-8 -*-
from libs.selenium_helper import SeleniumHelper

class Search():
    def setUp(self):
        self.driver = SeleniumHelper.driver
        self.base_url = SeleniumHelper.base_url

    def test_search_google(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("selenium webdriver python")
        driver.find_element_by_name("btnK").click()
        driver.find_element_by_link_text(u"7. WebDriver API — Selenium Python Bindings 2 documentation").click()
        driver.find_element_by_link_text("1. Installation").click()
        driver.find_element_by_link_text("2. Getting Started").click()
        driver.find_element_by_link_text("3. Navigating").click()

    def tearDown(self):
        self.driver.quit()