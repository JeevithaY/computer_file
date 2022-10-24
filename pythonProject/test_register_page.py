from selenium.webdriver.common.by import By
from selenium_wrapper import SeleniumWrapper
from confitest import setup
from home_page import HomePage
from registrationpage import RegistrationPage


def test_register(setup):
    hp = HomePage(setup)
    hp.click_register()
    rp = RegistrationPage(setup)
    rp.click_gender()
    rp.enter_fastname("hello")
    rp.enter_lastname("world")
    rp.enter_mail("helloworld@gmail.com")
    rp.enter_password("Password123")
    rp.enter_cpwd("Password123")
    rp.click_reg_btn()
