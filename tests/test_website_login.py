from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from data.login_data import test_data

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(page)

    for data in test_data:
        print("Testing:", data["username"])

        login_page.enter_username(data["username"])
        login_page.enter_password(data["password"])
        login_page.click_login()

        page.wait_for_timeout(3000)

        page.goto("https://the-internet.herokuapp.com/login")

    browser.close()