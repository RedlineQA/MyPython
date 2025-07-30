from playwright.sync_api import expect

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
        expect(sign_out_button).to_be_visible()

    def verify_login_invalid_email_format(self):
        continue_button = self.page.get_by_role("button", name="Continue")
        continue_button.click()

        error_locator = self.page.locator("text=Oops! Please type in your correct email address")
        expect(error_locator).to_be_visible(timeout=1000)

    def verify_login_unregistered_email(self):
        join_button = self.page.get_by_role("button", name="Join ASOS")
        expect(join_button).to_be_visible(timeout=1000)

    def verify_login_wrong_password(self):
        sign_in_button = self.page.get_by_role("button", name="Sign in")
        sign_in_button.click()

        error_locator = self.page.locator("text=email or password were incorrect")
        expect(error_locator).to_be_visible()