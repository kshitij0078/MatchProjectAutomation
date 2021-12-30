import random
import time

from selenium.webdriver.common.by import By


def test_add_project(login):
    driver = login
    time.sleep(5)

    disposition_tab = driver.find_element(By.XPATH, '//h6[text()="Disposition"]')
    disposition_tab.click()
    time.sleep(2)

    add_project_button = driver.find_element(By.XPATH, '//h6[text()="Add Project"]')
    add_project_button.click()
    time.sleep(10)

    from_date = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[1]')
    from_date.click()
    months_dropdown = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    months_dropdown.click()
    select_month = driver.find_element(By.XPATH, '//option[text()="September"]')
    select_month.click()
    select_from_date = driver.find_element(By.XPATH, '//span[@aria-label="September 28, 2021"]')
    select_from_date.click()
    time.sleep(3)

    to_date = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[2]')
    to_date.click()
    months_dropdown = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    months_dropdown.click()
    select_month = driver.find_element(By.XPATH, '//option[text()="December"]')
    select_month.click()
    select_to_date = driver.find_element(By.XPATH, '//span[@aria-label="December 30, 2021"]')
    select_to_date.click()
    time.sleep(3)

    project_title = driver.find_element(By.XPATH, '(//input[@class="form-control rounded-0 border-dark valid"])[1]')
    random_number = random.randint(0, 100)
    project_title.send_keys("lib" + str(random_number))
    time.sleep(3)

    project_number = driver.find_element(By.XPATH, '(//input[@class="form-control rounded-0 border-dark valid"])[2]')
    random_number = random.randint(0,1000)
    project_number.send_keys(random_number)
    time.sleep(3)

    customer = driver.find_element(By.XPATH, '(//input[@class="form-control rounded-0 border-dark valid"])[2]')
    customer.send_keys("Frank")
    time.sleep(2)

    organization_unit = driver.find_element(By.XPATH, '(//select[@class="form-control rounded-0 border-dark valid"])[1]')
    organization_unit.click()
    time.sleep(2)

    select_organization = driver.find_element(By.XPATH, '//option[text()="Banking - Services"]')
    select_organization.click()
    time.sleep(2)

    billable = driver.find_element(By.XPATH, '(//input[@class="valid"])[1]')
    billable.click()
    time.sleep(3)

    external = driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]')
    external.click()
    time.sleep(2)

    maintainer_name = driver.find_element(By.XPATH, '(//input[@class="blazored-typeahead__input "])[1]')
    maintainer_name.send_keys("a")
    time.sleep(2)
    select_maintainer_name = driver.find_element(By.XPATH, '//div[text()="Abdullah Zanaty"]')
    select_maintainer_name.click()
    time.sleep(2)

    project_description = driver.find_element(By.XPATH, '//textarea[@class="valid"]')
    project_description.send_keys("This application is useful for managing and viewing Consultant’s profile with "
                                  "details like their skills, project, CV, etc. Also, this application is useful for "
                                  "Managers to quickly identify their team or other consultants using the search "
                                  "feature, manage the allocation of their team members and the projects they are "
                                  "involved in")
    time.sleep(2)

    project_type = driver.find_element(By.XPATH, '//select[@class="form-control rounded-0 border-dark valid"]')
    project_type.click()
    select_project_type = driver.find_element(By.XPATH, '//option[text()="Internal Project"]')
    select_project_type.click()
    time.sleep(2)

    city = driver.find_element(By.XPATH, '(//input[@type="text"])[6]')
    city.send_keys("o")
    time.sleep(2)
    select_city = driver.find_element(By.XPATH, '//div[text()="Ober-Olm"]')
    select_city.click()
    time.sleep(2)

    consultant_name = driver.find_element(By.XPATH, '(//input[@type="text"])[7]')
    consultant_name.send_keys("ca")
    time.sleep(2)
    select_consultant_name = driver.find_element(By.XPATH, '//div[text()="Carina Rose"]')
    select_consultant_name.click()
    time.sleep(3)

    responsible_name = driver.find_element(By.XPATH, '(//input[@type="text"])[8]')
    responsible_name.send_keys("hem")
    time.sleep(2)
    select_responsible_name = driver.find_element(By.XPATH, '//div[text()="Hemanth Gaddam"]')
    select_responsible_name.click()
    time.sleep(2)

    click_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    click_save.click()
    time.sleep(3)

    status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
    print("\n")
    print(status_msg.text)
    time.sleep(10)

    '''
    add position..
    '''

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
    edit_add_position..
    '''

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
    delete position...
    '''

    delete_button = driver.find_element(By.XPATH, '(//i[text()="delete"])[1]')
    delete_button.click()
    time.sleep(10)








