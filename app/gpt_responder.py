import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure it's set in your .env file

def get_gpt_reply(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a kind English tutor for children aged 6 to 16."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"(OpenAI GPT error: {e})"
