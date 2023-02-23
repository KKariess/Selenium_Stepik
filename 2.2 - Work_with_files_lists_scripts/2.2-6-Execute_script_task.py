import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("http://SunInJuly.github.io/execute_script.html")
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    result = math.log(abs(12 * math.sin(x)))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    button.click()
    time.sleep(5)

finally:
    browser.quit()
