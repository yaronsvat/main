from tipalti.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    # Assert the title of the page
    assert page.title() == "Example Domain", "Title did not match"

    browser.close()


with sync_playwright() as playwright:
    run(playwright)