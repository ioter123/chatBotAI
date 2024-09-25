from fastapi import APIRouter
from model import *
from chatbot import ChatBot

app_router = APIRouter()
chat = ChatBot()


@app_router.post("/chatbot")
async def chatbot(messages: Massage) -> dict:
    print(messages)
    res = chat.ask(messages.message)
    return {"message": res}


@app_router.get("/chatbotClear")
async def chatbotclear() -> dict:
    chat.clear()
    return {"message": "챗봇이 초기화되었습니다."}


@app_router.get("/chatbotShow")
async def chatbotshow() -> dict:
    messages = chat.show_messages()
    return {"message": messages}