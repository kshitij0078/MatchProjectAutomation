import time

from selenium.webdriver.common.by import By

from langdetect import detect

import enchant


def test_language_change(login):
    driver = login
    time.sleep(10)

    settings_tab = driver.find_element(By.XPATH, '//h6[text()="Settings"]')
    settings_tab.click()
    time.sleep(3)

    list1 = []
    check_language = driver.find_element(By.XPATH, '//h2[text()="Settings"]')
    k = check_language.text
    check_language = driver.find_elements(By.XPATH, '//label[@class="font-weight-600"]')
    for i in check_language:
        list1.append(i.text)
    list1.insert(0, k)
    print("\n", list1)
    n = len(list1) - 1
    for i in range(n):
        d = enchant.Dict("en_US")
        check_language = (d.check(list1[i]))
        if check_language:
            print("Text is in English..")
        else:
            print("Text is not in English..")
    if detect(list1[n]) == "en":
        print("Text is in English...")
    else:
        print("Text is not in English..")

    change_language = driver.find_element(By.XPATH, '(//input[@role="switch"])[2]')
    change_language.click()
    time.sleep(5)

    list1 = []
    check_language = driver.find_element(By.XPATH, '//h2[text()="Einstellungen"]')
    k = check_language.text
    check_language = driver.find_elements(By.XPATH, '//label[@class="font-weight-600"]')
    for i in check_language:
        list1.append(i.text)
    list1.insert(0, k)
    print("\n", list1)
    n = len(list1) - 1
    for i in range(n):
        d = enchant.Dict("en_US")
        check_language = (d.check(list1[i]))
        if check_language:
            print("Text is in English..")
        else:
            print("Text is in Deutsch..")
    if detect(list1[n]) == "en":
        print("Text is in English...")
    else:
        print("Text is in Deutsch..")

    time.sleep(5)

    change_language = driver.find_element(By.XPATH, '(//input[@role="switch"])[1]')
    change_language.click()
    time.sleep(5)

    list1 = []
    check_language = driver.find_element(By.XPATH, '//h2[text()="Settings"]')
    k = check_language.text
    check_language = driver.find_elements(By.XPATH, '//label[@class="font-weight-600"]')
    for i in check_language:
        list1.append(i.text)
    list1.insert(0, k)
    print("\n", list1)
    n = len(list1) - 1
    for i in range(n):
        d = enchant.Dict("en_US")
        check_language = (d.check(list1[i]))
        if check_language:
            print("Text is in English..")
        else:
            print("Text is in Deutsch..")
    if detect(list1[n]) == "en":
        print("Text is in English...")
    else:
        print("Text is in Deutsch..")

    time.sleep(5)
