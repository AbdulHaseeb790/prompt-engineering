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

few_shot_prompt = """
Classify the sentiment as Positive, Negative or Neutral.

Review: "I loved this product!"
Sentiment: Positive

Review: "Worst purchase ever."
Sentiment: Negative

Review: "It's okay, nothing special."
Sentiment: Neutral

Review: "Absolutely fantastic experience!"
Sentiment:"""

print(prompt(few_shot_prompt))