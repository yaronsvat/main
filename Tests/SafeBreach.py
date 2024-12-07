import requests
from collections import defaultdict

class NewsletterSystem:
    def __init__(self, api_url):
        self.api_url = api_url
        self.users = []
        self.fetch_users()

    def fetch_users(self):
        """Fetches users from the external database and stores them in the system."""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            self.users = response.json()
            print("Users successfully fetched.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching users: {e}")
            self.users = []

    def query_users_by_email_domain(self, domain):
        """Returns a list of users with emails matching the specified domain."""
        return [user for user in self.users if user.get("email", "").split('@')[-1] == domain]

    def count_users_by_country(self):
        """Returns a dictionary with countries as keys and the count of users in each country as values."""
        country_counts = defaultdict(int)
        for user in self.users:
            country = user.get("country")
            if country:
                country_counts[country] += 1
        return dict(country_counts)


# Example usage:
if __name__ == "__main__":
    # URL to fetch users from the external API
    api_url = "https://66333084f7d50bbd9b487735.mockapi.io/api/v1/users"

    # Initialize the newsletter system
    newsletter_system = NewsletterSystem(api_url)

    # Query users by a specific email domain
    domain = "yahoo.com"
    users_with_domain = newsletter_system.query_users_by_email_domain(domain)
    print(f"Users with email domain '{domain}':", users_with_domain)

    # Get the count of users by country
    country_user_counts = newsletter_system.count_users_by_country()
    print("User count by country:", country_user_counts)
