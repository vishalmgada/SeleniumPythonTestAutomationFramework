from selenium import webdriver


class CookieUtils(object):

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_browser_cookies(self):
        return self.driver.get_cookies()

    def get_browser_cookie(self, cookie):
        return self.driver.get_cookie(cookie)

    def set_browser_cookie(self, cookie: dict):
        self.driver.add_cookie(cookie)

    def set_browser_cookie(self, cookies: dict):
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def delete_browser_cookie(self, cookie):
        self.driver.delete_cookie(cookie)

    def delete_browser_cookies(self):
        self.driver.delete_all_cookies()
