"""Python module to generate images using Google Gemini AI."""

from __future__ import annotations

from io import BytesIO

from google import genai
from google.genai import types
from PIL import Image

from lib.common import gemini_api_key


class GeminiImage:
    """Class responsible for handling image generation."""

    def __init__(self) -> None:
        """Initialize class objects."""
        self.part_text = None

    def generate_image(self, prompt: str, image_file_name: str) -> str | None:
        """Generate an image given a prompt."""
        client = genai.Client(api_key=gemini_api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
            ),
        )

        for part in response.candidates[0].content.parts:
            if part.text is not None:
                self.part_text = part.text
            elif part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                image.save(image_file_name)
        return self.part_text


if __name__ == "__main__":
    image = GeminiImage()
    prompt = "Siamese Cat"
    image_file_name = "siamese_cat.png"
    image.generate_image(prompt, image_file_name)
