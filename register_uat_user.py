from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://user.m-key.uat/mkey2088/login.html")
    # page.get_by_role("button", name="Advanced").click()
    # page.locator("#final-paragraph").click()
    # page.get_by_role("link", name="Proceed to admin.m-key.uat (unsafe)").click()
    page.locator("section div").filter(has_text="Register").nth(4).click()
    page.get_by_role("link", name="Register").click()
    page.get_by_placeholder("name@example.com").click()
    page.get_by_placeholder("name@example.com").fill("yenlingchng@gmail.com")
    page.locator("#register-account-name").click()
    page.locator("#register-account-name").fill("m0_user")
    page.locator("#register-password").click()
    page.locator("#register-password").fill("Ease@123")
    page.locator("#register-confirmPassword").click()
    page.locator("#register-confirmPassword").fill("Ease@123")
    page.get_by_role("button", name="Register").click()
    time.sleep(5)
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
