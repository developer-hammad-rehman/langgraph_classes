from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()



llm : ChatGoogleGenerativeAI  = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

response = llm.stream("Generate Me The Essay on ai")

for chunk in response:
    print(chunk.content , end="")