# this module fetches a random joke from the Humor API.
# this module will return a clean string to be used by the meme generator.

import requests

API_KEY = "13efbda6ccd6448a850d1fe1a06b8298" # API key from our humorapi account


def get_random_joke():
    url = "https://api.humorapi.com/jokes/random"
    params = {
        "api-key": API_KEY,
        "max-length": 150  # this will keep jokes meme-friendly
    }

    try:
        print("Sending request to Humor API...")  # the debugging print
        response = requests.get(url, params=params)

        # check if the response status is sucessful
        response.raise_for_status()
        print(f"Received response with status code: {response.status_code}")  # Debugging print

        data = response.json()

        # debugging: print the whole response data to inspect it
        print("Response JSON:", data)

        # return the joke or a fallback message
        joke = data.get("joke", "No joke found.")
        print(f"Fetched Joke: {joke}")  # Debugging print
        return joke
    except requests.RequestException as e:
        print("Error fetching joke:", e)
        return "Error getting a joke!"
