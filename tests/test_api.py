import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

res = client.responses.create(
    model="gpt-4.1-mini",
    input="responde só: ok"
)

print(res.output_text)
