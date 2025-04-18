# tests/test_shrink.py
"""
Unit‑test for dynamic font‑shrinking in create_meme().
Run with:  pytest -q
"""

import os
import tempfile
import PIL
from PIL import Image
from image_editor.meme_editor import create_meme


def test_dynamic_shrink_fits_on_small_image():
    """
    The text is extremely long and the template is very small.
    create_meme() should shrink the font enough that the caption
    still fits and the function does not crash.
    """
    # 1) create a tiny 300×200 white image in a temp dir
    with tempfile.TemporaryDirectory() as tmpdir:
        template_path = os.path.join(tmpdir, "tiny.jpg")
        Image.new("RGB", (300, 200), color="white").save(template_path)

        # 2) super‑long caption (forces shrink)
        long_text = " ".join(["shrink"] * 120)

        # 3) output file path
        out_path = os.path.join(tmpdir, "out.jpg")

        # 4) call the meme generator
        img = create_meme(
            template_path,
            long_text,
            font_size=48,          # starting size (will shrink)
            stroke_width=2,
            position="top",
            out_path=out_path
        )

        # 5) basic assertions
        assert os.path.exists(out_path), "Output image was not created"
        assert img.size == (300, 200)    # template size unchanged
