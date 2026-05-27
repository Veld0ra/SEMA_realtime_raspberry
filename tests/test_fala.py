from openai import OpenAI
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. gerar áudio (TTS)
audio = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input="Olá! Eu estou funcionando na sua caixinha bluetooth."
)

# 2. salvar arquivo
file_path = "/tmp/sema_audio.mp3"
with open(file_path, "wb") as f:
    f.write(audio.read())

# 3. tocar no bluetooth
subprocess.run(["paplay", file_path])

