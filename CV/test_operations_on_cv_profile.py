import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_operations_on_cv_profile(login):
    driver = login
    time.sleep(5)

    cv_tab = driver.find_element(By.XPATH, '//h6[text()="CV"]')
    cv_tab.click()
    time.sleep(5)

    duplicate_cv_profile(login)
    delete_cv_profile(login)
    save_cv_profile(login)
    edit_cv_profile(login)
    send_cv_profile(login)


def edit_cv_profile(driver):
    refresh = driver.find_element(By.XPATH, '//img[@class="ref-icon"]')
    refresh.click()
    time.sleep(10)

    more_button = driver.find_element(By.XPATH, '//button[@aria-label="more_vert"]')
    more_button.click()
    time.sleep(2)

    edit_button = driver.find_element(By.XPATH, '(//li[text()="Edit"])[3]')
    edit_button.click()
    time.sleep(2)

    edit_cv_name = driver.find_element(By.XPATH, '//input[@placeholder="CV Name"]')
    edit_cv_name.clear()
    time.sleep(2)

    cv_name = driver.find_element(By.XPATH, '//input[@placeholder="CV Name"]')
    cv_name.send_keys("Hemanth")
    time.sleep(2)

    save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
    save_button.click()
    time.sleep(3)
    save_button.click()
    time.sleep(5)

    edit_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(edit_status_msg.text)
    time.sleep(10)

    more = driver.find_element(By.XPATH, '//button[@aria-label="more_vert"]')
    more.click()
    time.sleep(2)

    edit_button = driver.find_element(By.XPATH, '(//li[text()="Edit"])[4]')
    edit_button.click()
    time.sleep(2)

    cv_name = driver.find_element(By.XPATH, '//input[@placeholder="CV Name"]')
    cv_name.send_keys(" Gaddam")
    time.sleep(2)

    save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
    save_button.click()
    time.sleep(5)

    edit_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(edit_status_msg.text)
    time.sleep(10)


def duplicate_cv_profile(driver):
    profile_name = driver.find_element(By.XPATH, '(//span[@data-placement="top"])[1]').text

    more = driver.find_element(By.XPATH, '//button[@aria-label="more_vert"]')
    more.click()
    time.sleep(5)

    string = profile_name[0:8]

    if string == "Copy Of ":
        duplicate_button = driver.find_element(By.XPATH, '//li[text()="Duplicate"]')
        duplicate_button.click()
        time.sleep(5)

        profile_name_after_duplicate = driver.find_element(By.XPATH, '(//span[@data-placement="top"])[1]').text

        if profile_name_after_duplicate == "Copy Of - " + profile_name:
            print("duplicate profile is created..")
        else:
            print("duplicate not created..")
    else:
        duplicate_button = driver.find_element(By.XPATH, '//li[text()="Duplicate"]')
        duplicate_button.click()
        time.sleep(5)

        profile_name_after_duplicate = driver.find_element(By.XPATH, '(//span[@data-placement="top"])[1]').text

        if profile_name_after_duplicate == "Copy Of - " + profile_name:
            print("duplicate profile is created..")
        else:
            print("duplicate not created..")


def delete_cv_profile(driver):
    more = driver.find_element(By.XPATH, '//button[@aria-label="more_vert"]')
    more.click()
    time.sleep(5)

    delete = driver.find_element(By.XPATH, '//li[text()="Delete"]')
    delete.click()
    time.sleep(2)

    button_delete = driver.find_element(By.XPATH, '//button[text()="Delete"]')
    button_delete.click()
    time.sleep(10)


def save_cv_profile(driver):
    more = driver.find_element(By.XPATH, '//button[@aria-label="more_vert"]')
    more.click()
    time.sleep(2)

    save = driver.find_element(By.XPATH, '//li[text()="Save"]')
    save.click()
    time.sleep(5)

    format_dropdown = driver.find_element(By.XPATH, '//select[@id="Format"]')
    format_dropdown.click()
    choose_format = driver.find_element(By.XPATH, '//option[@value="PDF"]')
    choose_format.click()
    time.sleep(2)

    language_dropdown = driver.find_element(By.XPATH, '//select[@id="Language"]')
    language_dropdown.click()
    choose_language = driver.find_element(By.XPATH, '//option[@value="English"]')
    choose_language.click()
    time.sleep(2)

    save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
    save_button.click()

    time.sleep(15)


def send_cv_profile(driver):
    more = driver.find_element(By.XPATH, '//button[@aria-label="more_vert"]')
    more.click()
    time.sleep(2)

    #  send = driver.find_element(By.XPATH, '//li[@data-target="#sendCV"]')
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "(//li[@data-target='#sendCV'])[5]")))
    print(element.is_displayed())
    element.click()
    time.sleep(5)

    ok_button = driver.find_element(By.XPATH, '//button[text()="OK"]')
    ok_button.click()
    time.sleep(5)
