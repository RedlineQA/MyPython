# 🧪 ASOS UI Test Automation (Python + Playwright)

This project is a UI test automation framework for the **login functionality** of the ASOS website using **Python** and **Playwright**.

---

## 🎯 Project Goals

- Automate login flow for an existing user
- Validate multiple negative login scenarios (invalid email, unregistered email, wrong password)
- Demonstrate usage of **Playwright** with **Pytest** and **Page Object Model (POM)**
- Handle real-world anti-bot mechanisms and dynamic web behavior
- Automate currency preference change 

---

## 🛠️ Tools & Technologies

- Python
- Playwright (`pytest-playwright`)
- Pytest
- Page Object Model structure

---

## 🔐 Login Test Notes
The following login scenarios are covered:
- ✅ Login with valid existing user
- ❌ Login attempt with invalid email format
- ❌ Login attempt with unregistered email
- ❌ Login attempt with incorrect password

Due to ASOS's bot protection mechanisms, login attempts may occasionally fail even with correct credentials.
This is likely caused by server-side anti-automation measures, including:
- Bot detection
- Rate limiting
- Temporary blocking

🛑 Important Note on User Blocking:
If login consistently fails for a specific account, even after multiple retries and across devices or networks, the user account itself may have been flagged and temporarily blocked by ASOS.
This can happen after repeated login attempts or fast, bot-like behavior.

✅ **Recommendation**:  
- If login fails without clear reason, wait a few minutes and try again.
- Avoid repeated login attempts in short periods.
- Add small delays between actions (e.g. ```await page.wait_for_timeout(1000)```).
- If an account gets blocked, create a new test user and continue testing with that.

---

### 🤖 Why `.type()` instead of `.fill()`?

The login form uses JavaScript-based validation that listens for **real user input events** like `input`, `change`, and `blur`.

To simulate **human-like typing** and trigger those events correctly, the following was used:

```python
email_input.type(user_email, delay=50)
```

Instead of:

```python
email_input.fill(user_email)
```

This approach reduces the chance of bot detection and ensures the form behaves as if a human is interacting with it.

---

## ⚙️ Country & Currency Preferences Test

This test ensures that updating the user's **country** and **currency** preferences works correctly and is reflected in both:

- The **selected values in the preferences modal**
- The **pricing of actual listed products**

---

### 🧪 Test Flow:

1. Open preferences modal  
2. Change **country** to Israel using `select_option("#country", value="IL")`  
   - This step is required, as currency selection is only available for Israel  
3. Change **currency** using `select_option("#currency", value="2")`  
4. Click **UPDATE PREFERENCES**  
5. Re-open modal and assert `Israel` and `$ USD` are selected  
6. Navigate to product list  
7. Extract first product price  
8. Assert currency symbol is `$` or `USD`

---

### ⚠️ Note: Currency Selector is Region-Specific

The currency dropdown is **only available when the selected country is set to Israel**.  
In all other regions (e.g. US, UK, EU), the currency is fixed and the dropdown is disabled.  
As a result, the test explicitly sets the country to **Israel** before attempting to change the currency.

---

### ⚠️ Known Issue with the Currency Dropdown

Despite selecting USD via code and confirming that the correct option is visually marked as `selected`, the preference often **reverts back to ILS (₪)**.

Example of code used:

```python
page.select_option("#currency", value="2")
```

Even with added JavaScript event dispatches:

```python
page.eval_on_selector("#currency", "el => el.dispatchEvent(new Event('change', { bubbles: true }))")
```

…the site may still ignore the change.

---

### ✅ Conclusion:

This is assumed to be a bug in the website’s behavior or intentional server-side validation.
The test includes assertions and will log a warning if the change doesn’t persist.
Failures in this area are considered known and documented.

---

## 🛍️ Bag Add Test (Product to Cart)

This test attempts to **navigate the site, select a product, choose a size**, and **add it to the shopping bag**.

---

### 🧪 Test Flow:

