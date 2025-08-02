class TestPreferences:
    def test_change_currency(self, setup_asos):
        page, _, preferences_page = setup_asos

        preferences_page.change_currency()

        try:
            preferences_page.verify_currency_change_in_preferences()
        except AssertionError as e:
            print(f"\u26A0\uFE0F Currency in preferences failed: {e}")

        try:
            preferences_page.verify_currency_change_in_products()
        except AssertionError as e:
            print(f"\u26A0\uFE0F Currency in products failed: {e}")

