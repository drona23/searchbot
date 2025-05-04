# helper.py

import os
from openai import OpenAI

# Grab your key from the env (set as a HF Space secret or locally exported)
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# Instantiate the new client
client = OpenAI(api_key=API_KEY)

# Define your chatbot’s persona
PERSONA = (
    "You are a kind, caring, and emotionally intelligent AI companion. "
    "You speak warmly and naturally, like a close friend who listens well "
    "and gives thoughtful, encouraging replies. You avoid sounding robotic "
    "or repetitive. If someone sounds down, you comfort them. If they’re excited, "
    "you celebrate with them."
)

def generate_reply(user_message: str) -> str:
    """
    Send the user’s message to OpenAI via the 1.0.0+ client
    and return the assistant’s reply.
    """
    messages = [
        {"role": "system",  "content": PERSONA},
        {"role": "user",    "content": user_message}
    ]
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=512
        )
        # Extract the text of the assistant’s reply
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {e}"
