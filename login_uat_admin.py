from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://admin.m-key.uat/mkey2088/login.html")
    # page.goto("chrome-error://chromewebdata/")
    # page.get_by_role("button", name="Advanced").click()
    # page.get_by_role("link", name="Proceed to admin.m-key.uat (unsafe)").click()
    page.get_by_placeholder("name@example.com").click()
    page.get_by_placeholder("name@example.com").fill("yenling.cheng.mg08@nycu.edu.tw")
    page.locator("#login-password").click()
    page.locator("#login-password").fill("Ease@123")
    page.get_by_role("button", name="Log In").click()
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
