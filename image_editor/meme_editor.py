import textwrap
import PIL
from PIL import Image, ImageDraw, ImageFont
import os
def wrap_text(
    text: str,
    font: ImageFont.FreeTypeFont,
    draw: ImageDraw.Draw,
    max_width: int
) -> str:
    """
    Breaks `text` into lines so each line’s pixel width (when drawn
    with `font`) does not exceed `max_width`. Returns a single string
    with '\n' between lines.
    """
    words = text.split()
    lines = []
    current = ""

    for word in words:
        test_line = f"{current} {word}".strip()
        # measure the bounding box of the line
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]  # width = right - left

        if w <= max_width:
            current = test_line
        else:
            # commit the previous line, start a new one
            lines.append(current)
            current = word

    if current:
        lines.append(current)

    return "\n".join(lines)


def create_meme(
    template_path: str,
    text: str,
    font_path: str = os.path.join(os.path.dirname(__file__), "..", "fonts", "impact.ttf"),
    font_size: int = 48,
    text_color: str = "white",
    stroke_color: str = "black",
    stroke_width: int = 2,
    position: str = "top",
    out_path: str | None = None
) -> Image.Image:
    img  = Image.open(template_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    W, H = img.size

    # Load font
    font = ImageFont.truetype(font_path, font_size)

    # Determine text area width (e.g. leave 20px margin either side)
    max_text_width = W - 40

    # Wrap the text
    wrapped = wrap_text(text, font,draw, max_text_width)
    # shrink the font until the text block fits
    while True:
        # measure the bounding box of the wrapped text
        bbox = draw.multiline_textbbox((0, 0), wrapped, font=font, align="center")
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        # if it fits within margins, or font_size is already very small, stop
        if text_w <= W - 40 and text_h <= H / 2 or font_size < 12:
            break

        # otherwise, shrink font and re-wrap
        font_size -= 2
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font not found at: {font_path}")

        font = ImageFont.truetype(font_path, font_size)
        wrapped = wrap_text(text, font, draw, max_text_width)

    # Choose y‑coordinate based on position
    if position == "top":
        y = 10
    else:  # "bottom"
        # measure total text height
        bbox = draw.textbbox((0, 0), "A", font=font)
        line_height = bbox[3] - bbox[1]  # bottom–top
        n_lines = wrapped.count("\n") + 1
        y = H - line_height * n_lines - 10

    # Draw wrapped text
    draw.multiline_text(
        (W/2, y),
        wrapped,
        font=font,
        fill=text_color,
        stroke_fill=stroke_color,
        stroke_width=stroke_width,
        anchor="ma",
        align="center"
    )

    if out_path:
        img.save(out_path, quality=90)
    return img

#def list_templates() -> list[str]:
    #"""Return all available template file paths."""
#def create_meme(
    #template_path: str,
    #text: str,
    #font_path: str = "fonts/impact.ttf",
    #font_size: int = 48,
    #text_color: str = "white",
    #stroke_color: str = "black",
    #out_path: str | None = None
#) -> PIL.Image.Image:
    #"""Load template, draw text, optionally save, then return the Image."""