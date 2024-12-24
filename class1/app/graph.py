from langgraph.graph import StateGraph, START, END
from typing import TypedDict


class Message(TypedDict):
    name: str
    greet_answer: str


graph_builder = StateGraph(Message)


def final_answer(state: Message):
    greet_message = f'Hello {state["name"]}'
    return {"greet_answer": greet_message}


graph_builder.add_node("final_answer", final_answer)
graph_builder.add_edge(START, "final_answer")
graph_builder.add_edge("final_answer", END)
graph = graph_builder.compile()
