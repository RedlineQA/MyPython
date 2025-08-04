import re
import pytest

class BagPage:
    def __init__(self, page):
        self.page = page

    def try_click_add_to_bag(self) -> bool:
        try:
            print("🔍 Looking for the ADD TO BAG button on the product page")
            add_btn = self.page.locator('#pdp-react-critical-app [data-testid="add-button"]')
            add_btn.wait_for(state="visible", timeout=5000)

            print("✅ Found, scrolling into view")
            add_btn.scroll_into_view_if_needed()
            self.page.wait_for_timeout(500)

            print("🖱️ Hovering over the button")
            add_btn.hover()
            self.page.wait_for_timeout(300)

            print("🧪 Trying regular click + watching Network")
            with self.page.expect_response(lambda res: "bag" in res.url, timeout=5000) as response_info:
                add_btn.click()

            if self.page.get_by_test_id("bag-error-message").first.is_visible():
                print("❌ Add to bag failed — error message displayed")
                return False

            response = response_info.value
            print(f"✅ Network response from: {response.url} | status: {response.status}")

            if response.status != 200:
                print("❌ Add to bag request failed with non-200 status")
                return False

            return True

        except Exception as e:
            print(f"❌ Regular click failed: {e}")
            try:
                print("🛠️ Trying JS fallback click")
                self.page.eval_on_selector('#pdp-react-critical-app [data-testid="add-button"]', """
                    el => {
                        el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }));
                        el.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
                        el.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
                        el.click();
                    }
                """)
                self.page.wait_for_timeout(300)

                if self.page.get_by_test_id("bag-error-message").first.is_visible():
                    print("❌ JS fallback failed — error message displayed")
                    return False

                print("✅ Force-clicked via JS fallback.")
                return True
            except Exception as inner_e:
                print(f"❌ JS fallback completely failed: {inner_e}")
                return False

    def add_to_bag(self) -> bool:  # ✅ Returns success/failure
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

                for size_choice in range(options.count()):
                    text = options.nth(size_choice).inner_text().lower()

                    if "select" in text or "out of stock" in text:
                        continue

                    value = options.nth(size_choice).get_attribute("value")
                    self.page.select_option("#variantSelector", value=value)
                    self.page.eval_on_selector(
                        "#variantSelector",
                        "el => el.dispatchEvent(new Event('change', { bubbles: true }))"
                    )
                    self.page.wait_for_timeout(500)

                    result = self.try_click_add_to_bag()
                    if result:
                        return True
                    else:
                        print("🛑 Stopping test due to add-to-bag failure")
                        return False

                self.page.go_back()
                continue

            elif self.page.locator('#pdp-react-critical-app [data-testid="add-button"]').is_visible():
                result = self.try_click_add_to_bag()
                if result:
                    return True
                else:
                    print("🛑 Stopping test due to add-to-bag failure (no size selection case)")
                    return False
            else:
                self.page.go_back()

        return False  # In case we couldn’t add any item at all

    def verify_added_to_bag(self):
        print("🛒 Verifying bag contents")
        self.page.get_by_test_id("miniBagIcon").click()
        self.page.wait_for_load_state("domcontentloaded")

        empty_bag_title = self.page.locator("h1.empty-bag-title")
        if empty_bag_title.is_visible():
            print("⚠️ Detected 'Your bag is empty' despite trying to add a product.")
            raise Exception("❌ Expected item in bag, but got 'Your bag is empty' message")

        items_in_bag = self.page.locator("ul.bag-items > li")
        count = items_in_bag.count()
        print(f"✅ Bag contains {count} item(s)")
        assert count > 0, "❌ No items in the bag"