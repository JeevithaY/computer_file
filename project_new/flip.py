import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome(r"C:\browser\chromedriver.exe")
driver.get("https://www.flipkart.com")
driver.maximize_window()
driver.implicitly_wait(40)
driver.find_element(By.XPATH, "//input[@class = '_2IX_2- VJZDxU']").send_keys("8792641743")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("kiran@jeevi")
driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[text()='Home & Furniture']").click()
path = "//h2[text()='Stylish Home Decor']/../../../div[2]/div/div/div[1]/div//div[text()='Wall Clocks']"
driver.find_element(By.XPATH, path).click()
driver.find_element(By.XPATH, "(//a[text()='Hb Mall India Analog 30 cm X 30 cm Wall Clock'])[1]").click()
handle = driver.window_handles
driver.switch_to.window(handle[1])
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']").click()


