class TestSavedItems:
    def test_saved_item(self, setup_asos):
        page, _, _, _, saved_item_page = setup_asos

        saved_item_page.add_to_saved_items()

        saved_item_page.verify_add_to_saved_items()

    def test_remove_from_saved_item(self, setup_asos):
        page, _, _, _, saved_item_page = setup_asos

        saved_item_page.remove_from_saved_items()

        saved_item_page.verify_remove_from_saved_items()