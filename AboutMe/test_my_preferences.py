import time

from selenium.webdriver.common.by import By


def test_edit_preferences(login):
    driver = login
    driver.find_element(By.XPATH, '//img[@alt="About Me"]').click()
    time.sleep(5)

    button_edit = driver.find_element(By.XPATH, '//button[text()="Edit"]')
    button_edit.click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//textarea[1]').clear()
    time.sleep(3)
    preferences = driver.find_element(By.XPATH, '//textarea[1]')
    preferences.send_keys("I am quite good in java programming language and mathematics.")

    time.sleep(5)
    driver.find_element(By.XPATH, '//textarea[2]').clear()
    time.sleep(5)
    summary = driver.find_element(By.XPATH, '//textarea[2]')
    summary.send_keys("I am from Andhra Pradesh. I did my graduation in CSE from Anna University.")

    button_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    button_save.click()

    time.sleep(10)

    button_edit = driver.find_element(By.XPATH, '//button[text()="Edit"]')
    button_edit.click()
    time.sleep(3)

    preferences = driver.find_element(By.XPATH, '//textarea[1]')
    preferences.send_keys("I am quite good in java programming language and mathematics.")
    time.sleep(3)
    summary = driver.find_element(By.XPATH, '//textarea[2]')
    summary.send_keys("I am from Ongole. I did my graduation in CSE from Anna University.")
    time.sleep(3)

    button_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    button_save.click()
    time.sleep(5)

    updating_preferences = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n", updating_preferences.text)

    time.sleep(10)
