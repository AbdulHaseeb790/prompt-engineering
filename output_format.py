from dotenv import load_dotenv
from groq import Groq
import json

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

system = """You are a sentiment analysis API.
Always respond in JSON format like this:
{
  "sentiment": "positive/negative/neutral",
  "confidence": "high/medium/low",
  "reason": "one sentence explanation"
}
Return only JSON, no extra text."""

result = prompt(system, "I absolutely loved this movie, best film of the year!")
print(result)

# Parse it as real JSON
data = json.loads(result)
print(f"\nSentiment: {data['sentiment']}")
print(f"Confidence: {data['confidence']}")