from fastapi import FastAPI
from langgraph_sdk import get_client

app = FastAPI()


client = get_client(url="http://127.0.0.1:2024")


@app.get("/")
async def main_root(name : str):
    thread = await client.threads.create()
    assitant = await client.runs.wait(
       thread["thread_id"] , "agent"  , input={"name":name}
    )
    return assitant["greet_answer"]



@app.get('/generate-pdf-essay')
async def pdf_generator(query : str):
   thread = await client.threads.create()
   assistant = await client.runs.wait(
       thread["thread_id"] , "agent"  , input={
         "messages":[
            ("human" , query)
         ]
       }
   )
   return assistant["messages"][-1]["content"]