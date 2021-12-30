import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_add_disposition_to_consultant(login):
    driver = login
    time.sleep(10)

    disposition_tab = driver.find_element(By.XPATH, '//h6[text()="Disposition"]')
    disposition_tab.click()
    time.sleep(2)

    disposition_to_project = driver.find_element(By.XPATH, '//h6[text()="Add disposition to Consultant"]')
    disposition_to_project.click()
    time.sleep(2)

    '''
    calling methods...
    '''

    add_position(login)
    edit_position(login)
    delete_position(login)

    name = driver.find_element(By.XPATH, '//input[@type="search"]')
    name.send_keys("test")

    search_button = driver.find_element(By.XPATH, '//i[text()="search"]')
    search_button.click()
    time.sleep(2)

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


def add_position(driver):
    name = driver.find_element(By.XPATH, '//input[@type="search"]')
    name.send_keys("test")

    search_button = driver.find_element(By.XPATH, '//i[text()="search"]')
    search_button.click()
    time.sleep(2)

    consultant_name = driver.find_element(By.XPATH, '//div[text()="Test QA-Internal"]')
    action = ActionChains(driver)
    action.context_click(consultant_name).perform()

    add_position_button = driver.find_element(By.XPATH, '(//li[text()="Add Position"])')
    add_position_button.click()
    time.sleep(30)

    calendar = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[1]')
    calendar.click()
    months = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    months.click()
    select_month = driver.find_element(By.XPATH, '//option[text()="December"]')
    select_month.click()
    time.sleep(2)
    select_from_date = driver.find_element(By.XPATH, '//span[@aria-label="December 1, 2021"]')
    select_from_date.click()
    time.sleep(2)

    calendar = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[2]')
    calendar.click()
    year = driver.find_element(By.XPATH, '//input[@aria-label="Year"]')
    year.clear()
    time.sleep(2)
    year.send_keys("2022")
    months = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    months.click()
    select_month = driver.find_element(By.XPATH, '//option[text()="March"]')
    select_month.click()
    time.sleep(2)
    select_from_date = driver.find_element(By.XPATH, '//span[@aria-label="March 30, 2022"]')
    select_from_date.click()
    time.sleep(2)

    project = driver.find_element(By.XPATH, '//div[@class="blazored-typeahead__input-mask"]')
    project.send_keys("lib")
    select_project = driver.find_element(By.XPATH, '//div[text()="lib40"]')
    select_project.click()
    time.sleep(2)

    job_role = driver.find_element(By.XPATH, '//select[@class="form-control input-select-popup valid"]')
    job_role.click()
    select_job = driver.find_element(By.XPATH, '//option[text()="Mds Migrated"]')
    select_job.click()
    time.sleep(2)

    allocation_type = driver.find_element(By.XPATH, '//select[@id="AllocationType"]')
    allocation_type.click()
    select_allocation = driver.find_element(By.XPATH, '//option[text()="Local Holiday"]')
    select_allocation.click()
    time.sleep(2)

    probability = driver.find_element(By.XPATH, '//select[@id="Probability"]')
    probability.click()
    select_probability = driver.find_element(By.XPATH, '//option[text()="75%"]')
    select_probability.click()
    time.sleep(2)

    workload = driver.find_element(By.XPATH, '(//input[@id="Project"])[1]')
    workload.clear()
    time.sleep(2)
    workload.send_keys("50")
    time.sleep(2)

    allocation_remarks = driver.find_element(By.XPATH, '(//input[@id="Project"])[2]')
    allocation_remarks.send_keys("Local Holiday allocation is commercial work for the project with good workload")
    time.sleep(2)

    save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    save.click()
    time.sleep(5)

    status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(status_msg.text)
    time.sleep(5)

    '''
    Edit position...
    '''


def edit_position(driver):
    name_field = driver.find_element(By.XPATH, '//input[@type="search"]')
    name_field.send_keys("test")

    search_icon = driver.find_element(By.XPATH, '//i[text()="search"]')
    search_icon.click()
    time.sleep(2)

    allocation = driver.find_element(By.XPATH, '(//div[@oncontextmenu="return false"])[3]')
    action = ActionChains(driver)
    action.context_click(allocation).perform()

    list_of_edit_position = driver.find_elements(By.XPATH, '(//li[text()="Edit Position"])')
    length_of_list = len(list_of_edit_position)
    print(length_of_list)
    edit_position_button = list_of_edit_position[length_of_list-1]
    edit_position_button.click()

    '''
    edit_position_button = driver.find_element(By.XPATH, '(//li[text()="Edit Position"])[4]')
    edit_position_button.click()
    time.sleep(5)
     '''

    job_role = driver.find_element(By.XPATH, '//select[@class="form-control input-select-popup valid"]')
    job_role.click()
    select_job = driver.find_element(By.XPATH, '//option[text()="PMO "]')
    select_job.click()
    time.sleep(2)

    workload = driver.find_element(By.XPATH, '(//input[@id="Project"])[1]')
    workload.clear()
    time.sleep(2)
    workload.send_keys("35")
    time.sleep(2)

    allocation_remarks = driver.find_element(By.XPATH, '(//input[@id="Project"])[2]')
    allocation_remarks.clear()
    allocation_remarks.send_keys("Local Holiday allocation is commercial work for the project with good workload.")
    time.sleep(2)

    save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    save.click()
    time.sleep(5)

    update_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(update_status_msg.text)
    time.sleep(5)

    '''
    delete position
    '''


def delete_position(driver):
    name_field = driver.find_element(By.XPATH, '//input[@type="search"]')
    name_field.send_keys("test")

    search_icon = driver.find_element(By.XPATH, '//i[text()="search"]')
    search_icon.click()
    time.sleep(2)

    allocation = driver.find_element(By.XPATH, '(//div[@oncontextmenu="return false"])[2]')
    action = ActionChains(driver)
    action.context_click(allocation).perform()
    time.sleep(2)

    list_of_edit_position = driver.find_elements(By.XPATH, '(//li[text()="Edit Position"])')
    length_0f_list = len(list_of_edit_position)

    edit_position_button = list_of_edit_position[length_0f_list-1]
    edit_position_button.click()
    '''
    edit_position_button = driver.find_element(By.XPATH, '(//li[text()="Edit Position"])[7]')
    edit_position_button.click()
    time.sleep(5)
    '''

    delete = driver.find_element(By.XPATH, '//button[text()="Delete"]')
    delete.click()
    time.sleep(2)

    update_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(update_status_msg.text)
    time.sleep(5)


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
    list2_of_calendar = []
    list_of_calendar = driver.find_elements(By.XPATH, '//div[@class="calendar text-center border"]')

    for i in list_of_calendar:
        list2_of_calendar.append(i.text)
    print(list2_of_calendar)

    action.click_and_hold(on_element=c1).move_to_element(c2).perform()
    c2.click()
    time.sleep(3)
    action.click_and_hold(on_element=c2).move_to_element(c3).perform()
    c3.click()
    time.sleep(3)

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
