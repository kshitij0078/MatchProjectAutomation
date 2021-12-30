import time

from selenium.webdriver.common.by import By


def test_add_cv_profile(login):
    '''first way is from scratch, 2nd is from plus button'''
    driver = login
    time.sleep(5)

    cv_tab = driver.find_element(By.XPATH, '//h6[text()="CV"]')
    cv_tab.click()
    time.sleep(5)

    element = []
    element = driver.find_elements(By.XPATH, '//div[@role="tablist"]')

    if len(element) == 0:
        add_button = driver.find_element(By.XPATH, '//button[text()="Add"]')
        add_button.click()
        time.sleep(2)

        cv_name = driver.find_element(By.XPATH, '//input[@placeholder="Standardprofil"]')
        cv_name.send_keys("Hemanth Gaddam")
        time.sleep(2)

        save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
        save_button.click()
        time.sleep(5)

        cv_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
        print("\n")
        print(cv_status_msg.text)
        time.sleep(5)

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
        project_name.send_keys("Library Management System")
        time.sleep(2)

        project_description = driver.find_element(By.XPATH, '//div[@class="ql-editor ql-blank"]')
        project_description.send_keys("The system randomly generates the QR Code and OTP at the time of login. "
                                      "It makes the login more secure. However, to use this system, "
                                      "one always needs an active Internet connection.")

        short_description = driver.find_element(By.XPATH, '//textarea[@class="textarea"]')
        short_description.send_keys("This project focuses on building an e-Authentication system using a "
                                    "combination of QR code and OTP for enhanced security.")

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

        add_button = driver.find_element(By.XPATH, '//button[@aria-label="add"]')
        add_button.click()
        time.sleep(3)

        save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
        save_button.click()
        time.sleep(10)

    else:

        new_button = driver.find_element(By.XPATH, '//i[text()="add"]')
        new_button.click()
        time.sleep(5)

        cv_name = driver.find_element(By.XPATH, '//input[@placeholder="CV Name"]')
        cv_name.send_keys("Hemanth Gaddam")
        time.sleep(2)

        save_button = driver.find_element(By.XPATH, '//button[text()="Save"]')
        save_button.click()
        time.sleep(5)

        upload_status_msg = driver.find_element(By.XPATH, '//p[@class="blazored-toast-message"]')
        print("\n")
        print(upload_status_msg.text)
        time.sleep(5)

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
                                      "they are involved in")

        short_description = driver.find_element(By.XPATH, '//textarea[@class="textarea"]')
        short_description.send_keys("The Match App is built as a project staffing management and scheduling "
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









