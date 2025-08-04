class TestBag:
    def test_add_to_bag(self, setup_asos):
        page, _, _, bag_page = setup_asos

        bag_page.add_to_bag()

        bag_page.verify_added_to_bag()
