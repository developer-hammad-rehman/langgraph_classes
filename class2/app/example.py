from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()


system_message = SystemMessage(
    content="""
 You are The Essay generate AI Agent . Generate The Best Possible essay according to the Human Query.
"""
)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


response = llm.invoke(
    [system_message, HumanMessage(content="Generate Essay On AI Agents")]
)


print(response.content)
