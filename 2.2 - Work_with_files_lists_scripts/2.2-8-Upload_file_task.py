import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('John')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Smith')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('john.smith@email.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(5)

finally:
    browser.quit()