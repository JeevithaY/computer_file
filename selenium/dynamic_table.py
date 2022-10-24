from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome(r"C:\browser\chromedriver.exe")
driver.get("file:///C:/Users/user/Desktop/html_files/demo.html")
driver.implicitly_wait(20)
driver.maximize_window()

# sleep(4)
# t = driver.find_element(By.XPATH, "//td[text()='AAPL']/../td[3]")
# print(t.text)
# driver.close()

# fnames = driver.find_elements(By.XPATH, "//th[text()='Firstname']/../..//td[2]")
# first_name = [fname.text for fname in fnames]
# print(first_name)
# l = sorted(first_name)
# print(l)
# if first_name == l:
#     print("pass")
# else:
#     print("fail")

