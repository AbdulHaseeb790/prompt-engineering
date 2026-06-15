from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

def prompt(user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": user_message}]
    )
    return response.choices[0].message.content

# Without CoT
print("WITHOUT COT:")
print(prompt("If I have 10 apples, give 3 to John, eat 2, then buy 5 more. How many do I have?"))
print("---")

# With CoT
print("WITH COT:")
print(prompt("Think step by step. If I have 10 apples, give 3 to John, eat 2, then buy 5 more. How many do I have?"))