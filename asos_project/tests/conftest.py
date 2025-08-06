import pytest
from playwright.sync_api import sync_playwright

from asos_project.pages.bag_page import BagPage
from asos_project.pages.login_page import LoginPage
from asos_project.pages.preferences_page import PreferencesPage
from asos_project.pages.saved_items_page import SavedItemsPage
from asos_project.tests.globals import BASE_URL


@pytest.fixture()
def setup_asos():
    print("### Test start ###")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        )

        context.add_init_script("""Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""")

        context.clear_cookies()

        page = context.new_page()
        page.goto(BASE_URL)

        login_page = LoginPage(page)
        preferences_page = PreferencesPage(page)
        bag_page = BagPage(page)
        saved_items_page = SavedItemsPage(page)

        yield page, login_page, preferences_page, bag_page, saved_items_page

        page.close()
        browser.close()
        print("### Test end ###")
