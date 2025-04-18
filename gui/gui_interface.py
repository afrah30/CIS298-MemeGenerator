import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os

# Import custom modules
from api_fetcher.fetch_api import get_random_joke
from image_editor.meme_editor import create_meme

class MemeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meme Generator")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")

        self.template_path = None

        # Title
        tk.Label(root, text="Meme Generator", font=("Helvetica", 20, "bold"), bg="#f0f0f0").pack(pady=10)

        # Template Selector
        tk.Button(root, text="Choose Meme Template", command=self.choose_template).pack(pady=5)

        # Quote Input
        tk.Label(root, text="Enter Quote (or leave blank to fetch one):", bg="#f0f0f0").pack(pady=5)
        self.quote_entry = tk.Entry(root, width=70)
        self.quote_entry.pack(pady=5)

        # Generate Button
        tk.Button(root, text="Generate Meme", command=self.generate_meme).pack(pady=10)

        # Image Preview
        self.preview_label = tk.Label(root, bg="#f0f0f0")
        self.preview_label.pack(pady=10)

    def choose_template(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if path:
            self.template_path = path
            img = Image.open(path).resize((400, 300))
            img = ImageTk.PhotoImage(img)
            self.preview_label.configure(image=img)
            self.preview_label.image = img

    def fetch_quote(self):
        return get_random_joke()

    def generate_meme(self):
        if not self.template_path:
            messagebox.showwarning("Template Missing", "Please select a meme template image first.")
            return

        quote = self.quote_entry.get()
        if not quote:
            quote = self.fetch_quote()

        try:
            output_path = os.path.join("output", "generated_meme.jpg")
            os.makedirs("output", exist_ok=True)

            # Call create_meme from image_editor
            img = create_meme(self.template_path, quote, out_path=output_path)

            # Display in GUI
            img = img.resize((400, 300))
            img = ImageTk.PhotoImage(img)
            self.preview_label.configure(image=img)
            self.preview_label.image = img

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate meme:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemeGeneratorApp(root)
    root.mainloop()
