import re

class Preferences:
    def __init__(self, page):
        self.page = page

    def change_currency(self):
        self.page.locator('[data-testid="country-selector-btn"]').first.click()

        # Currency selection is only available when country is set to Israel.
        # In other regions (e.g. US, UK, EU), the currency is fixed and the dropdown is disabled.

        self.page.select_option("#currency", value="2")

        selected_option_text = self.page.locator("#currency >> option[selected]").inner_text()
        print(f"\U0001F4CC Selected currency after select_option: {selected_option_text}")

        self.page.get_by_role("button", name="UPDATE PREFERENCES").click()

    def verify_currency_change_in_preferences(self):
        self.page.locator('[data-testid="country-selector-btn"]').first.click()

        selected_option_text = self.page.locator("#currency >> option[selected]").inner_text()

        currency = selected_option_text[2:]

        print(f"Currency selector test: {currency}")

        self.page.get_by_role("button", name="UPDATE PREFERENCES").click()

        assert "USD" in selected_option_text, f"\u274C Currency not set to USD! Found: {selected_option_text}"


    def verify_currency_change_in_products(self):
        self.page.get_by_test_id("men-floor").click()

        self.page.get_by_role("button", name="New in").hover()
        self.page.get_by_role("link", name="View all").click()

        price_element = self.page.locator("[class='price__B9LP']").first
        price_text = price_element.text_content()
        match = re.match(r"([^\d]+)([\d.,]+)", price_text)

        if match:
            currency = match.group(1).strip()
            amount = match.group(2).strip()
            print(f"Currency: {currency}")
            assert currency in ["$", "USD"], f"\u274C Currency in products is not USD! Found: {currency}"
        else:
            raise AssertionError(f"\u274C Failed to parse price text: {price_text}")