# 🧪 ASOS Automation Project

This project is a UI test automation framework for the **login functionality** of the ASOS website using **Python** and **Playwright**.

---

## 🎯 Project Goals

- Automate login flow for an existing user
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

Due to **ASOS's bot protection mechanisms**, login attempts may occasionally fail even with correct credentials.  
This is likely caused by **server-side anti-automation measures**, including:

- Bot detection
- Rate limiting
- Temporary blocking

✅ **Recommendation**:  
If login fails without clear reason, wait a few minutes and try again.

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