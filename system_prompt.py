from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

def prompt(system, user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

# Bad system prompt
print("BAD SYSTEM PROMPT:")
print(prompt(
    "You are a helpful assistant.",
    "What is a for loop?"
))
print("---")

# Good system prompt
print("GOOD SYSTEM PROMPT:")
print(prompt(
    "You are an expert Python tutor for beginners. Explain concepts in super simple words with a short code example. Keep answers under 5 lines.",
    "What is a for loop?"
))