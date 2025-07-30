# 🧪 ASOS Automation Project

This project is a UI test automation framework for the **login functionality** of the ASOS website using **Python** and **Playwright**.

---

## 🎯 Project Goals

- Automate login flow for an existing user
- Validate multiple negative login scenarios (invalid email, unregistered email, wrong password)
- Demonstrate usage of **Playwright** with **Pytest** and **Page Object Model (POM)**
- Handle real-world anti-bot mechanisms and dynamic web behavior

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
- Add small delays between actions (e.g. ```python await page.wait_for_timeout(1000)```).
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

## 📌 Additional Notes
This project will be expanded in the future to include further automation scenarios such as:

Product search

Cart management

Checkout flow

Responsive tests across different devices