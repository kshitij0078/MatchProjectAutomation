import time

from selenium.webdriver.common.by import By


def test_edit_qualification(login):
    driver = login
    time.sleep(5)

    tab_qualification = driver.find_element(By.XPATH, '//a[@href="qualification"]')
    tab_qualification.click()
    time.sleep(5)

    button_more = driver.find_element(By.XPATH, '(//button[@aria-label="more_vert"])[2]')
    button_more.click()
    time.sleep(2)

    click_edit = driver.find_element(By.XPATH, '(//a[text()="Edit"])[2]')
    click_edit.click()
    time.sleep(2)

    issue_from = driver.find_element(By.XPATH, '(//input[@class="mat-text-field-input mdc-text-field__input"])[2]')

    issue_from.clear()
    time.sleep(3)

    edit_category = driver.find_element_by_id("Category")
    edit_category.click()
    select_category = driver.find_element(By.XPATH, '//option[text()="Certificates"]')
    select_category.click()
    time.sleep(2)

    name_field = driver.find_element(By.XPATH, '//input[@class="form-control rounded-0 valid"]')
    name_field.clear()
    name_field.send_keys("GaddamHemanth")
    time.sleep(2)

    upload_attachment = driver.find_element(By.XPATH, '//input[@class="custom-file-input"]')
    upload_attachment.send_keys("C://MatchAutomation/pictures/attachment2.docx")
    time.sleep(2)

    button_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    button_save.click()
    time.sleep(2)
    button_save.click()

    time.sleep(5)

    updated_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")

    print(updated_status_msg.text)

    time.sleep(10)

    delete_qualification(login)
    '''
        Delete the Qualification.....
        '''


def delete_qualification(driver):
    button_more = driver.find_element(By.XPATH, '(//button[@aria-label="more_vert"])[2]')
    button_more.click()
    time.sleep(2)

    click_delete = driver.find_element(By.XPATH, '(//a[text()="Delete Qualification"])[2]')
    click_delete.click()
    time.sleep(3)

    button_delete = driver.find_element(By.XPATH, '(//button[text()="Delete"])[2]')
    button_delete.click()
    time.sleep(3)

    delete_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")

    print(delete_status_msg.text)

    time.sleep(10)
