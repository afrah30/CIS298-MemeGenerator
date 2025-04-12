# main.py
# This is where everything comes together once we start working on our assigned parts.

# We'll import our different modules here once they're ready.
# Right now they're commented out because we don't have the code yet.

# From the API fetcher
# from api_fetcher.fetch_api import get_random_joke  # Will get a random joke/quote from the API

# From the image editor
# from image_editor.meme_editor import create_meme  # Will take the quote and add it to a meme template

# From the GUI/CLI
# from gui.interface import run_interface  # Will create the user interface (either GUI or CLI)

# main.py
from api_fetcher.fetch_api import get_random_joke  # Import the function from fetch_api


def main():
    print("Welcome to Meme Generator!")

    # Afrah: Testing the API fetcher by calling the function to get a random joke
    fetched_joke = get_random_joke()  # this will fetch the joke from the API

if __name__ == "__main__":
    main()
