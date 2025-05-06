"""Python module that provides common functionality for the other modules."""


import os

from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
