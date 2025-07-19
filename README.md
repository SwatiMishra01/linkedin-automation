# 🔗 LinkedIn Automation Bot

Automate your LinkedIn tasks with ease using this Python-based Selenium bot.  
This script logs into your LinkedIn account and performs actions like sending connection requests automatically.

---

## 🚀 Features

- Logs into your LinkedIn account securely
- Sends connection requests
- Headless browser automation using Selenium
- Keeps credentials safe using `.env` file

---

## ⚙️ Tech Stack

- Python
- Selenium
- `python-dotenv`
- Chrome WebDriver

---

## 🔐 Setup Instructions

---

### 1. Clone the Repository

```bash
git clone https://github.com/SwatiMishra01/linkedin-automation.git
cd linkedin-automation
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Set Up Your .env File
```bash
LINKEDIN_EMAIL=your-email@gmail.com
LINKEDIN_PASSWORD=your-password
```
⚠️ Do not share this file publicly! Your .env file should be listed in .gitignore.

### 4. Find Your Chrome Profile Path
```bash
Start-Process "chrome.exe" -ArgumentList '--user-data-dir="C:\Users\<YOUR USERNAME>\AppData\Local\Google\Chrome\User Data"', '--profile-directory="<PROFILE>"'

```
### 5. Run the Bot
```bash
python main.py

```
