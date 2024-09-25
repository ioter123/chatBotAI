from openai import OpenAI

#
# def ai_chat(message):
#     client = OpenAI(
#         api_key='sk-w6B51885ldKTZWeb1GVfRojvZ-RlJ3JOmYnDxzFP8kT3BlbkFJWjcCEIFOLFPnZYXGLMHKTjTWvBZ9NPxGyLbGJR-3sA',
#     )
#     total_message = [
#         {
#             "role": "system",
#             "content": "질문자의 상황에 적합한 캐릭터를 추천해주는 전문가야. 대답은 항상 한글로 해줘."
#         }
#     ]
#     total_message += message
#     completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=total_message
#     )
#
#     return total_message + [{'role':'assistant', 'content': completion.choices[0].message.content}]


# 챗봇 클래스
class ChatBot():
    def __init__(self, model='gpt-4o'):
        # api key 입력
        self.client = OpenAI(
            api_key='sk-w6B51885ldKTZWeb1GVfRojvZ-RlJ3JOmYnDxzFP8kT3BlbkFJWjcCEIFOLFPnZYXGLMHKTjTWvBZ9NPxGyLbGJR-3sA',
        )
        # ChatGPT 모델
        self.model = model
        # GPT 시스템 세팅
        self.messages = [
            {
                "role": "system",
                "content": "질문자의 질문에 정확한 답변을 하는 전문가야. 대답은 항상 한글로 해주고 항상 존댓말로 대답해줘."
            }
        ]

    # 질문 시작
    def ask(self, question):
        self.messages.append({
            'role': 'user',
            'content': question
        })
        res = self.__ask__()
        return res

    def __ask__(self):
        completion = self.client.chat.completions.create(
            # model 지정
            model=self.model,
            messages=self.messages
        )
        response = completion.choices[0].message.content
        self.messages.append({
            'role': 'assistant',
            'content': response
        })
        return response

    # 응답 보여주기
    def show_messages(self):
        return self.messages

    # GPT 초기화
    def clear(self):
        #self.messages.clear()
        self.messages = [
            {
                "role": "system",
                "content": "질문자의 질문에 정확한 답변을 하는 전문가야. 대답은 항상 한글로 해주고 항상 존댓말로 대답해줘."
            }
        ]