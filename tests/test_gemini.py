"""Python module to test Google Gemini AI features."""

# ruff: noqa: S101

from pathlib import Path

from generate_content import GeminiContent
from generate_image import GeminiImage

FILE_NAME = "siamese_cat.png"
PROMPT = "Siamese Cat"


def test_content() -> None:
    """Tests that the image contains the correct text."""
    gemini_content = GeminiContent()
    image_text = gemini_content.generate_content(PROMPT)
    assert "Siamese" in image_text


def test_image() -> None:
    """Tests that the image contains the correct text."""
    gemini_image = GeminiImage()
    image_text = gemini_image.generate_image(PROMPT, FILE_NAME)
    assert "Siamese" in image_text
    assert Path(FILE_NAME).exists()
    Path(FILE_NAME).unlink()
