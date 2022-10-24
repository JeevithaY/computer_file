from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome(r"C:\browser\chromedriver.exe")
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
action = ActionChains(driver)
job_ = driver.find_element(By.XPATH, "//a[text()='Job search']")
job_skill = driver.find_element(By.XPATH, "//a[text() = 'Jobs by Skills']")
action.move_to_element(job_).move_to_element(job_skill).perform()
driver.find_element(By.XPATH, "//a[contains(text(), 'Angular Js Jobs')]").click()