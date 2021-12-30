import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_selecting_project(login):
    driver = login
    time.sleep(5)

    disposition_tab = driver.find_element(By.XPATH, '//h6[text()="Disposition"]')
    disposition_tab.click()
    time.sleep(2)

    disposition_to_project = driver.find_element(By.XPATH, '//h6[text()="Add disposition to Project"]')
    disposition_to_project.click()
    time.sleep(2)

    select_project = driver.find_element(By.XPATH, '(//i[text()="create"])[3]')
    select_project.click()
    time.sleep(2)

    to_date = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[2]')
    to_date.click()
    year = driver.find_element(By.XPATH, '//input[@aria-label="Year"]')
    year.clear()
    select_year = driver.find_element(By.XPATH, '//input[@aria-label="Year"]')
    select_year.send_keys("2022")
    time.sleep(2)
    months_dropdown = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    months_dropdown.click()
    select_month = driver.find_element(By.XPATH, '//option[text()="March"]')
    select_month.click()
    select_to_date = driver.find_element(By.XPATH, '//span[@aria-label="March 30, 2022"]')
    select_to_date.click()
    time.sleep(3)

    billable = driver.find_element(By.XPATH, '(//input[@class="valid"])[1]')
    billable.click()
    time.sleep(3)

    external = driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]')
    external.click()
    time.sleep(2)

    maintainer_name = driver.find_element(By.XPATH, '(//div[@class="blazored-typeahead__input-mask"])[1]')
    maintainer_name.send_keys("a")
    time.sleep(2)
    select_maintainer_name = driver.find_element(By.XPATH, '(//div[@class="blazored-typeahead__result "])[2]')
    select_maintainer_name.click()
    time.sleep(10)

    city = driver.find_element(By.XPATH, '(//div[@class="blazored-typeahead__input-mask"])[2]')
    city.send_keys("o")
    time.sleep(2)
    select_city = driver.find_element(By.XPATH, '//div[text()="Ober-Olm"]')
    select_city.click()
    time.sleep(2)

    click_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    click_save.click()
    time.sleep(3)

    status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(status_msg.text)
    time.sleep(10)

    '''
    add position...
    '''

    element = driver.find_element(By.XPATH, '//div[@class="row flex-container justify-content-end mb-3"]')

    actions = ActionChains(driver)

    actions.move_to_element(element).perform()

    add_position = driver.find_element(By.XPATH, '//div[text()="Add Position"]')
    add_position.click()
    time.sleep(3)

    role_dropdown = driver.find_element(By.XPATH, '(//select[@class="form-control input-select-popup valid"])[1]')
    role_dropdown.click()
    select_role = driver.find_element(By.XPATH, '//option[text()="Mds Migrated"]')
    select_role.click()
    time.sleep(2)

    name_field = driver.find_element(By.XPATH, '//input[@class="blazored-typeahead__input "]')
    name_field.send_keys("test")
    time.sleep(2)
    select_name = driver.find_element(By.XPATH, '//div[text()="Test QA-Internal"]')
    select_name.click()
    time.sleep(2)

    from_date = driver.find_element(By.XPATH, '(//input[@placeholder="DD.MM.YYYY"])[1]')
    from_date.send_keys("29.09.2021")

    to_date = driver.find_element(By.XPATH, '(//input[@placeholder="DD.MM.YYYY"])[2]')
    to_date.send_keys("29.12.2021")
    time.sleep(2)

    driver.find_element(By.XPATH, '//div[text()="To Date"]').click()

    workload = driver.find_element(By.XPATH, '(//input[@class="form-control input-select-popup pd-input-3 valid"])')
    workload.clear()
    random_workload = random.randint(1, 10)
    random_workload = random_workload * 10
    workload.send_keys(random_workload)
    time.sleep(2)

    allocation_type = driver.find_element(By.XPATH, '//select[@class="form-control input-select-popup valid"]')
    allocation_type.click()
    select_allocation = driver.find_element(By.XPATH, '//option[text()="F+E"]')
    select_allocation.click()
    time.sleep(2)

    allocation_remark = driver.find_element(By.XPATH, '//input[@class="form-control input-select-popup pd-input-3"]')
    allocation_remark.send_keys("F+E allocation is commercial work for the project with good workload.")

    probability = driver.find_element(By.XPATH, '//select[@class="form-control input-select-popup pd-input-3 valid"]')
    probability.click()
    select_probability = driver.find_element(By.XPATH, '//option[@value="90%"]')
    select_probability.click()
    time.sleep(2)

    save_button = driver.find_element(By.XPATH, '//i[text()="save"]')
    save_button.click()
    time.sleep(5)

    '''
    edit position...
    '''

    edit_add_position = driver.find_element(By.XPATH, '(//i[text()="create"])[6]')
    edit_add_position.click()
    time.sleep(2)

    role_dropdown = driver.find_element(By.XPATH, '(//select[@class="form-control input-select-popup valid"])[1]')
    role_dropdown.click()
    select_role = driver.find_element(By.XPATH, '//option[text()="Projektleiter"]')
    select_role.click()
    time.sleep(2)

    workload_field = driver.find_element(By.XPATH, '(//input[@class="form-control input-select-popup pd-input-3 '
                                                   'valid"])[3]')
    workload_field.clear()
    time.sleep(2)
    workload_field.send_keys("30")

    allocation = driver.find_element(By.XPATH, '//select[@class="form-control input-select-popup valid"]')
    allocation.click()
    select_allocation_type = driver.find_element(By.XPATH, '//option[text()="Management"]')
    select_allocation_type.click()
    time.sleep(2)

    probability_field = driver.find_element(By.XPATH, '//select[@class="form-control input-select-popup pd-input-3 '
                                                      'valid"]')
    probability_field.click()
    select_probability_field = driver.find_element(By.XPATH, '//option[@value="90%"]')
    select_probability_field.click()
    time.sleep(2)

    save_button = driver.find_element(By.XPATH, '//i[text()="save"]')
    save_button.click()
    time.sleep(5)

    '''
    delete position..
    '''

    delete_button = driver.find_element(By.XPATH, '(//i[text()="delete"])[6]')
    delete_button.click()
    time.sleep(10)






