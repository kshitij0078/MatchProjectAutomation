import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_add_disposition_to_project(login):
    driver = login
    time.sleep(5)

    disposition_tab = driver.find_element(By.XPATH, '//h6[text()="Disposition"]')
    disposition_tab.click()
    time.sleep(2)

    disposition_to_project = driver.find_element(By.XPATH, '//h6[text()="Add disposition to Project"]')
    disposition_to_project.click()
    time.sleep(2)

    '''
    calling methods
    '''

    search_and_edit_project(login)
    add_position(login)
    edit_position(login)

    '''
    operation on days, weeks, months, years..
    '''

    day = driver.find_element(By.XPATH, '//button[text()="Day"]')
    day.click()
    time.sleep(2)
    operation_on_drag_element(login)

    weeks = driver.find_element(By.XPATH, '//button[text()="Weeks"]')
    weeks.click()
    time.sleep(2)
    operation_on_drag_element(login)

    calendar_weeks = driver.find_element(By.XPATH, '//button[text()="Calender Week"]')
    calendar_weeks.click()
    time.sleep(2)
    operation_on_drag_element(login)

    months = driver.find_element(By.XPATH, '//button[text()="Months"]')
    months.click()
    time.sleep(2)
    operation_on_drag_element(login)

    Year = driver.find_element(By.XPATH, '//button[text()="Year"]')
    Year.click()
    time.sleep(2)
    operation_on_drag_element(login)

    '''
     calling delete method..
    '''
    delete_position(login)

    '''
    search_and_edit project..
    '''


def search_and_edit_project(driver):
    search_project = driver.find_element(By.XPATH, '//input[@placeholder="Search Projects..."]')
    search_project.send_keys("lib")
    search_button = driver.find_element(By.XPATH, '//i[text()="search"]')
    search_button.click()
    time.sleep(2)

    edit_button = driver.find_element(By.XPATH, '(//i[text()="create"])[3]')
    edit_button.click()
    time.sleep(5)

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

    maintainer_name = driver.find_element(By.XPATH, '(//div[@class="blazored-typeahead__input-mask"])[1]')
    maintainer_name.send_keys("a")
    select_name = driver.find_element(By.XPATH, '//div[text()="Abdullah Zanaty"]')
    select_name.click()
    time.sleep(2)

    project_description = driver.find_element(By.XPATH, '//textarea[@class="valid"]')
    project_description.clear()
    project_description.send_keys("This application is useful for managing and viewing Consultant’s profile with "
                                  "details like their skills, project, CV, etc. Also, this application is useful for "
                                  "Managers to quickly identify their team or other consultants using the search "
                                  "feature, manage the allocation of their team members and the projects they are "
                                  "involved in")
    time.sleep(2)

    save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
    save_button.click()
    time.sleep(3)
    save_button.click()
    time.sleep(5)

    update_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(update_status_msg.text)
    time.sleep(5)

    '''
    ADD POSITION
    '''


def add_position(driver):
    add_position_button = driver.find_element(By.XPATH, '//div[text()="Add Position"]')
    add_position_button.click()
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
    to_date.send_keys("29.03.2022")
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
    select_allocation = driver.find_element(By.XPATH, '//option[text()="Meeting"]')
    select_allocation.click()
    time.sleep(2)

    allocation_remark = driver.find_element(By.XPATH, '//input[@class="form-control input-select-popup pd-input-3"]')
    allocation_remark.send_keys("Meeting allocation is daily update by team for the project with good workload")

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


def edit_position(driver):
    edit_add_position = driver.find_element(By.XPATH, '//i[text()="create"]')
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


def delete_position(driver):
    delete_button = driver.find_element(By.XPATH, '(//i[text()="delete"])[1]')
    delete_button.click()
    time.sleep(10)


def operation_on_drag_element(driver):
    c1 = driver.find_element(By.XPATH, '//div[@class="mdc-slider__focus-ring"]')
    c2 = driver.find_element(By.XPATH, '//div[@data-step="1"]')
    a1 = driver.find_element(By.XPATH, '//img[@alt="slider-left"]')
    c3 = driver.find_element(By.XPATH, '//img[@alt="slider-right"]')

    action = ActionChains(driver)
    action.click_and_hold(on_element=c1).move_to_element(a1).perform()
    a1.click()
    time.sleep(5)

    print("\n")
    list2 = []
    list1 = driver.find_elements(By.XPATH, '//div[@class="calendar text-center border"]')

    for i in list1:
        list2.append(i.text)
    print(list2)

    action.click_and_hold(on_element=c1).move_to_element(c2).perform()
    c2.click()
    time.sleep(3)
    action.click_and_hold(on_element=c2).move_to_element(c3).perform()
    c3.click()
    time.sleep(2)

    today = driver.find_element(By.XPATH, '//button[text()="Today"]')
    today.click()
    time.sleep(3)

    today_arrow = driver.find_element(By.XPATH, '//i[text()="keyboard_arrow_left"]')
    today_arrow.click()
    time.sleep(2)
    today_arrow.click()
    time.sleep(3)

    today_arrow = driver.find_element(By.XPATH, '//i[text()="keyboard_arrow_right"]')
    today_arrow.click()
    time.sleep(2)
    today_arrow.click()
    time.sleep(3)
