import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_driver_path = "/Users/user/Downloads/chromedriver-mac-arm64 3/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get("https://the-internet.herokuapp.com/javascript_alerts")
js_alert = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
js_alert.click()
actions = ActionChains(driver)
actions.double_click(js_alert)
print(js_alert.get_attribute("type"))
driver.save_screenshot("click_js_alert.jpg")

alert = driver.switch_to.alert
alert.accept()
time.sleep(2)

confirm_alert = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_alert.click()
con_alert = driver.switch_to.alert
con_alert.dismiss()
time.sleep(2)

prompt_alert = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_alert.click()
pro_alert = driver.switch_to.alert
pro_alert.send_keys("555555")
pro_alert.accept()
time.sleep(2)

