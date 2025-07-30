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

    def login(self, user_email, user_password):
        my_account_button = self.page.locator("#myAccountDropdown")
        my_account_button.click()

        sign_in_by_text = self.page.locator("text=Sign In")
        sign_in_by_text.click()

        email_input = self.page.locator("#email")
        email_input.type(user_email, delay=50)

        self.trigger_input_events("#email")

        continue_button = self.page.get_by_role("button", name="Continue")
        self.page.wait_for_timeout(1000)
        continue_button.click()

        self.page.wait_for_selector("#password")
        password_input = self.page.locator("#password")
        password_input.type(user_password, delay=50)

        self.trigger_input_events("#password")

        sign_in_button = self.page.get_by_role("button", name="Sign in")
        self.page.wait_for_timeout(1000)
        sign_in_button.click()

    def verify_login_success(self):
        my_account_button = self.page.locator("#myAccountDropdown")
        my_account_button.click()
        assert self.page.locator("text=Sign out").is_visible()