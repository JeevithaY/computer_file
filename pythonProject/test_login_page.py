from loginpage import LoginPage
from home_page import HomePage
from confitest import setup


def test_login(setup):

    hp = HomePage(setup)
    hp.click_login()
    lp = LoginPage(setup)
    lp.enter_email("hello.world@company.com")
    lp.enter_password("Password123")
    lp.click_login()

