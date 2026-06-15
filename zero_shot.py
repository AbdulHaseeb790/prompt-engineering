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

# Zero-shot examples
print(prompt("Translate to French: Hello how are you?"))
print("---")
print(prompt("Is this review positive or negative: The food was amazing!"))
print("---")
print(prompt("Summarize in one sentence: Artificial intelligence is a branch of computer science that aims to create machines that can perform tasks that typically require human intelligence."))