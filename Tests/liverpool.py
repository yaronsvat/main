# tests/liverpool.py
from time import sleep
from tipalti.sync_api import sync_playwright


def checkPlayersScreens(trying_playwright):
    players = ["Alisson Becker", "Vitezslav Jaros", "Joe Gomez", "Dominik Szoboszlai"]
    browser = trying_playwright.chromium.launch(headless=False)
    page = browser.new_page()
    def handle_dialog(dialog):
        print(f"Dialog message: {dialog.message}")
        if dialog.type == 'alert':
            dialog.accept()  # Accept the alert
        elif dialog.type == 'confirm':
            dialog.dismiss()  # Dismiss the confirmation
    page.on('dialog', handle_dialog)
    page.goto("https://www.liverpoolfc.com")
    cookie_button_selector = "text=Accept All Cookies"
    page.wait_for_selector(cookie_button_selector)
    try:
        if page.is_visible(cookie_button_selector):
            page.keyboard.press("Tab")
            page.keyboard.press("Enter")
    except Exception as e:
        print("Error clicking button:", e)
    page.wait_for_selector("text=Fixtures & Teams")
    if page.is_visible("text=Fixtures & Teams"):
        page.hover("text=Fixtures & Teams")
    page.wait_for_selector("text=Players & Staff")
    if page.is_visible("text=Players & Staff"):
        page.click("text=Players & Staff")
    dialog_selector = '.wp-optin-dialog-container'  # Adjust the selector if needed
    page.wait_for_selector(dialog_selector, state='visible', timeout=5000)
    for player in players:
        page.wait_for_selector("text={0}".format(player))
        if page.is_visible("text={0}".format(player)):
            page.click("text={0}".format(player))
        index = 0
        temp=""
        for char in player:
            if char == " ":
                temp=temp+"-"
            else:
                temp=temp+char.lower()
                index+=1
        player=temp
        sleep(120)
        current_url = page.url
        expected_url = "https://www.liverpoolfc.com/team/mens/player/{0}".format(player)
        assert current_url == expected_url, f"Expected URL '{expected_url}', but got '{current_url}'"
        page.screenshot(path="{0}.png".format(player))
        print("Enter {0} screen".format(player))
        page.go_back()
    browser.close()

with sync_playwright() as trying_playwright:
    checkPlayersScreens(trying_playwright)


"Would you like LFC to send you Notifications?"

