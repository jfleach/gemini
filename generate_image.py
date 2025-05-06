"""Python module to generate images using Google Gemini AI."""

from io import BytesIO

from google import genai
from google.genai import types
from PIL import Image

from lib.common import gemini_api_key


class GeminiImage:
  """Class responsible for handling image generation."""

  def generate_image(self, prompt: str) -> None:
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
          print(part.text) # noqa: T201
        elif part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            # TODO: Save with timestamp # noqa: FIX002 TD003 TD002
            image.save("gemini-native-image.png")
            image.show()

if __name__ == "__main__":
    image = GeminiImage()
    prompt = "lynx point siamese cat"
    image.generate_image(prompt)
