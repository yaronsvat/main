from playwright.sync_api import sync_playwright

class EshAuthTester:
    def __init__(self, login_url, user_email, user_password):
        self.login_url = login_url
        self.user_email = user_email
        self.user_password = user_password
        self.browser_instance = None
        self.context_instance = None
        self.page_instance = None

    def initialize_browser(self):
        """Initialize the browser and create a new page context."""
        playwright = sync_playwright().start()
        self.browser_instance = playwright.chromium.launch(headless=True)
        self.context_instance = self.browser_instance.new_context()
        self.page_instance = self.context_instance.new_page()
        print("Browser has been launched successfully.")

    def check_login_elements(self):
        """Verify that all required login page elements are available."""
        self.page_instance.goto(self.login_url)

        # Locate login elements
        email_field = self.page_instance.locator('[data-testid="text-field-email-input"] input')
        password_field = self.page_instance.locator('[data-testid="text-field-password-input"] input')
        login_button = self.page_instance.locator('[data-testid="bo-dsm-common-button-contained-submit"]')

        # Wait for elements to load
        self.page_instance.wait_for_selector('[data-testid="text-field-email-input"]', timeout=10000)
        self.page_instance.wait_for_selector('[data-testid="text-field-password-input"]', timeout=10000)

        # Check visibility
        if not email_field.is_visible() or not password_field.is_visible() or not login_button.is_visible():
            raise Exception("One or more login elements are not visible on the page.")
        print("All login elements are visible and ready.")

    def attempt_login(self):
        """Attempt to log in using provided credentials."""
        email_field = self.page_instance.locator('[data-testid="text-field-email-input"] input')
        password_field = self.page_instance.locator('[data-testid="text-field-password-input"] input')
        login_button = self.page_instance.locator('[data-testid="bo-dsm-common-button-contained-submit"]')

        # Fill in credentials
        email_field.fill(self.user_email)
        password_field.fill(self.user_password)
        login_button.click()
        print(f"Login attempt made with email: {self.user_email}")

    def close_browser(self):
        """Close the browser instance."""
        if self.browser_instance:
            self.browser_instance.close()
            print("Browser session closed.")

if __name__ == "__main__":
    # Esh-specific login test details
    esh_login_url = "https://web.eos.bnk-il.com/auth"
    sample_email = "john_doe@company.con"
    sample_password = "123456"

    # Create an instance of the tester class and execute the test
    esh_tester = EshAuthTester(esh_login_url, sample_email, sample_password)

    try:
        esh_tester.initialize_browser()
        esh_tester.check_login_elements()
        esh_tester.attempt_login()
    finally:
        esh_tester.close_browser()
