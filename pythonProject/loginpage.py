from excel_lib import read_locators
from selenium_wrapper import SeleniumWrapper

from time import sleep


class LoginPage(SeleniumWrapper):
    def __init__(self, driver):
        super().__init__(driver)

    locators = read_locators("loginpage")

    def enter_email(self, email):
        element = LoginPage.locators['txt_email']
        self.enter_text(element, value=email)

    def enter_password(self, password):
        element = LoginPage.locators['txt_password']
        self.enter_text(element, value=password)

    def click_login(self):
        element = LoginPage.locators['btn_login']
        self.click_element(element)



# class Login_Page(SeleniumWrapper):
#
#     def __int__(self, driver):
#         super.__init__(driver)
#
#     email_text = ("name", "Email")
#     password_text = ("id", "Password")
#     login_button = ("xpath", "//input[@value = 'Log in']")
#
#     def enter_email(self, email):
#         self.enter_text(Login_Page.email_text, value=email)
#
#     def enter_password(self, password):
#         self.enter_text(Login_Page.password_text, value=password)
#
#     def click_login(self):
#         self.click_element(Login_Page.login_button)
