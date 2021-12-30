import time

from selenium.webdriver.common.by import By


def test_download_attachment(login):
    driver = login

    time.sleep(5)

    tab_qualification = driver.find_element(By.XPATH, '//a[@href="qualification"]')
    tab_qualification.click()
    time.sleep(5)

    '''
       Download the attachment.....
       '''
    click_attach = driver.find_element(By.XPATH, '(//button[@aria-label="attach_file"])[1]')
    click_attach.click()
    time.sleep(2)

    click_download = driver.find_element(By.XPATH, '(//a[text()="Download"])[1]')
    click_download.click()
    time.sleep(2)

    delete_attachment(login)

    '''
        Delete the attachment.....
        '''


def delete_attachment(driver):
    click_attach = driver.find_element(By.XPATH, '(//button[@aria-label="attach_file"])[2]')
    click_attach.click()
    time.sleep(2)

    click_delete_attach = driver.find_element(By.XPATH, '(//a[text()="Delete"])[2]')
    click_delete_attach.click()
    time.sleep(3)

    button_delete = driver.find_element(By.XPATH, '(//button[text()="Delete"])[1]')
    button_delete.click()

    time.sleep(5)

    upload_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")

    print(upload_status_msg.text)

    time.sleep(10)
