"""Python module to test Google Gemini AI features."""

from generate_image import GeminiImage


def test_image_text_contains() -> None:
    """Tests that the image contains the correct text."""
    gemini_image = GeminiImage()
    image_text = gemini_image.generate_image("Siamese Cat", "siamese_cat.png")
    assert "Siamese" in image_text  # noqa: S101
