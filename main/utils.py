from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from main.Constants import Constants


class Utils:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, *identifiers):
        wait = WebDriverWait(self.driver, Constants.TIMEOUT)
        element = wait.until(expected_conditions.element_to_be_clickable((identifiers[0], identifiers[1])))
        return element

    def find_element_by_id_and_click(self, identifier):
        self.wait_for_element_to_be_clickable(By.ID, identifier).click()

    def find_element_by_name_and_click(self, identifier):
        self.wait_for_element_to_be_clickable(By.NAME, identifier).click()

    def find_element_by_class_name_and_click(self, identifier):
        self.wait_for_element_to_be_clickable(By.CLASS_NAME, identifier).click()

    def find_element_by_css_and_click(self, identifier):
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, identifier).click()

    def find_element_by_xpath_and_click(self, identifier):
        self.wait_for_element_to_be_clickable(By.XPATH, identifier).click()

    def find_element_by_link_text_and_click(self, identifier):
        self.wait_for_element_to_be_clickable(By.LINK_TEXT, identifier).click()

    def find_element_by_partial_link_text_and_click(self, identifier):
        self.wait_for_element_to_be_clickable(By.PARTIAL_LINK_TEXT, identifier).click()

    def find_element_by_tag_name_and_click(self, identifier):
        self.wait_for_element_to_be_clickable(By.TAG_NAME, identifier).click()

    def find_element_by_id_and_send_text(self, identifier, text):
        self.wait_for_element_to_be_clickable(By.ID, identifier).send_keys(text)

    def find_element_by_name_and_send_text(self, identifier, text):
        self.wait_for_element_to_be_clickable(By.NAME, identifier).send_keys(text)

    def find_element_by_class_name_and_send_text(self, identifier, text):
        self.wait_for_element_to_be_clickable(By.CLASS_NAME, identifier).send_keys(text)

    def find_element_by_css_and_send_text(self, identifier, text):
        self.wait_for_element_to_be_clickable(By.CSS_SELECTOR, identifier).send_keys(text)

    def find_element_by_xpath_and_send_text(self, identifier, text):
        self.wait_for_element_to_be_clickable(By.XPATH, identifier).send_keys(text)

    def find_element_by_link_text_and_send_text(self, identifier, text):
        self.wait_for_element_to_be_clickable(By.LINK_TEXT, identifier).send_keys(text)

    def find_element_by_partial_link_text_and_send_text(self, identifier, text):
        self.wait_for_element_to_be_clickable(By.PARTIAL_LINK_TEXT, identifier).send_keys(text)

    def find_element_by_tag_name_and_send_text(self, identifier, text):
        self.wait_for_element_to_be_clickable(By.TAG_NAME, identifier).send_keys(text)

    def check_presence_of_element(self, *identifiers):
        wait = WebDriverWait(self.driver, Constants.TIMEOUT)
        element = wait.until(expected_conditions.presence_of_element_located((identifiers[0], identifiers[1])))
        return element

    def move_to_element_and_click(self, *identifiers):
        element = self.check_presence_of_element(identifiers)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def move_to_element_and_hold(self, *identifiers):
        element = self.check_presence_of_element(identifiers)
        ActionChains(self.driver).click_and_hold(element).perform()

    def move_to_element_and_context_click(self, *identifiers):
        element = self.check_presence_of_element(identifiers)
        ActionChains.context_click(element).perform()
