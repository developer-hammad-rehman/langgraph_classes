from langgraph.graph import START, END, StateGraph, MessagesState
from langchain_google_genai import ChatGoogleGenerativeAI
from app.prompt import SYTSTEM_PROMPT
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


graph_buiilder = StateGraph(MessagesState)


def assistant_node(state: MessagesState):
    system_message = SystemMessage(content=SYTSTEM_PROMPT)
    messages = [system_message] + state["messages"]
    response = llm.invoke(messages)
    return {"messages": response}


graph_buiilder.add_node("assistant", assistant_node)

graph_buiilder.add_edge(START, "assistant")
graph_buiilder.add_edge("assistant", END)

graph = graph_buiilder.compile()
