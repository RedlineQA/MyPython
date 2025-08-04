import re


class BagPage:
    def __init__(self, page):
        self.page = page

    def add_to_bag(self):
        self.page.get_by_test_id("men-floor").click()
        self.page.get_by_role("button", name="New in").hover()
        self.page.get_by_role("link", name="View all").click()

        product_link = self.page.locator(".productLink_KM4PI")
        product_count = product_link.count()

        for product in range(product_count):
            product_link.nth(product).click()
            self.page.wait_for_load_state("domcontentloaded")

            if self.page.locator("h2.Owf2X", has_text=re.compile("out of stock.*won't be back", re.I)).is_visible():
                self.page.go_back()
                continue

            if self.page.locator("#variantSelector").is_visible():
                options = self.page.locator("#variantSelector option")

                for size_choise in range(options.count()):
                    text = options.nth(size_choise).inner_text().lower()

                    if "select" in text or "out of stock" in text:
                        continue

                    value = options.nth(size_choise).get_attribute("value")
                    self.page.select_option("#variantSelector", value=value)
                    self.page.eval_on_selector("#variantSelector", "el => el.dispatchEvent(new Event('change', { bubbles: true }))")
                    self.page.wait_for_timeout(500)

                    if self.page.get_by_role("button", name="ADD TO BAG").first.is_visible():
                        self.page.get_by_role("button", name="ADD TO BAG").first.click()
                        return

                    elif self.page.get_by_role("button", name="NOTIFY ME").first.is_visible():
                        continue

                self.page.go_back()
                continue

            elif self.page.get_by_role("button", name="ADD TO BAG").first.is_visible():
                self.page.get_by_role("button", name="ADD TO BAG").first.click()
                return

            else:
                self.page.go_back()

    def verify_added_to_bag(self):
        self.page.get_by_role("button", name="#minibag-dropdown").hover()
        self.page.locator("[data-testid='bag-link']").click()


