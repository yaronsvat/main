from playwright.sync_api import sync_playwright


def test_homepage(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://qa-tipalti-assignment.tipalti-pg.com/index.html")
    page.click('nav ul li a[href="#menu"]')
    menu_items = page.locator('#menu ul li a')
    names = menu_items.all_inner_texts()
    assert "Kika" in names, f"Expected that Kika will be on the menu but it doesn't"
    page.click('nav#menu ul li a[href="kika.html"]')
    page.fill('input#name', 'Yaron Svatitzky')
    page.fill('input#email', 'yaron.svatitzky@gmail.com')
    page.fill('textarea#message', 'Hello, this is a test message.')
    page.click('input[type="submit"]')


with sync_playwright() as playwright:
    test_homepage(playwright)