"""Python module to generate images using Google Gemini AI."""

from __future__ import annotations

from google import genai

from lib.common import gemini_api_key


class GeminiVideo:
    """Class responsible for handling video generation."""

    def __init__(self) -> None:
        """Initialize class objects."""
        self.part_text = None

    def generate_video(self, prompt: str, video_file_name: str) -> str | None:
        """Generate a video given a prompt."""
        client = genai.Client(api_key=gemini_api_key)
        operation = client.models.generate_videos(
            model="veo-3.0-generate-preview",
            prompt=prompt,
        )
        video = operation.response.generated_videos[0]
        video.video.save(video_file_name)


if __name__ == "__main__":
    video = GeminiVideo()
    prompt = "siamese cat meowing"
    video_file_name = "siamese_cat.mp4"
    video.generate_video(prompt, video_file_name)
