from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
ser = Service(r"C:\browser\chromedriver.exe")
driver = webdriver.Chrome(service = ser)

driver.get("http://demowebshop.tricentis.com/")
driver.implicitly_wait(20)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@value = 'Search']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.close()