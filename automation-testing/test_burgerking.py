from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)  # opens Chrome/Chromium
    page = browser.new_page()
    page.goto("https://www.burgerking.co.za")
    print("✅ Page title:", page.title())
    input("Press Enter to close browser...")  # waits so browser doesn’t close immediately
    browser.close()
