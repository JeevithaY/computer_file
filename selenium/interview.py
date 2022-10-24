from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver = Chrome(r"C:\browser\chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Sony")
founders = driver.find_element(By.XPATH, "//th[text()='Founders']/../td/div/ul/li").text
founded = driver.find_element(By.XPATH, "//th[text() = 'Founded']/../td").text
head = driver.find_element(By.XPATH, "//th[text() = 'Headquarters']/../td").text
e_founder = "Masaru Ibuka"
e_founded = "7 May 1946"
e_head = "Sony City, "
assert e_founder == founders
# assert e_founded == founded
# assert e_head == head
