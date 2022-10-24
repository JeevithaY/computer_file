from excel_lib import read_locators
from selenium_wrapper import SeleniumWrapper


class RegistrationPage(SeleniumWrapper):

    def __init__(self, driver):
        super().__init__(driver)

    locators = read_locators("registrationpage")

    def click_gender(self):
        element = RegistrationPage.locators['rdo_male']
        self.click_element(element)

    def enter_fastname(self, fname):
        element = RegistrationPage.locators['txt_fname']
        self.enter_text(element, value=fname)

    def enter_lastname(self, lname):
        element = RegistrationPage.locators['txt_lname']
        self.enter_text(element, value=lname)

    def enter_mail(self, mail):
        element = RegistrationPage.locators['txt_email']
        self.enter_text(element, value=mail)

    def enter_password(self, pwd):
        element = RegistrationPage.locators['txt_password']
        self.enter_text(element, value=pwd)

    def enter_cpwd(self, cpwd):
        element = RegistrationPage.locators['txt_confirm_password']
        self.enter_text(element, value=cpwd)

    def click_reg_btn(self):
        element = RegistrationPage.locators['btn_register']
        self.click_element(element)
