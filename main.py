from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
# Toggle mutual filter here
USE_MUTUAL_FILTER = False  # Set to False to accept ALL
MIN_MUTUALS = 5  # Minimum mutuals required if filter is ON

# Setup Chrome options (without profile)
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Step 1: Go to LinkedIn login page
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)

    # Step 2: Enter email
    email_input = driver.find_element(By.ID, "username")
    email_input.clear()
    email_input.send_keys(LINKEDIN_EMAIL)

    # Step 3: Enter password
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(LINKEDIN_PASSWORD)

    # Step 4: Click login button
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    time.sleep(5)  # Wait for login to complete

    # Step 5: Navigate to invitations page
    driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
    time.sleep(5)

    # Step 6: Scroll to load more invitations
    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Step 7: Find all Accept buttons
    accept_buttons = driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Accept")]')

    print(f"🔍 Total requests found: {len(accept_buttons)}")
    accepted_count = 0

    # Step 8: Loop and apply filter if enabled
    for btn in accept_buttons:
        try:
            parent = btn.find_element(By.XPATH, "./../../..")

            if USE_MUTUAL_FILTER:
                text = parent.text.lower()
                mutual_count = 0
                if "mutual connection" in text:
                    for word in text.split():
                        if word.isdigit():
                            mutual_count = int(word)
                            break

                if mutual_count >= MIN_MUTUALS:
                    btn.click()
                    accepted_count += 1
                    print(f"✅ Accepted (Mutuals: {mutual_count})")
                    time.sleep(1)
                else:
                    print(f"⛔ Skipped (Mutuals: {mutual_count})")
            else:
                btn.click()
                accepted_count += 1
                print("✅ Accepted (No filter)")
                time.sleep(1)

        except Exception as e:
            print("⚠️ Error:", e)

    print(f"\n🎉 Done! Total accepted: {accepted_count}")

finally:
    driver.quit()
