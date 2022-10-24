from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

ser = Service(r"C:\browser\chromedriver.exe")
driver = webdriver.Chrome(service = ser)
driver.implicitly_wait(20)
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.delete_all_cookies()
driver.find_element(By.XPATH, "//div[text()='Login']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys("jeevitha.y94@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("kiran@jeevi")
driver.find_element("xpath","//button[text() = 'Login']").click()
driver.find_element("")

