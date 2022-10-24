from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome(r"C:\browser\chromedriver.exe")
driver.get("https://www.amezon.com")
driver.maximize_window()
driver.implicitly_wait(10)
element = driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
action = ActionChains(driver)
action.move_to_element(element).perform()
driver.find_element(By.XPATH, "//span[text()='Account']").click()
expected_title = "Your Account"
actual_title = driver.title
assert actual_title == expected_title



