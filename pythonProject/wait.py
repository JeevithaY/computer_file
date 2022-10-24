from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from config import Config


def _wait(func):

    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        wait = WebDriverWait(instance.driver, Config.MAX_TIMEOUT)
        v = visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper
