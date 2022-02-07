from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:

    browser = webdriver.Chrome()
    browser.get(link)
    option1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    option1.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
