import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = "/Users/user/Downloads/chromedriver-mac-arm64 3/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver,10)

driver.get("https://the-internet.herokuapp.com/jqueryui/menu")
#hover over "Enabled"

enable = driver.find_element(By.ID, "ui-id-3")
ActionChains(driver).move_to_element(enable).perform()
time.sleep(2)

downloads = wait.until(EC.element_to_be_clickable((By.ID, 'ui-id-4')))
ActionChains(driver).move_to_element(downloads).perform()
time.sleep(2)

excel = driver.find_element(By.ID, "ui-id-7")
excel.click()
time.sleep(2)

print("menu interaction passed")



