import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_operation_on_CV(login):
    driver = login
    time.sleep(5)

    click_cv = driver.find_element(By.XPATH, '//h6[text()="CV"]')
    click_cv.click()
    time.sleep(5)

    element = []
    element = driver.find_elements(By.XPATH, '//div[@class="flex d-flex"]')

    if len(element) == 0:

        from_calender = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[1]')
        from_calender.click()
        time.sleep(2)

        months_dropdown = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
        months_dropdown.click()
        time.sleep(2)
        select_from_month = driver.find_element(By.XPATH, '//option[text()="September"]')
        select_from_month.click()
        select_from_date = driver.find_element(By.XPATH, '//span[@aria-label="September 29, 2021"]')
        select_from_date.click()
        time.sleep(3)

        from_calender = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[2]')
        from_calender.click()
        time.sleep(2)

        months_dropdown = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
        months_dropdown.click()
        time.sleep(2)
        select_due_month = driver.find_element(By.XPATH, '//option[text()="December"]')
        select_due_month.click()
        select_due_date = driver.find_element(By.XPATH, '//span[@aria-label="December 30, 2021"]')
        select_due_date.click()
        time.sleep(3)

        sector_dropdown = driver.find_element(By.XPATH, '//select[@class="form-control valid"]')
        sector_dropdown.click()
        select_sector = driver.find_element(By.XPATH, '//option[text()="Public"]')
        select_sector.click()
        time.sleep(3)

        customer_location = driver.find_element(By.XPATH, '//input[@placeholder="e.g. Deutsche Bank not DeuBa"]')
        customer_location.send_keys("Germany")
        time.sleep(2)

        project_name = driver.find_element(By.XPATH, '(//input[@class="form-control valid"])[2]')
        project_name.send_keys("Sosmart")
        time.sleep(2)

        project_description = driver.find_element(By.XPATH, '//div[@class="ql-editor ql-blank"]')
        project_description.send_keys("This application is useful for managing and viewing Consultant’s profile with "
                                      "details like their skills, project, CV, etc. Also, this application is useful "
                                      "for Managers to quickly identify their team or other consultants using the "
                                      "search feature, manage the allocation of their team members and the projects "
                                      "they are involved in. ")

        short_description = driver.find_element(By.XPATH, '//textarea[@class="textarea"]')
        short_description.send_keys("The Match Windows App is built as a project staffing management and scheduling "
                                    "solution, to cater to needs of managers to have a central place for resource "
                                    "searching as well as reporting.")

        time.sleep(3)

        skill_search = driver.find_element(By.XPATH, '//input[@placeholder="Type in your Skill"]')
        skill_search.send_keys("java")
        time.sleep(5)
        select_skill = driver.find_element(By.XPATH, '(//div[@class="blazored-typeahead__result "])[1]')
        select_skill.click()
        time.sleep(2)

        level_dropdown = driver.find_element(By.XPATH, '//div[@class="mdc-select__anchor"]')
        level_dropdown.click()
        time.sleep(2)
        select_skill_level = driver.find_element(By.XPATH, '//span[text()="Level 4"]')
        select_skill_level.click()
        time.sleep(5)

        add_icon = driver.find_element(By.XPATH, '//button[@aria-label="add"]')
        add_icon.click()
        time.sleep(3)

        save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
        save_button.click()
        time.sleep(10)

        new_cv(login)
        edit_cv(login)
        copy_cv(login)
        delete_cv(login)

    else:
        # print("hello")
        new_cv(login)
        edit_cv(login)
        copy_cv(login)
        delete_cv(login)


def edit_cv(driver):
    element = driver.find_element(By.XPATH, '//div[text()="Edit"]')

    actions = ActionChains(driver)

    actions.move_to_element(element).perform()

    edit_button = driver.find_element(By.XPATH, '//div[text()="Edit"]')
    edit_button.click()
    time.sleep(3)

    due_date = driver.find_element(By.XPATH, '(//input[@type="text"])[2]')
    due_date.clear()
    time.sleep(3)

    sector_dropdown = driver.find_element(By.XPATH, '//select[@class="form-control valid"]')
    sector_dropdown.click()
    select_sector = driver.find_element(By.XPATH, '//option[text()="Banking"]')
    select_sector.click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//div[@class="blazored-typeahead__input-mask"]').click()
    time.sleep(3)

    skill_search = driver.find_element(By.XPATH, '//input[@placeholder="Type in your Skill"]')
    skill_search.send_keys("f")
    time.sleep(5)
    select_skill = driver.find_element(By.XPATH, '(//div[@class="blazored-typeahead__result "])[3]')
    select_skill.click()
    time.sleep(2)

    level_dropdown = driver.find_element(By.XPATH, '//div[@class="mdc-select__anchor"]')
    level_dropdown.click()
    time.sleep(2)
    select_skill_level = driver.find_element(By.XPATH, '//span[text()="Level 2"]')
    select_skill_level.click()
    time.sleep(5)

    add_button = driver.find_element(By.XPATH, '//button[@aria-label="add"]')
    add_button.click()
    time.sleep(3)

    save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
    save_button.click()
    time.sleep(10)