1. Navigate to **Men → New In → View All**
2. Iterate through the product list  
3. For each product:
   - Skip products marked as `Out of stock`
   - If available:
     - Select the **first valid size**
     - Click the **"Add to Bag"** button
     - Wait for a network response (`/bag` URL)
     - Assert that **no error message** is shown
4. If successful:
   - Open the bag via the mini icon
   - Assert that at least one item appears in the cart

---

### ⚙️ Technical Notes:

- Uses `.click()` wrapped with `expect_response()` to listen for `/bag` network request
- If regular click fails, a **JavaScript-based fallback** is attempted:
  ```javascript
  el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }));
  el.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
  el.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
  el.click();
  ```
- Error messages detected via:
  ```python
  page.get_by_test_id("bag-error-message")
  ```

---

### ❌ Known Issues

Adding items to the bag may fail even when everything seems correct:

- Product *appears available* but triggers a hidden server-side validation
- Site may return a `200 OK` response without actually adding the item
- `bag-error-message` may appear with no explanation
- Anti-bot mechanisms may silently interfere with the request

---

### 🔍 Debug Features

- Log messages use Unicode icons for clarity:
  - `\U0001F50D` (🔍), `\u2705` (✅), `\U0001F5B1` (🖱️), `\U0001F9EA` (🧪), `\u274C` (❌), `\U0001F6D1` (🛑), `\U0001F6CD` (🛒), `\u26A0` (⚠️)
- JS fallback added when normal click fails
- The test **fails fast** with meaningful logs and assertion

---

### ✅ Conclusion

The test simulates a full add-to-bag flow and logs failures clearly.  
However, **failure does not always mean test bug** — sometimes it's site logic or protection.

If the bag still shows empty, the test raises:
```
❌ Expected item in bag, but got 'Your bag is empty' message
```

---

## 💾 Saved Items Test

This test validates the ability to **save a product for later** and optionally **remove it** from the Saved Items list.

---

### 🧪 Test Flow:

1. Navigate to **Men → New In → View All**
2. Click on the **first product**
3. Add the product to **Saved Items**
4. Open the **Saved Items** page
5. Assert that the product is **visible** in the list
6. Remove the product from Saved Items
7. Assert that the list now displays **"You have no Saved Items"**

---

### ⚙️ Technical Notes

- Page actions and assertions are handled using Page Object Model:
  - `add_to_saved_items()`
  - `verify_add_to_saved_items()`
  - `remove_from_saved_items()`
  - `verify_remove_from_saved_items()`

- Unicode indicators are used for logging:
  - ✅ `Item successfully found in Saved Items!`
  - ✅ `Item successfully removed from Saved Items!`
  - ❌ `Item not visible in Saved Items!`
  - ❌ `Failed to remove item from Saved Items!`

- Simple and fast test, minimal risk of flakiness compared to login/cart flows

---

### ✅ Conclusion

This test verifies both adding and removing Saved Items with clear feedback.  
It can serve as a **quick sanity check** for user wishlist functionality.

---

## 📌 Additional Notes
This project will be expanded in the future to include further automation scenarios such as:

- Product search

- Checkout flow

- Responsive tests across different devices

---

## 📂 Project Structure

```bash
asos_project/
├── pages/
│   ├── bag_page.py             # Page Object for bag/cart functionality
│   ├── login_page.py           # Page Object for login functionality
│   ├── preferences_page.py     # Page Object for country & currency preferences
│   └── saved_items_page.py     # Page Object for Saved Items (wishlist)
│
├── tests/
│   ├── conftest.py             # Pytest fixtures and browser setup
│   ├── globals.py              # Test data (credentials, etc.)
│   ├── test_bag.py             # Test suite for adding products to cart
│   ├── test_login.py           # Test suite for login functionality
│   ├── test_preferences.py     # Test suite for preferences (country & currency)
│   └── test_saved_items.py     # Test suite for Saved Items functionality
│
├── README.md                   # Project documentation
└── requirements.txt            # Dependencies list
```

---

## 🙋 Author

Made with ❤️ by Yuri Kirsanov

🔗 [LinkedIn](https://www.linkedin.com/in/yuri-kirsanov/)  
🐙 [GitHub](https://github.com/RedlineQA)