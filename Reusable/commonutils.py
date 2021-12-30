import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def launchbrowser():
    global driver
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    driver.maximize_window()
    driver.set_page_load_timeout(10)
    # driver.close()

