class TestPreferences:
    def test_change_country(self, setup_asos):
        page, _, preferences_page, _, _ = setup_asos

        preferences_page.change_country()
        preferences_page.verify_country_change()

    def test_change_currency(self, setup_asos):
        page, _, preferences_page, _, _ = setup_asos

        preferences_page.change_currency()

        errors = []

        try:
            preferences_page.verify_currency_change_in_preferences()
        except AssertionError as e:
            print(f"\u26A0\uFE0F Currency in preferences failed: {e}")
            errors.append(e)

        try:
            preferences_page.verify_currency_change_in_products()
        except AssertionError as e:
            print(f"\u26A0\uFE0F Currency in products failed: {e}")
            errors.append(e)

        if errors:
            raise AssertionError(" | ".join(str(e) for e in errors))