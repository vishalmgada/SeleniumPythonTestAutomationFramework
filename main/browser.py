import selenium
from selenium import webdriver
from pathlib import Path


class Browser:

    def __init__(self, driver, browser_name: str):
        self.driver = driver
        self.browser_name = browser_name

    def initialize_browser(self, url):
        driver_path = str(Path(__file__).parent.parent)
        driver_path = driver_path + r'\drivers'
        try:
            if self.browser_name.lower() == 'chrome':
                driver = webdriver.Chrome(executable_path=driver_path+r"\chromedriver.exe")
            elif self.browser_name.lower() == 'firefox':
                driver = webdriver.Firefox(executable_path=driver_path + r"\geckodriver.exe")
            elif self.browser_name.lower() == "edge":
                driver = webdriver.Edge(executable_path=driver_path + r"\msedgedriver.exe")
            elif self.browser_name.lower() == 'opera':
                driver = webdriver.Opera(executable_path=driver_path + r"\operadriver.exe")
            elif self.browser_name.lower() == 'safari':
                driver = webdriver.Safari(executable_path=driver_path + r"\safaridriver.exe")
            elif self.browser_name.lower() == 'ie':
                driver = webdriver.Ie(executable_path=driver_path + r"\iedriver.exe")
            elif self.browser_name.lower() == 'remote':
                driver = webdriver.Remote(desired_capabilities="", command_executor="")
            else:
                print("Browser name does not match")
                raise TypeError("Browser type did not match")
            driver.get(url)
        except selenium.common.exceptions.WebDriverException:
            raise FileNotFoundError("Browser driver file not available in the given path")
