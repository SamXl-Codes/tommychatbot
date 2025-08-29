import os
import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

system_prompt = """
    You are TommyChat.
    Answer any question in your best view, question can be any aspect of life, work, academics and so on.

    You should also have a sense of humor.
"""

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")]
)

chain = prompt | llm | StrOutputParser()


def chat(user_input, hist):

    langchain_history = []
    for item in hist:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item['content']))
        elif item['role'] == 'assistant':
            langchain_history.append(AIMessage(content=item['content']))

    response = chain.invoke({"input": user_input, "history": langchain_history})

    return "", hist + [{"role": "user", "content": user_input},
                {"role": "assistant", "content": response}]


def clear_chat():
    return"", []

app = gr.Blocks(
    title="Connect with TommyChat",
    theme=gr.themes.Soft(),
)

with app:
    gr.Markdown (
        """
        # Connect with TommyChat
        Start your personal conversation...
        """
    )

    chatbot = gr.Chatbot(type='messages', avatar_images= [None, 'tommychat.png'],
                         show_label=False)

    msg = gr.Textbox(show_label=False, placeholder= "Ask Tommychat anything....")

    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat")
    clear.click(clear_chat, outputs=[msg, chatbot])

app.queue() 