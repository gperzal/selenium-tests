from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import platform

# Start timer
start_time = time.time()

# Brave browser configuration
options = Options()
system = platform.system()

if system == "Windows":
    options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    options.add_argument("--start-maximized")
else:
    options.binary_location = "/usr/bin/brave-browser"
    options.add_argument("--start-maximized")
    #options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--user-data-dir=/tmp/brave-user-data-{os.getpid()}")

# Launch ChromeDriver (expects it to be in PATH)
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://duckduckgo.com")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.ID, "searchbox_input"))
    )

    search_box.send_keys("DevOps testing")
    search_box.send_keys(Keys.RETURN)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".results--main")))

    # Try multiple selectors for result titles
    results = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")
    if not results:
        results = driver.find_elements(By.CSS_SELECTOR, ".result__title a")

    print(f"\n🔎 Results found: {len(results)}")

    if len(results) == 0:
        # Save page HTML for debugging
        with open("page_debug.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("⚠️ No results found. HTML saved to 'page_debug.html'")

    assert len(results) > 0

    # Print result titles
    for i, r in enumerate(results, start=1):
        print(f"{i}. {r.text.strip()}")

    # Save results to file
    with open("results.txt", "w", encoding="utf-8") as f:
        for r in results:
            f.write(r.text.strip() + "\n")

    print("\n📄 Results saved to 'results.txt'")

    # Take screenshot of the final state
    os.makedirs("screenshots", exist_ok=True)
    screenshot_path = os.path.join("screenshots", "results.png")
    driver.save_screenshot(screenshot_path)
    print(f"🖼️ Screenshot saved to '{screenshot_path}'")

    print("✅ Functional test completed successfully.")

finally:
    driver.quit()
    duration = time.time() - start_time
    print(f"⏱ Total execution time: {duration:.2f} seconds")
