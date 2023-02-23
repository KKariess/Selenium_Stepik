import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    # - Open web page
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    # - Click on button
    browser.find_element(By.TAG_NAME, "button").click()

    # - Assign tab names & switch to second tab
    firstW = browser.window_handles[0]
    secondW = browser.window_handles[1]
    browser.switch_to.window(secondW)

    # - Get x value, calculate & input the result
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    result = math.log(abs(12 * math.sin(x)))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)

    # - Click submit button
    browser.find_element(By.TAG_NAME, "button").click()

    # - Read alert window text, print it into the console & accept the alert
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    browser.quit()
