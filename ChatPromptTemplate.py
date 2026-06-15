from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client=Groq()
chat_prompt=ChatPromptTemplate.from_messages([
    ("system","you are a {role} assistant"),
    ("human","{question}")
])
result = chat_prompt.invoke({"role": "chef", "question": "how do i make pasta"})
response=client.chat.completions.create(
    model='llama-3.3-70b-versatile',
    messages=[{"role": "user" if m.type == "human" else m.type, "content": m.content} for m in result.to_messages()]

)
print(response.choices[0].message.content)