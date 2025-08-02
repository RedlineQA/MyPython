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

## 💱 Currency Preference Test

This test ensures that changing the user's currency preference to **USD ($)** is reflected both:

- In the **dropdown selection UI**
- In the **pricing of actual listed products**

---

### 🧪 Test Flow:

1. Open preferences modal  
2. Change currency using `select_option("#currency", value="2")`  
3. Click **UPDATE PREFERENCES**  
4. Re-open modal and assert `$ USD` is selected  
5. Navigate to product list  
6. Extract first product price  
7. Assert currency symbol is `$` or `USD`

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

This is assumed to be a **bug in the website’s behavior** or **intentional server-side validation**.  
The test includes assertions and will log a warning if the change doesn’t persist.

---

## 📌 Additional Notes
This project will be expanded in the future to include further automation scenarios such as:

- Product search

- Cart management

- Checkout flow

- Responsive tests across different devices

---

## 📂 Project Structure

```python
asos_project/
├── pages/
│   ├── login_page.py          # Page Object for login functionality
│   └── preferences_page.py    # Page Object for user preferences (currency)
├── tests/
│   ├── test_login.py          # Test suite for login scenarios
│   └── test_preferences.py    # Test suite for currency preferences
├── globals.py                 # Test data (e.g. valid/invalid credentials)
└── conftest.py                # Pytest fixtures and setup
```

---

## 🙋 Author
Made with ❤️ by Yuri Kirsanov
🔗 [LinkedIn](https://www.linkedin.com/in/yuri-kirsanov/)  
🐙 [GitHub](https://github.com/RedlineQA)