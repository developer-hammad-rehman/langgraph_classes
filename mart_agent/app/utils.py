from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from app.config import llm , system_message , tools


def assistant_node(state:MessagesState):
    messages = [system_message] + state["messages"]
    response = llm.invoke(messages)
    return {"messages":response}


tools_node = ToolNode(tools=tools)