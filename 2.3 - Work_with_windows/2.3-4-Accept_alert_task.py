import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element(By.TAG_NAME, "button").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    result = math.log(abs(12 * math.sin(x)))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)

    browser.find_element(By.TAG_NAME, "button").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    browser.quit()