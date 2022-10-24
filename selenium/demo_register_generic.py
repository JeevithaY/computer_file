from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service

ser = Service(r"C:\browser\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()


def _wait(func):

    def wrapper(*args, **kwargs):
        locator = args[0]
        wait = WebDriverWait(driver, 20)
        v = visibility_of_element_located(locator)
        wait.until(v)
        func(*args, **kwargs)
    return wrapper


@_wait
def element_click(locator):
    driver.find_element(*locator).click()


@_wait
def enter_text(locator, *, value):
    driver.find_element(*locator).click()
    driver.find_element(*locator).send_keys(value)


@_wait  # select_item = _wait(select_item)
def select_item(self, locator, *, item):
    element = self.driver.find_element(*locator)
    s = Select(element)
    if isinstance(item, str):
        s.select_by_visible_text(item)
    elif isinstance(item, int):
        s.select_by_index(item)
    else:
        raise Exception


element_click((By.LINK_TEXT, "Register"))
element_click((By.ID, "gender-female"))
enter_text((By.NAME, "FirstName"), value="hello")
enter_text((By.NAME, "LastName"), value="world")
enter_text((By.CSS_SELECTOR, "input[name = 'Email']"), value="hello.world@company.com")
enter_text((By.ID, "Password"), value="password123")
enter_text((By.ID, "ConfirmPassword"), value="password123")
element_click((By.ID, "register-button"))
driver.close()
