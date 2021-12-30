import time

import pytest
from selenium.webdriver.common.by import By


def test_change_profile_picture(login):
    driver = login
    time.sleep(5)

    change_picture = driver.find_element(By.XPATH, '//input[@id="file-input"]')
    change_picture.send_keys("C://MatchAutomation/pictures/6.jpg")
    time.sleep(5)

    upload_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n", upload_status_msg.text)

    time.sleep(10)
