import gradio as gr
import random
import time
from chatbot import ChatBot

# 챗봇 인스턴스 생성
chatgpt = ChatBot()

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        # ChatGPT 질의
        bot_message = chatgpt.ask(message)
        # 답변 기록
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

# 로컬(local) 구동시
demo.launch()