from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://httpbin.org/forms/post")
custname = browser.find_element_by_name("custname")
custname.clear()
custname.send_keys("Sean O'Connell")
for size_element in browser.find_elements_by_name('size'):
    if size_element.get_attribute('value') == 'medium':
        size_element.click()

for topping in browser.find_elements_by_name('topping'):
    if topping.get_attribute('value') in ['bacon', 'cheese']:
        topping.click()

browser.find_element_by_tag_name('form').submit()
sleep(10)
browser.quit()