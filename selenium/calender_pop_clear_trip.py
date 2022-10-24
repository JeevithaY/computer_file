from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome(r"C:\browser\chromedriver.exe")

driver.get("https://www.cleartrip.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[@class ='px-1 plNew  flex flex-middle nmx-1 pb-1']").click()
driver.find_element(By.XPATH, "//div[@class ='card']").click()
sleep(5)
driver.find_element(By.XPATH, "//div[@class = 'flex flex-middle flex-between p-relative homeCalender']").click()

# driver.close()