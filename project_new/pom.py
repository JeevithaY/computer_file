from selenium.webdriver.common.by import By
class Login:

    txt_username_ ="Email"
    txt_password_id = "password"
    button_login_xpath = "//button[type ='login']"
    button_loout_xpath = "//button[type='logout']"

    def __init__(self, driver):
        self.driver = driver

    def enter_text_login(self, username):
        self.driver.find_element(By.ID, self.txt_username_).clear()