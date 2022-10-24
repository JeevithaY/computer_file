from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
driver = Chrome(r"C:\browser\chromedriver.exe")

driver.get("http://demowebshop.tricentis.com/")
driver.implicitly_wait(20)
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text() ='Twitter']").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])
driver.find_element(By.XPATH, "//input[@placeholder = 'Search Twitter']").send_keys("hello")
driver.switch_to.window(handles[0])
driver.find_element(By.LINK_TEXT, "Register").click()
for i in range(len(handles)):
    driver.switch_to.window(handles[i])
    driver.close()
    sleep(3)
