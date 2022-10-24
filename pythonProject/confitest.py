from time import sleep
from selenium.webdriver import Chrome
from pytest import fixture
from config import Config


@fixture()
def setup(scope="session"):
    print("open browser ")
    driver = Chrome(Config.DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    sleep(3)
    yield driver
    print("closing browser")
    driver.close()
