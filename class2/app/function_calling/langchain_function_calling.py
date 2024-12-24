from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , SystemMessage


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


def product_data(category : str):
    """
    Get The Product Data
    """
    if category.lower() == "women":
        return {
            'products'  : ["shirts" , "tshirst" , 'polo shirt'] 
        } 
    else:
        return "Product Not avaliable"
    


llm_with_tools = llm.bind_tools([product_data])

messages : list = [
    HumanMessage(content="Hello")
] 


response = llm_with_tools.invoke(messages)

functions = {
    "product_data" : product_data
}



if response.tool_calls:
    for tool_call in response.tool_calls:
        to_func_call  = tool_call["name"]
        tools_agrs = tool_call["args"]
