import requests
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import datetime
import pytest

# 1. API Interaction - Fetch episodes and characters
base_url = "https://rickandmortyapi.com/api"

# Fetch all episodes
episodes_url = f"{base_url}/episode"
response = requests.get(episodes_url)
episodes = response.json()['results']

# Randomly choose one episode with >= 30 characters
selected_episode = None
while selected_episode is None:
    episode = random.choice(episodes)
    if len(episode['characters']) >= 30:
        selected_episode = episode

# Print episode details
print(f"Selected Episode: {selected_episode['name']}")
print(f"Number of characters: {len(selected_episode['characters'])}")

# Randomly select two characters
characters = random.sample(selected_episode['characters'], 2)

# Fetch character details and create character objects
class Character:
    def __init__(self, id, name, status, species, location):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.location = location

characters_objects = []
for char_url in characters:
    char_data = requests.get(char_url).json()
    char = Character(
        id=char_data['id'],
        name=char_data['name'],
        status=char_data['status'],
        species=char_data['species'],
        location=char_data['location']['name']
    )
    characters_objects.append(char)

# Write introductions to file
with open("characters_introduction.txt", "w") as f:
    for char in characters_objects:
        f.write(f"Hi! I'm {char.name}, My ID is {char.id}, I'm from {char.location}, etc.\n")

# 2. UI Automation - Search for characters and take screenshots
def calculate_image_position(character_id):
    if character_id < 10:
        return character_id  # Single-digit ID
    return (character_id // 10) + (character_id % 10)  # Hundreds + Ones digit

# Pytest setup to start the browser
@pytest.fixture(scope="module")
def setup_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()  # Maximize the window
    driver.get("https://www.google.com")
    yield driver  # Yield the driver to the test
    driver.quit()  # Quit the driver after the test

def test_api_and_ui_integration(setup_browser):
    driver = setup_browser

    # Use the character data from API interaction
    first_character = characters_objects[0]
    second_character = characters_objects[1]

    # Step 1: Search for the first character on Google
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(f"Rick and Morty {first_character.name}")
    search_box.send_keys(Keys.RETURN)  # Press enter to search
    time.sleep(2)  # Wait for the search results

    # Step 2: Navigate to Google Images
    images_link = driver.find_element(By.LINK_TEXT, "Images")
    images_link.click()
    time.sleep(2)  # Wait for the images to load

    # Step 3: Calculate the position of the first character's image
    position = calculate_image_position(first_character.id)
    print(f"Calculated image position for {first_character.name}: {position}")

    # Step 4: Select the image by position
    image = driver.find_elements(By.XPATH, f"//div[@data-q]")[position - 1]  # Subtract 1 to align with 0-based index
    image.click()

    # Take a screenshot of the first character's image
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"{first_character.name}-{first_character.id}-{timestamp}.jpg"
    image.screenshot(screenshot_filename)

    # Step 5: Now search for the second character and repeat the process
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()  # Clear the previous search
    search_box.send_keys(f"Rick and Morty {second_character.name}")
    search_box.send_keys(Keys.RETURN)  # Press enter to search
    time.sleep(2)  # Wait for the search results

    # Navigate to Google Images again
    images_link = driver.find_element(By.LINK_TEXT, "Images")
    images_link.click()
    time.sleep(2)  # Wait for the images to load

    # Calculate the position of the second character's image
    position = calculate_image_position(second_character.id)
    print(f"Calculated image position for {second_character.name}: {position}")

    # Select the image for the second character
    image = driver.find_elements(By.XPATH, f"//div[@data-q]")[position - 1]  # Subtract 1 to align with 0-based index
    image.click()

    # Take a screenshot of the second character's image
    screenshot_filename = f"{second_character.name}-{second_character.id}-{timestamp}.jpg"
    image.screenshot(screenshot_filename)

    # Step 6: Verify that the locations of the characters match
    if first_character.location == second_character.location:
        print(f"Both characters are from {first_character.location}.")
    else:
        print(f"{first_character.name} from {first_character.location} and {second_character.name} from {second_character.location}.")

    # Clean up: Close the browser
    driver.quit()
