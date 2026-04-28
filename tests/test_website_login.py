from utils.browser_setup import launch_browser
from pages.login_page import LoginPage


def test_login_failure():
    p, browser, page = launch_browser()

    page.goto("https://the-internet.herokuapp.com/login")

    login = LoginPage(page)
    login.enter_username("wrong")
    login.enter_password("wrong")
    login.click_login()

    assert "invalid" in page.content()

    browser.close()
    p.stop()