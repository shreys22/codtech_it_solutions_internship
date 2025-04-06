import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Constants

CSV_FILE = "task1\\test_data.csv"
# Set up WebDriver
driver = webdriver.Chrome()

# Function to log result
def log_result(username, result):
    with open("test_results.log", "a") as log_file:
        log_file.write(f"Username: {username} - Result: {result}\n")

# Read CSV and perform login tests
with open(CSV_FILE, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        username = row['username']
        password = row['password']

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(3)  # Wait for the page to load

        try:
            # Locate username and password fields
            driver.find_element(By.NAME, "username").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys(password)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Login button

            time.sleep(4)  # Wait for login to process

            # Check login success by checking the presence of the dashboard
            if "dashboard" in driver.current_url.lower():
                log_result(username, "Login Successful")
            else:
                log_result(username, "Login Failed")

        except NoSuchElementException as e:
            log_result(username, f"Error: {str(e)}")

# Close the browser
driver.quit()

print("✅ Test complete. Check 'test_results.log' for results.")
