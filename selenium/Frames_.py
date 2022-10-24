from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
ser = Service(r"C:\browser\chromedriver.exe")
driver = webdriver.Chrome(service = ser)

driver.get("file:///C:/Users/user/Desktop/html_files/iframe.html")
driver.implicitly_wait(20)
driver.maximize_window()
driver.switch_to.frame("frame1")
driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.XPATH, "(//input[@type = 'radio'])[2]").click()
driver.switch_to.parent_frame()
driver.switch_to.frame("frame2")
driver.find_element(By.LINK_TEXT, "Request Demo").click()
sleep(4)
driver.switch_to.default_content()
driver.quit()
