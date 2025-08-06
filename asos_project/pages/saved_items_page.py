class SavedItemsPage:
    def __init__(self, page):
        self.page = page

    def add_to_saved_items(self):
        self.page.get_by_test_id("men-floor").click()

        self.page.get_by_role("button", name="New in").hover()
        self.page.get_by_role("link", name="View all").first.click()

        self.page.locator(".productLink_KM4PI").first.click()

        self.page.locator(".AGXyD.GIdCP").click()

    def remove_from_saved_items(self):
        self.add_to_saved_items()

        self.page.get_by_test_id("savedItemsIcon").first.click()

        self.page.locator(".deleteButton_c9wnw.deleteButton_hkW_Q").click()

    def verify_add_to_saved_items(self):
        self.page.get_by_test_id("savedItemsIcon").first.click()

        product = self.page.locator(".customerItemsProductTile_UTepY")

        self.page.wait_for_timeout(1000)

        assert product.is_visible(), "\u274C Item not visible in Saved Items!"
        print("\u2705 Item successfully found in Saved Items!")

    def verify_remove_from_saved_items(self):
        self.page.get_by_test_id("savedItemsIcon").first.click()

        self.page.wait_for_timeout(1000)

        no_item = self.page.locator("h2.noItemsTitle_uTxWD.title_uIMya")

        assert no_item.is_visible(), "\u274C Failed to remove item from Saved Items!"
        print("\u2705 Item successfully removed from Saved Items!")