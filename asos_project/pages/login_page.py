class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, user_email, user_password):
        user_login_button = self.page.locator("#myAccountDropdown")
        user_login_button.click()

        sign_in_by_text = self.page.locator("text=Sign In")
        sign_in_by_text.click()

        email_input = self.page.locator("#email")
        email_input.type(user_email, delay=50)

        self.page.evaluate("""
            () => {
                const input = document.querySelector('#email');
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
                input.dispatchEvent(new Event('blur', { bubbles: true }));
            }
        """)

        continue_button = self.page.locator("button.button-module_button__17Mvp")
        self.page.wait_for_timeout(1000)
        continue_button.click()

        self.page.wait_for_selector("#password")
        password_input = self.page.locator("#password")
        password_input.type(user_password, delay=50)

        self.page.evaluate("""
            () => {
                const input = document.querySelector('#password');
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
                input.dispatchEvent(new Event('blur', { bubbles: true }));
            }
        """)

        sign_in_button = self.page.locator("button.button-module_content__35zEt")
        sign_in_button.click()