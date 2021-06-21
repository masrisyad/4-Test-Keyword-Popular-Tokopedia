# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Testkeywordpopulartokopedia():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testkeywordpopulartokopedia(self):
        # Test name: test-keyword-popular-tokopedia
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://www.tokopedia.com/")
        # 2 | setWindowSize | 1382x744 |
        self.driver.set_window_size(1382, 744)
        # 3 | mouseOver | css=#trending-popular-keywords > a:nth-child(4) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, "#trending-popular-keywords > a:nth-child(4)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 4 | mouseOver | css=#trending-popular-keywords > a:nth-child(1) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, "#trending-popular-keywords > a:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 5 | click | css=#trending-popular-keywords > a:nth-child(1) |
        self.driver.find_element(
            By.CSS_SELECTOR, "#trending-popular-keywords > a:nth-child(1)").click()
        # 6 | click | css=#trending-popular-keywords > a:nth-child(2) |
        self.driver.find_element(
            By.CSS_SELECTOR, "#trending-popular-keywords > a:nth-child(2)").click()
        # 7 | click | css=#trending-popular-keywords > a:nth-child(3) |
        self.driver.find_element(
            By.CSS_SELECTOR, "#trending-popular-keywords > a:nth-child(3)").click()
        # 8 | click | css=#trending-popular-keywords > a:nth-child(4) |
        self.driver.find_element(
            By.CSS_SELECTOR, "#trending-popular-keywords > a:nth-child(4)").click()
