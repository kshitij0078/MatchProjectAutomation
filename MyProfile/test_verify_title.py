import time

import pytest
from selenium.webdriver.common.by import By


def test_verify_titles(login):
    driver = login
    time.sleep(5)

    header = driver.title
    print("\n", header)
    print(header == "Match")

    user_name = driver.find_element_by_tag_name('h2')
    print(user_name.text)
    time.sleep(5)

    empty_text = driver.find_element(By.XPATH, '(//input[@type="text"])[7]')
    string_value = empty_text.get_attribute('value')

    list_value = driver.find_elements(By.XPATH, '//input[@class="form-control"]')

    for i in list_value:
        if i.get_attribute("value") == string_value:
            print("False")
        else:
            print(i.get_attribute("value"))

    time.sleep(10)
