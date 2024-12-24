from langchain_core.messages import SystemMessage
from app.prompts import SYSTEM_PROMPT
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph , MessagesState
from app.tools import get_products
from langchain_openai import ChatOpenAI

load_dotenv()



llm = ChatOpenAI(model="gpt-4o-mini")


system_message = SystemMessage(content=SYSTEM_PROMPT)


graph_builder = StateGraph(MessagesState) 

tools = [get_products]