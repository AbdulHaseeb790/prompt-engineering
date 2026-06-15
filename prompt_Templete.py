from dotenv import load_dotenv
from groq import Groq
load_dotenv()
client=Groq()
from langchain_core.prompts import PromptTemplate
prompt=PromptTemplate(template="whats your name {name}:welcome {name}")
result=prompt.invoke({'name':'haseeb'})
print(result)

respone=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {'role':'user','content':result.text}
    ]

    
            

    

)
print(respone.choices[0].message.content)
