import time

from selenium.webdriver.common.by import By


def test_add_qualification(login):
    driver = login
    time.sleep(5)

    tab_qualification = driver.find_element(By.XPATH, '//a[@href="qualification"]')
    tab_qualification.click()
    time.sleep(5)

    button_add = driver.find_element(By.XPATH, '//button[text()="ADD"]')
    button_add.click()
    time.sleep(3)

    issued_from = driver.find_element(By.XPATH, '(//input[@type="checkbox"])[1]')
    issued_from.click()
    time.sleep(2)

    issued_to = driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]')
    issued_to.click()
    time.sleep(5)

    calendar_from = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[1]')
    calendar_from.click()

    months = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    months.click()
    select_month = driver.find_element(By.XPATH, '//option[text()="November"]')
    select_month.click()
    time.sleep(2)

    select_from_date = driver.find_element(By.XPATH, '//span[@aria-label="November 19, 2021"]')
    select_from_date.click()

    calendar_to_date = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[2]')
    calendar_to_date.click()

    click_on_month = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    click_on_month.click()
    select_month = driver.find_element(By.XPATH, '//option[text()="December"]')
    select_month.click()
    select_to_date = driver.find_element(By.XPATH, '//span[@aria-label="December 31, 2021"]')
    select_to_date.click()
    time.sleep(3)

    click_category = driver.find_element_by_id("Category")
    click_category.click()
    select_category = driver.find_element(By.XPATH, '//option[text()="Certificates"]')
    select_category.click()
    time.sleep(2)

    name_field = driver.find_element(By.XPATH, '//input[@class="form-control rounded-0 valid"]')
    name_field.send_keys("Hemanth kumar")
    time.sleep(2)

    upload_attachment = driver.find_element(By.XPATH, '//input[@class="custom-file-input"]')
    upload_attachment.send_keys("C://MatchAutomation/pictures/attachment1.docx")
    time.sleep(2)

    button_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    button_save.click()
    time.sleep(5)

    upload_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(upload_status_msg.text)

    time.sleep(10)

