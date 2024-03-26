from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote import switch_to
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from conftest import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def scrool_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def input_text_to_element(self, locator, text):
        self.find_element_and_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_and_wait(locator).text

    def format_locator(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    def switch_to_page(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.find_element_and_wait(locator)
        redirected_url = self.driver.current_url
        return redirected_url
