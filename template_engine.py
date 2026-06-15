from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
client=Groq()
role=input("pls enter the role:")
question=input("pls,enter the question")
chat_prompt=ChatPromptTemplate.from_messages([
    ("system","you are a {role} assistant"),
    ("human",'{question}')
])
result=chat_prompt.invoke({'role':role,'question':question})
respone=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user" if m.type == "human" else m.type, "content": m.content} for m in result.to_messages()]
)
print(respone.choices[0].message.content)