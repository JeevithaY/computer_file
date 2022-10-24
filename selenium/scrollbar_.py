from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

ser = Service(r"C:\browser\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.implicitly_wait(20)
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(5)
driver.execute_script("window.scrollBy(0,1000)","")
element = driver.find_element(By.XPATH, "//span[text()='Customer Support ']")
sleep(3)
driver.execute_script("arguments[0].scrollIntoView();", element)
sleep(3)
driver.execute_script("window.scrollBy(0,-300)","")
sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")



