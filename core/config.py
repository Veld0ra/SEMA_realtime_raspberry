import os

API_KEY = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-realtime"

URL = f"wss://api.openai.com/v1/realtime?model={MODEL}"

DEBUG = True
