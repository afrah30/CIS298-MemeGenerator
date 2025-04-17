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
import argparse
import os
from datetime import datetime
from image_editor.meme_editor import create_meme
def main():
    parser = argparse.ArgumentParser(description="Generate a meme from the CLI")
    parser.add_argument(
        "--template",
        help="Path to your meme template image (jpg/png)",
        required=True,
    )
    parser.add_argument(
        "--text",
        help="Text for the meme (omit for random joke)",
        default=None
    )
    parser.add_argument(
        "--out",
        help="Output filename",
        default="out.jpg"
    )
    parser.add_argument("--font-size", type=int, default=48, help="Base font size")
    parser.add_argument("--stroke-width", type=int, default=2, help="Outline thickness")
    parser.add_argument("--color", type=str, default="white", help="Text color")
    parser.add_argument("--position", type=str, choices=["top", "bottom"], default="top",
                        help="Where to place the text")

    args = parser.parse_args()
    # Determine actual out_path
    if args.out == "out.jpg":
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = f"meme_{ts}.jpg"
    else:
        out_path = args.out

    # validate that the template exists
    if not os.path.isfile(args.template):
        print(f"Error: template file not found: {args.template}")
        exit(1)

    caption = args.text or get_random_joke()

    img = create_meme(
        args.template,
        caption,
        font_size = args.font_size,
        text_color = args.color,
        stroke_color = args.color,  # if you want stroke same as text
        stroke_width = args.stroke_width,  # ← now supported
        position = args.position,
        out_path = out_path
              )
    print(f"Meme saved to {out_path}")

if __name__ == "__main__":
    main()
##def main():
   ## print("Welcome to Meme Generator!")

    # Afrah: Testing the API fetcher by calling the function to get a random joke
  ##  fetched_joke = get_random_joke()  # this will fetch the joke from the API

##if __name__ == "__main__":
   # main()
