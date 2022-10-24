from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

driver =Chrome(r"C:\browser\chromedriver.exe")
driver.get("https://www.myntra.com/")
driver.save_screenshot("./pythonProject/snap.png")
driver.maximize_window()
