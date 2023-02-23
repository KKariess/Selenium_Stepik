import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#price"), "$100"
    ))
    browser.find_element(By.CSS_SELECTOR, "#book").click()

    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    result = math.log(abs(12 * math.sin(x)))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)

    browser.find_element(By.CSS_SELECTOR, "#solve").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    browser.quit()
