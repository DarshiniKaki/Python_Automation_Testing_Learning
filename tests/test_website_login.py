from utils.browser_setup import launch_browser
from pages.login_page import LoginPage


def test_login_success():
    p, browser, page = launch_browser()

    page.goto("https://the-internet.herokuapp.com/login")

    login = LoginPage(page)
    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    assert "Secure Area" in page.content()

    browser.close()
    p.stop()