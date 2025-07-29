import pytest
from playwright.sync_api import sync_playwright

from asos_project.pages.login_page import LoginPage


@pytest.fixture()
def setup_asos():
    print("### Test start ###")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        )

        context.add_init_script("""Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""")

        context.clear_cookies()

        page = context.new_page()
        page.goto("https://www.asos.com/")

        login_page = LoginPage(page)

        yield page, login_page

        print("### Test end ###")
        page.close()
        browser.close()