import re


class Preferences:
    def __init__(self, page):
        self.page = page

    def change_country(self):
        self.page.locator('[data-testid="country-selector-btn"]').first.click()

        self.page.select_option("#country", value="IL")

        selected_country_text = self.page.locator("#country >> option[selected]").inner_text()

        print(f"\U0001F4CC Selected country after select option: {selected_country_text}")

        self.page.get_by_role("button", name="UPDATE PREFERENCES").click()

    def change_currency(self):
        self.change_country()

        # Currency selection is only available when country is set to Israel.
        # In other regions (e.g. US, UK, EU), the currency is fixed and the dropdown is disabled.

        self.page.locator('[data-testid="country-selector-btn"]').first.click()

        self.page.select_option("#currency", value="2")
        self.page.eval_on_selector("#currency", "el => el.dispatchEvent(new Event('change', { bubbles: true }))")

        selected_currency_text = self.page.locator("#currency >> option[selected]").inner_text()
        print(f"\U0001F4CC Selected currency after select option: {selected_currency_text}")

        self.page.get_by_role("button", name="UPDATE PREFERENCES").click()

    def verify_country_change(self):
        self.page.locator('[data-testid="country-selector-btn"]').first.click()

        selected_country_text = self.page.locator("#country >> option[selected]").inner_text()

        self.page.get_by_role("button", name="UPDATE PREFERENCES").click()

        assert (selected_country_text == "Israel")

    def verify_currency_change_in_preferences(self):
        self.page.locator('[data-testid="country-selector-btn"]').first.click()

        selected_currency_text = self.page.locator("#currency >> option[selected]").inner_text()

        currency = selected_currency_text[2:]

        print(f"Currency selector test: {currency}")

        self.page.get_by_role("button", name="UPDATE PREFERENCES").click()

        # Known issue: although USD is selected, the site reverts back to ILS automatically.
        # This appears to be due to client-side enforcement or server logic.

        assert "USD" in selected_currency_text, f"\u274C Currency not set to USD! Found: {selected_currency_text}"

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
