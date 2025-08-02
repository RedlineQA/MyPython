from playwright.sync_api import expect
from selenium.common import TimeoutException


class LoginPage:
    def __init__(self, page):
        self.page = page


    def trigger_input_events(self, selector: str):
        self.page.evaluate(f"""
            () => {{
                const input = document.querySelector('{selector}');
                input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                input.dispatchEvent(new Event('change', {{ bubbles: true }}));
                input.dispatchEvent(new Event('blur', {{ bubbles: true }}));
            }}
        """)


    def login_user_email(self, user_email):
        my_account_button = self.page.locator("#myAccountDropdown")
        my_account_button.click()

        sign_in_by_text = self.page.locator("text=Sign In")
        sign_in_by_text.click()

        email_input = self.page.locator("#email")
        email_input.type(user_email, delay=50)

        self.trigger_input_events("#email")

        continue_button = self.page.get_by_role("button", name="Continue")
        continue_button.click()


    def login_user_password(self, user_password):
        self.page.wait_for_selector("#password")
        password_input = self.page.locator("#password")
        password_input.type(user_password, delay=50)

        self.trigger_input_events("#password")

        sign_in_button = self.page.get_by_role("button", name="Sign in")
        sign_in_button.click()


    def verify_login_success(self):
        my_account_button = self.page.locator("#myAccountDropdown")
        my_account_button.click()

        sign_out_button = self.page.locator("text=Sign out")
        try:
            expect(sign_out_button).to_be_visible()
            print("\u2705 Successfully logged in")
        except AssertionError:
            print("\u274C Failed to log in")
            print("\u2139 Possible cause: User access may have been temporarily restricted by site security mechanisms")
            raise


    def verify_login_invalid_email_format(self):
        continue_button = self.page.get_by_role("button", name="Continue")
        continue_button.click()

        error_locator = self.page.locator("text=Oops! Please type in your correct email address")
        try:
            expect(error_locator).to_be_visible(timeout=1000)
            print("\u2705 Error message appeared for invalid email format as expected.")
        except AssertionError:
            print("\u274C Error message did not appear for invalid email format.")
            print("\u2139 Possible cause: Validation text may have changed or failed to load in time.")
            raise


    def verify_login_unregistered_email(self):
        join_button = self.page.get_by_role("button", name="Join ASOS")
        try:
            expect(join_button).to_be_visible(timeout=3000)
            print("\u2705 System correctly detected unregistered email and offered registration.")
        except AssertionError:
            print("\u274C 'Join ASOS' button did not appear for unregistered email.")
            print("\u2139 Possible cause: The email may not have been detected as unregistered.")
            raise


    def verify_login_wrong_password(self):
        sign_in_button = self.page.get_by_role("button", name="Sign in")
        sign_in_button.click()

        error_locator = self.page.locator("text=email or password were incorrect")
        try:
            expect(error_locator).to_be_visible()
            print("\u2705 Error message appeared as expected for wrong password.")
        except AssertionError:
            print("\u274C Error message did not appear for invalid password")
            print("\u2139 Note: Passwords have no format validation, so any incorrect input should trigger a general login error")
            raise