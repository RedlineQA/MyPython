import pytest

class TestLogin:
    def test_login_existing_user(self, setup_asos):
        page, login_page = setup_asos
        login_page.login_user_email("heavybrown@somoj.com")
        login_page.login_user_password("12345qwerty")
        login_page.verify_login_success()

    def test_login_invalid_email_format(self, setup_asos):
        page, login_page = setup_asos
        login_page.login_user_email("qwerty")
        login_page.verify_login_invalid_email_format()

    def test_login_unregistered_email(self, setup_asos):
        page, login_page = setup_asos
        login_page.login_user_email("unregistered@gmail.com")
        login_page.verify_login_unregistered_email()

    def test_login_wrong_password(self, setup_asos):
        page, login_page = setup_asos
        login_page.login_user_email("heavybrown@somoj.com")

        if not page.locator("#password").is_visible(timeout=3000):
            print("\U0001F512 Account temporarily locked (30 minutes). Skipping test.")
            pytest.skip("Account locked – skipping invalid password test.")

        login_page.login_user_password("wrongpassword")
        login_page.verify_login_wrong_password()