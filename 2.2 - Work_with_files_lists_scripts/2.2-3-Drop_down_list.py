import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/selects1.html")
    a = browser.find_element(By.CSS_SELECTOR, "#num1")
    b = browser.find_element(By.CSS_SELECTOR, "#num2")
    c = str(int(a.text) + int(b.text))

    select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_value(c)

    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)

finally:
    browser.quit()
