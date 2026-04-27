from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        login = LoginPage(page)
        login.enter_username("tomsmith")
        login.enter_password("SuperSecretPassword!")
        login.click_login()

        assert "Secure Area" in page.content()

        browser.close()