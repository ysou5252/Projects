from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = "https://google.com"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_css_selector('#gb_70').click()

action.send_keys('id').perform()
action.reset_actions()
driver.find_element_by_class_name('VfPpkd-RLmnJb').click()

time.sleep(2)
driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('password')
driver.find_element_by_css_selector('VfPpkd-RLmnJ').click()
time.sleep(2)

driver.get('https://mail.google.com/mail/u/0/#inbox')
time.sleep(2)

driver.find_element_by_css_selector('.T-I.T-I-KE.L3').click()
time.sleep(1)

send_button = driver.find_element_by_css_selector('gU.Up')

action.send_keys('id').key_down(Keys.TAB).key_down(Keys.TAB).send_keys('제목').key_down(Keys.TAB).send_keys('내용입니다').move_to_element(send_button).perform()