'''
Add new cv
'''


def new_cv(driver):
    new_button = driver.find_element(By.XPATH, '//div[text()="New"]')
    new_button.click()
    time.sleep(3)

    from_calender = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[1]')
    from_calender.click()
    time.sleep(2)

    months_dropdown = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    months_dropdown.click()
    time.sleep(2)
    select_from_month = driver.find_element(By.XPATH, '//option[text()="September"]')
    select_from_month.click()
    select_from_date = driver.find_element(By.XPATH, '//span[@aria-label="September 29, 2021"]')
    select_from_date.click()
    time.sleep(3)

    from_calender = driver.find_element(By.XPATH, '(//i[text()="calendar_today"])[2]')
    from_calender.click()
    time.sleep(2)

    months_dropdown = driver.find_element(By.XPATH, '//select[@class="flatpickr-monthDropdown-months"]')
    months_dropdown.click()
    time.sleep(2)
    select_due_month = driver.find_element(By.XPATH, '//option[text()="December"]')
    select_due_month.click()
    select_due_date = driver.find_element(By.XPATH, '//span[@aria-label="December 30, 2021"]')
    select_due_date.click()
    time.sleep(3)

    sector_dropdown = driver.find_element(By.XPATH, '//select[@class="form-control valid"]')
    sector_dropdown.click()
    select_sector = driver.find_element(By.XPATH, '//option[text()="Telekom"]')
    select_sector.click()
    time.sleep(3)

    customer_location = driver.find_element(By.XPATH, '//input[@placeholder="e.g. Deutsche Bank not DeuBa"]')
    customer_location.send_keys("Canada")
    time.sleep(2)

    project_name = driver.find_element(By.XPATH, '(//input[@class="form-control valid"])[2]')
    project_name.send_keys("Survival outcome prediction for cancer patients")
    time.sleep(2)

    project_description = driver.find_element(By.XPATH, '//div[@class="ql-editor ql-blank"]')
    project_description.send_keys("This application is useful for managing and viewing Consultant’s profile with "
                                  "details like their skills, project, CV, etc. Also, this application is useful for "
                                  "Managers to quickly identify their team or other consultants using the search "
                                  "feature, manage the allocation of their team members and the projects they are "
                                  "involved in. ")

    short_description = driver.find_element(By.XPATH, '//textarea[@class="textarea"]')
    short_description.send_keys("The Match Windows App is built as a project staffing management and scheduling "
                                "solution, to cater to needs of managers to have a central place for resource "
                                "searching as well as reporting.")

    time.sleep(3)

    skill_search = driver.find_element(By.XPATH, '//input[@placeholder="Type in your Skill"]')
    skill_search.send_keys("python")
    time.sleep(5)
    select_skill = driver.find_element(By.XPATH, '(//div[@class="blazored-typeahead__result "])[1]')
    select_skill.click()
    time.sleep(2)

    level_dropdown = driver.find_element(By.XPATH, '//div[@class="mdc-select__anchor"]')
    level_dropdown.click()
    time.sleep(2)
    select_skill_level = driver.find_element(By.XPATH, '//span[text()="Level 2"]')
    select_skill_level.click()
    time.sleep(5)

    add_button = driver.find_element(By.XPATH, '//button[@aria-label="add"]')
    add_button.click()
    time.sleep(3)

    save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
    save_button.click()
    time.sleep(10)

    '''
    #Copy cv
'''


def copy_cv(driver):
    element = driver.find_element(By.XPATH, '(//div[text()="Copy"])[1]')

    actions = ActionChains(driver)

    actions.move_to_element(element).perform()

    copy_button = driver.find_element(By.XPATH, '(//div[text()="Copy"])[1]')
    time.sleep(5)
    copy_button.click()
    time.sleep(3)

    paste_button = driver.find_element(By.XPATH, '//div[text()="Paste"]')
    paste_button.click()
    time.sleep(10)


'''
    #delete the project
'''


def delete_cv(driver):
    element = driver.find_element(By.XPATH, '(//div[@class="flexColumn"])[2]')

    actions = ActionChains(driver)

    actions.move_to_element(element).perform()

    delete_icon = driver.find_element(By.XPATH, '(//div[@data-target="#DeleteModal"])[2]')
    time.sleep(5)
    delete_icon.click()
    time.sleep(2)

    button_delete = driver.find_element(By.XPATH, '(//button[text()="Delete"])[2]')
    button_delete.click()
    time.sleep(10)
