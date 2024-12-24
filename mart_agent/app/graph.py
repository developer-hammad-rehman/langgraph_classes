from app.config import graph_builder
from app.utils import assistant_node , tools_node
from langgraph.graph import START
from langgraph.prebuilt import tools_condition


graph_builder.add_node("assistant", assistant_node)
graph_builder.add_node("tools", tools_node)
graph_builder.add_edge(START, "assistant")
graph_builder.add_conditional_edges(
    "assistant",
    tools_condition,
)
graph_builder.add_edge("tools", "assistant")


graph  = graph_builder.compile()