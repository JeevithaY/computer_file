from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
driver  = Chrome(r"C:\browser\chromedriver.exe")

driver.get("https://www.google.com/")
driver.maximize_window()
a=driver.find_element(By.NAME, "q")
a.send_keys("java")
sleep(5)
all_sug = driver.find_elements(By.XPATH, "//span[contains(text(),'java')]")

print(all_sug)
for i in all_sug:
    t = i.text
    print(t)