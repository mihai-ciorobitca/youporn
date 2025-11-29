# 📌 YouPorn Account Automation – QA Portfolio Project

This project is part of my **QA Automation Engineering portfolio**.  
It demonstrates my ability to build **complex, end-to-end automated flows** using **Playwright**, including:

- UI automation  
- Modal handling  
- Email verification  
- Screenshot capture  
- Workflow execution  

The automation interacts with **https://www.youporn.com** to simulate a **realistic multi-step registration flow** for testing purposes.

⚠️ **Disclaimer:**  
This project is for **portfolio and educational purposes only**.  
It is **not** intended to bypass security, create real accounts, or violate Terms of Service.

---

## 🧭 Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [QA Skills Demonstrated](#qa-skills-demonstrated)  
- [Project Structure](#project-structure)  
- [How It Works](#how-it-works)  
- [Example Code Snippet](#example-code-snippet)  
- [Installation](#installation)  
- [Running the Script](#running-the-script)  
- [Ethical Notice](#ethical-notice)  
- [Limitations](#limitations)  
- [Future Enhancements](#future-enhancements)  

---

## 📌 Overview

This script automates the **signup, email verification, and login workflow** on YouPorn.com.  
Key capabilities:

- Fill registration forms  
- Handle modals and overlays  
- Accept cookie banners  
- Capture screenshots after signup  
- Observe workflow execution  

---

## ✨ Features

- **Automated sign-up workflow**  
- **Email verification handling**  
- **TOS + age modal automation**  
- **Sign-in workflow**  
- **Screenshot capture**  
- **Async Playwright browser management**  

---

## 🧪 QA Skills Demonstrated

- End-to-end UI automation  
- Handling modals and overlays  
- Dynamic locator handling  
- Asynchronous browser management  
- Error recovery and exception handling  
- Debugging with screenshots  
- Working with real-world dynamic UIs  

---

## 📂 Project Structure

/project
├─ browser_manager.py

├─ utils.py

├─ main.py

├─ screenshots/

└─ README.md

---

## 📝 How It Works

### **1. Sign-Up Flow**
1. Navigate to YouPorn homepage  
2. Handle age confirmation and cookie banners  
3. Open registration form  
4. Fill in email and password  
5. (Optional) Retrieve email verification code via `get_verification_code()`  
6. Input code into verification fields  
7. Handle DOB and TOS modals  
8. Capture final screenshot  

### **2. Sign-In Flow**
1. Navigate to homepage  
2. Handle overlays and cookie banners  
3. Enter credentials  
4. Handle TOS or DOB modals if shown  
5. Confirm login via profile menu  

---

## 💻 Example Code Snippet

```
async def sign_up(page, username, password):
    await page.goto("https://www.youporn.com/")

    # Handle age confirmation
    age_button = page.locator("#accessButton")
    try:
        await age_button.click()
    except:
        print("Age button not found or already handled.")

    # Accept cookies
    await page.evaluate("""
        const btn = document.querySelector('#consent_accept_all');
        if (btn) btn.click();
    """)

    # Navigate to registration
    await page.goto("https://www.youporn.com/register")
    await page.locator("#registration_email").fill(username)
    await page.locator("#registration_password").fill(password)

    # Screenshot after signup
    await page.screenshot(path=f"screenshots/{username}_screenshot.png")
```

### ⚙️ Installation

```
pip install playwright
playwright install
```

### ▶️ Running the Script

```
python main.py
```
Screenshots will be saved to:

```
/screenshots/<username>_screenshot.png
```

## ⚠️ Ethical Notice

This repository is strictly for portfolio and educational purposes.
All accounts used are test accounts; no real user data is involved.
This script must not be used to bypass security measures or create real accounts.

## ⚠️ Limitations

Due to reCAPTCHA protection, multiple registrations or logins cannot be fully automated.
The script demonstrates flow handling but cannot bypass anti-bot measures on the site.

## 🚀 Future Enhancements

- Logging system
- HTML/Allure reports
- Selector abstraction layer
- Parallel execution
- Mailbox provider swapping
- UI flow visualization