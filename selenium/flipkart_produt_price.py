from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ser = Service(r"C:\browser\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()
driver.find_element(By.NAME, "q").send_keys("iphone 13 pro max"+Keys.ENTER)
product = driver.find_elements(By.XPATH, "//div[contains(text(),'APPLE iPhone 13 Pro Max') and @class] ")
xpath = "//div[contains(text(),'APPLE iPhone 13 Pro Max') and @class] /../../div[2]/div[1]/div[1]"
price = driver.find_elements(By.XPATH, xpath)
for pro, pri in zip(product, price):
    print(pro.text, pri.text, sep="-----")

driver.close()
