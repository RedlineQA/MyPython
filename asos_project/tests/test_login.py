import pytest

from asos_project.tests.globals import VALID_USER_EMAIL_SUCCESS_LOGIN, VALID_USER_PASSWORD_SUCCESS_LOGIN, \
    VALID_USER_EMAIL_WRONG_PASSWORD, WRONG_PASSWORD, INVALID_USER_EMAIL_FORMAT, UNREGISTERED_EMAIL


class TestLogin:
    def test_login_existing_user(self, setup_asos):
        page, login_page, _ = setup_asos
        login_page.login_user_email(VALID_USER_EMAIL_SUCCESS_LOGIN)
        login_page.login_user_password(VALID_USER_PASSWORD_SUCCESS_LOGIN)
        login_page.verify_login_success()


    def test_login_invalid_email_format(self, setup_asos):
        page, login_page, _ = setup_asos
        login_page.login_user_email(INVALID_USER_EMAIL_FORMAT)
        login_page.verify_login_invalid_email_format()


    def test_login_unregistered_email(self, setup_asos):
        page, login_page, _ = setup_asos
        login_page.login_user_email(UNREGISTERED_EMAIL)
        login_page.verify_login_unregistered_email()


    def test_login_wrong_password(self, setup_asos):
        page, login_page, _ = setup_asos
        login_page.login_user_email(VALID_USER_EMAIL_WRONG_PASSWORD)

        lock_message = page.locator("text=This account is locked")

        if lock_message.is_visible(timeout=2000):
            print("\U0001F512 Account temporarily locked (30 minutes). Skipping test.")
            pytest.skip("Account locked – skipping invalid password test.")

        login_page.login_user_password(WRONG_PASSWORD)
        login_page.verify_login_wrong_password()