# 🔐 Automated Login Test with Selenium (Python)

This project automates the login functionality of a web application using **Selenium WebDriver** and **Python's `unittest` framework**.

---

## 🌐 Demo Site

> https://practicetestautomation.com/practice-test-login/

---

## ✅ Features

- Automated browser-based tests using **Chrome**
- Tests for:
  - Valid credentials ✅
  - Invalid password ❌
  - Invalid username ❌
  - Empty username ❌
  - Empty password ❌
  - Both fields empty ❌

---

---

## ⚙️ Setup Instructions

### 1. 🔽 Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/login-automation-test.git
cd login-automation-test




### 2.📦 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt



🚀 Run Tests
▶️ Option 1: Run All Tests from Test File

python tests/test_login.py

▶️ Option 2: Run via run_tests.py

python run_tests.py




📚 Technologies Used
Python 3.x

Selenium

ChromeDriver

unittest (built-in Python testing framework)


📝 Author
Sheeza Raheem

📌 Notes
Make sure chromedriver is installed and in your system PATH.

If you prefer to include it locally, place it in a drivers/ folder and reference the path like:

self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver")


✅ Example Test Case

def test_valid_login(self):
    self.driver.find_element(By.ID, "username").send_keys("student")
    self.driver.find_element(By.ID, "password").send_keys("Password123")
    self.driver.find_element(By.ID, "submit").click()
    self.assertIn("Logged In Successfully", self.driver.page_source)





Happy Testing! 🎉









