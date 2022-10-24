from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep

ser = Service(r"C:\browser\chromedriver.exe")
driver = webdriver.Chrome(service = ser)
driver.get("file:///C:/Users/user/Desktop/html_files/loading.html")
driver.maximize_window()
driver.implicitly_wait(10)
# wait = WebDriverWait(driver, 20)
# wait.until(visibility_of_element_located(("name" ,"fname")))
driver.find_element(By.NAME, "fname").send_keys("hello hai")
driver.close()
