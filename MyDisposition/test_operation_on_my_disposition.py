import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_operation_on_my_disposition(login):
    driver = login
    time.sleep(5)

    my_disposition_tab = driver.find_element(By.XPATH, '//h6[text()="My Disposition"]')
    my_disposition_tab.click()
    time.sleep(5)

    day = driver.find_element(By.XPATH, '(//div[@class="mdc-button__ripple"])[2]')
    day.click()
    time.sleep(2)
    operation_on_drag_element(login)

    weeks = driver.find_element(By.XPATH, '(//div[@class="mdc-button__ripple"])[3]')
    weeks.click()
    time.sleep(2)
    operation_on_drag_element(login)

    calendar_weeks = driver.find_element(By.XPATH, '(//div[@class="mdc-button__ripple"])[4]')
    calendar_weeks.click()
    time.sleep(2)
    operation_on_drag_element(login)

    months = driver.find_element(By.XPATH, '(//div[@class="mdc-button__ripple"])[5]')
    months.click()
    time.sleep(2)
    operation_on_drag_element(login)

    Year = driver.find_element(By.XPATH, '(//div[@class="mdc-button__ripple"])[6]')
    Year.click()
    time.sleep(2)
    operation_on_drag_element(login)

    menu_button = driver.find_element(By.XPATH, '//button[@id="dropdownMenuButton"]')
    menu_button.click()
    time.sleep(2)


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
    time.sleep(5)
    action.click_and_hold(on_element=c2).move_to_element(c3).perform()
    c3.click()
    time.sleep(5)

    today = driver.find_element(By.XPATH, '(//div[@class="mdc-button__ripple"])[7]')
    today.click()
    time.sleep(5)

    today_arrow = driver.find_element(By.XPATH, '//i[text()="keyboard_arrow_left"]')
    today_arrow.click()
    time.sleep(5)
    today_arrow.click()
    time.sleep(5)

    today_arrow = driver.find_element(By.XPATH, '//i[text()="keyboard_arrow_right"]')
    today_arrow.click()
    time.sleep(5)
    today_arrow.click()
    time.sleep(5)
