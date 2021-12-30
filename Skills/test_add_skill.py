import random
import string
import time

from selenium.webdriver.common.by import By
from selenium import webdriver


def test_add_skill(login):
    driver = login

    time.sleep(5)
    skill_tab = driver.find_element(By.XPATH, '//img[@alt="Skills"]')
    skill_tab.click()
    time.sleep(5)
    button_add = driver.find_element(By.XPATH, '//button[text()="Add"]')
    button_add.click()
    time.sleep(5)

    add_skill = driver.find_element(By.XPATH, '//input[@placeholder="Type in your Skill"]')
    add_skill.send_keys("r")
    select_skill = driver.find_element(By.XPATH,
                                       '//div[@class="blazored-typeahead__result blazored-typeahead__active-item"]')
    select_skill.click()
    time.sleep(2)

    skill_level = driver.find_element(By.XPATH, '//div[@class="mdc-select__anchor"]')
    skill_level.click()
    select_skill_level = driver.find_element(By.XPATH, '//span[text()="Level 2"]')
    select_skill_level.click()
    time.sleep(2)
    button_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    button_save.click()

    time.sleep(10)

    button_add = driver.find_element(By.XPATH, '//button[text()="Add"]')
    button_add.click()
    time.sleep(5)

    dummy_skill_length = 10
    random_str = "".join(random.choices(string.ascii_lowercase + string.digits, k=dummy_skill_length))
    add_skill = driver.find_element(By.XPATH, '//input[@placeholder="Type in your Skill"]')
    add_skill.send_keys(str(random_str))

    new_skill = driver.find_element(By.XPATH, '//strong[text()="Add"]')
    new_skill.click()
    time.sleep(5)
