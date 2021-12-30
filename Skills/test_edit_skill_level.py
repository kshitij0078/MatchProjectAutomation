import time

from selenium.webdriver.common.by import By


def test_edit_skill(login):
    driver = login
    time.sleep(5)

    skill_tab = driver.find_element(By.XPATH, '//img[@alt="Skills"]')
    skill_tab.click()
    time.sleep(5)

    before_edit_skills = []
    before_edit_skills = driver.find_elements(By.XPATH, '//div[@class="tagCardDiv"]')
    a = []
    for i in before_edit_skills:
        list1 = i.text
        a.append(list1)

    time.sleep(10)

    button_edit = driver.find_element(By.XPATH, '//button[text()="Edit"]')
    button_edit.click()
    time.sleep(2)

    skill_to_be_changed = driver.find_element(By.XPATH, '(//span[text()="1"])[2]')
    skill_to_be_changed.click()
    time.sleep(2)

    skill_changed_to = driver.find_element(By.XPATH, '//div[@class="Experiencelevel3"]')
    skill_changed_to.click()
    time.sleep(2)

    button_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    button_save.click()
    time.sleep(3)

    after_edit_skills = []
    after_edit_skills = driver.find_elements(By.XPATH, '//div[@class="tagCardDiv"]')
    b = []
    for j in after_edit_skills:
        list2 = j.text
        b.append(list2)
    # print(b)
    time.sleep(5)

    print("\n", "Skilla which are changed the levels... :")
    c = []
    list3 = set(b).difference(a)
    c.append(list3)

    print(c)

    time.sleep(10)

    '''
    Delete the Skill
    '''

    before_edit_skills = []
    before_edit_skills = driver.find_elements(By.XPATH, '//div[@class="tagCardDiv"]')
    a = []
    for i in before_edit_skills:
        list1 = i.text
        a.append(list1)

    time.sleep(3)

    button_edit = driver.find_element(By.XPATH, '//button[text()="Edit"]')
    button_edit.click()
    time.sleep(2)

    delete_skill = driver.find_element(By.XPATH, '(//i[text()="clear"])[2]')
    delete_skill.click()
    time.sleep(2)

    button_save = driver.find_element(By.XPATH, '//button[text()="Save"]')
    button_save.click()

    time.sleep(3)

    after_edit_skills = []
    after_edit_skills = driver.find_elements(By.XPATH, '//div[@class="tagCardDiv"]')
    b = []
    for j in after_edit_skills:
        list2 = j.text
        b.append(list2)

    time.sleep(5)

    print("\n", "Skills which are deleted... :")
    c = []
    list3 = set(a).difference(b)
    c.append(list3)

    print(c)

    time.sleep(10)

    '''
    def intersection(lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
    print(intersection(a, b)) '''
