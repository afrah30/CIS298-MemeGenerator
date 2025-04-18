import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import random

from api_fetcher.fetch_api import get_random_joke
from image_editor.meme_editor import create_meme


class MemeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meme Generator")
        self.root.geometry("900x800")
        self.root.configure(bg="#f8f8f8")

        self.template_path = None
        self.latest_meme_path = None
        self.tk_img = None
        self.current_theme = "light"

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Teal.TButton",
                        background="#8cd9c3",
                        foreground="#ffffff",
                        font=("Futura", 13, "bold"),
                        padding=(14, 10),
                        borderwidth=0)
        style.map("Teal.TButton",
                  background=[("active", "#72c5b0")])

        style.configure("Gray.TButton",
                        background="#e6e6e6",
                        foreground="#333333",
                        font=("Futura", 12, "bold"),
                        padding=(12, 8),
                        borderwidth=0)
        style.map("Gray.TButton",
                  background=[("active", "#d4d4d4")])

        top_bar = tk.Frame(root, bg="#f8f8f8")
        top_bar.pack(fill="x", anchor="n", pady=(5, 0))

        self.toggle_canvas = tk.Canvas(top_bar, width=70, height=30, bg="#f8f8f8", highlightthickness=0)
        self.toggle_canvas.pack(side="left", padx=12)

        self.toggle_bg = self.toggle_canvas.create_oval(5, 5, 65, 25, fill="#e6e6e6", outline="")
        self.toggle_circle = self.toggle_canvas.create_oval(5, 5, 35, 25, fill="#ffffff", outline="")
        self.sun_icon = self.toggle_canvas.create_text(57, 15, text="☀️", font=("Futura", 10))
        self.moon_icon = self.toggle_canvas.create_text(13, 15, text="🌙", font=("Futura", 10))

        self.toggle_canvas.bind("<Button-1>", self.animate_toggle)

        self.content_frame = tk.Frame(root, bg="#f8f8f8")
        self.content_frame.pack(expand=True)

        self.title_label = tk.Label(self.content_frame, text="MEMEIFY",
                                    font=("Impact", 32, "bold"),
                                    bg="#f8f8f8", fg="#222222")
        self.title_label.pack(pady=(30, 15))

        self.caption_label = tk.Label(self.content_frame,
                                      text="Enter a caption (or leave blank for a random joke):",
                                      font=("Futura", 14),
                                      bg="#f8f8f8", fg="#444444")
        self.caption_label.pack(pady=(10, 5))

        self.quote_entry = tk.Entry(self.content_frame, font=("Futura", 12),
                                    width=70, bd=1, relief="solid",
                                    bg="#ffffff", fg="#000000", insertbackground="#000000")
        self.quote_entry.pack(ipady=6, pady=(0, 20))

        ttk.Button(self.content_frame, text="🖼️  Choose Meme Template", style="Gray.TButton",
                   command=self.choose_template).pack(pady=5)

        ttk.Button(self.content_frame, text="🎲  Use Random Template", style="Gray.TButton",
                   command=self.use_random_template).pack(pady=5)

        self.preview_label = tk.Label(self.content_frame, bg="#f8f8f8")
        self.preview_label.pack(pady=10)

        ttk.Button(self.content_frame, text="📤  Create Meme", style="Teal.TButton",
                   command=self.generate_meme).pack(pady=(5, 10))

        ttk.Button(self.content_frame, text="💾  Save Meme As...", style="Gray.TButton",
                   command=self.save_meme_as).pack()

        self.footer_label = tk.Label(self.content_frame,
                                     text="Built with 💖 using Python + Tkinter",
                                     font=("Futura", 10),
                                     bg="#f8f8f8", fg="#999999")
        self.footer_label.pack(pady=30)

    def animate_toggle(self, event=None):
        if self.current_theme == "light":
            for _ in range(15):
                self.toggle_canvas.move(self.toggle_circle, 2, 0)
                self.toggle_canvas.update()
                self.toggle_canvas.after(5)
            self.toggle_canvas.itemconfig(self.toggle_bg, fill="#444")
            self.toggle_theme()
        else:
            for _ in range(15):
                self.toggle_canvas.move(self.toggle_circle, -2, 0)
                self.toggle_canvas.update()
                self.toggle_canvas.after(5)
            self.toggle_canvas.itemconfig(self.toggle_bg, fill="#e6e6e6")
            self.toggle_theme()

    def toggle_theme(self):
        if self.current_theme == "light":
            self.root.configure(bg="#1e1e2f")
            self.content_frame.configure(bg="#1e1e2f")
            self.title_label.configure(bg="#1e1e2f", fg="#ffffff")
            self.caption_label.configure(bg="#1e1e2f", fg="#dddddd")
            self.quote_entry.configure(bg="#2a2a3d", fg="#ffffff", insertbackground="#ffffff")
            self.preview_label.configure(bg="#1e1e2f")
            self.footer_label.configure(bg="#1e1e2f", fg="#888888")
            self.current_theme = "dark"
        else:
            self.root.configure(bg="#f8f8f8")
            self.content_frame.configure(bg="#f8f8f8")
            self.title_label.configure(bg="#f8f8f8", fg="#222222")
            self.caption_label.configure(bg="#f8f8f8", fg="#444444")
            self.quote_entry.configure(bg="#ffffff", fg="#000000", insertbackground="#000000")
            self.preview_label.configure(bg="#f8f8f8")
            self.footer_label.configure(bg="#f8f8f8", fg="#999999")
            self.current_theme = "light"

    def choose_template(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if path:
            self.template_path = path
            self.show_image(path)

    def use_random_template(self):
        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
        if not os.path.exists(template_dir):
            messagebox.showerror("Error", "No 'templates/' folder found!")
            return

        image_files = [f for f in os.listdir(template_dir)
                       if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        if not image_files:
            messagebox.showerror("Error", "No image templates found in the folder.")
            return

        chosen_file = random.choice(image_files)
        path = os.path.join(template_dir, chosen_file)
        self.template_path = path
        self.show_image(path)

    def show_image(self, path):
        img = Image.open(path).resize((400, 300))
        self.tk_img = ImageTk.PhotoImage(img)
        self.preview_label.configure(image=self.tk_img)
        self.preview_label.image = self.tk_img

    def fetch_quote(self):
        return get_random_joke()

    def generate_meme(self):
        if not self.template_path:
            messagebox.showwarning("Missing Template", "Please select a meme template first!")
            return

        quote = self.quote_entry.get()
        if not quote:
            quote = self.fetch_quote()

        try:
            os.makedirs("output", exist_ok=True)
            output_path = os.path.join("output", "generated_meme.jpg")
            create_meme(self.template_path, quote, out_path=output_path)
            self.latest_meme_path = output_path

            self.show_image(output_path)
            messagebox.showinfo("Success", "Meme generated successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate meme:\n{str(e)}")

    def save_meme_as(self):
        if not self.latest_meme_path or not os.path.exists(self.latest_meme_path):
            messagebox.showwarning("No Meme", "Please generate a meme first!")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[("JPEG image", "*.jpg"), ("PNG image", "*.png")],
            title="Save Meme As"
        )

        if save_path:
            try:
                img = Image.open(self.latest_meme_path)
                img.save(save_path)
                messagebox.showinfo("Success", f"Meme saved to:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save meme:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MemeGeneratorApp(root)
    root.mainloop()
