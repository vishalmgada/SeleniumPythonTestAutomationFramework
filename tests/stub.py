import main.browser
from selenium import webdriver


#
# driver = webdriver
# brow = main.browser.Browser(driver, "firefox")
# brow.initialize_browser("https://www.google.com")

def testing(*args):
    print(args[0])
    print(args[1])


testing(1, 2)
