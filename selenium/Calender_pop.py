from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome(r"C:\browser\chromedriver.exe")

driver.get("https://www.goibibo.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//span[@class='sc-kgflAQ ezEjxY fswDownArrow']").click()
date = '13'
month_ = 'January 2023'
for _ in range(12):
    try:
        driver.find_element(By.XPATH, f"//div[text() = '{month_}']/../..//p[text() = '{date}']").click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//span[@class ='DayPicker-NavButton DayPicker-NavButton--next']").click()
        sleep(4)
driver.close()
