import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    yield page

    browser.close()
    p.stop()