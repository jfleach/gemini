"""Python module to generate text content using Google Gemini AI."""

from google import genai

from lib.common import gemini_api_key


class GeminiContent:
  """Class responsible for handling text content generation."""

  def generate_content(self, prompt: str) -> None:
    """Generate text content given a prompt."""
    client = genai.Client(api_key=gemini_api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    print(response.text) # noqa

if __name__ == "__main__":
    content = GeminiContent()
    prompt = "lynx point siamese cat"
    content.generate_content(prompt)
