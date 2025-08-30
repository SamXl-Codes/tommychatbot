import os
import gradio as gr
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser  # Updated import
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
if not gemini_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")
print("API Key:", gemini_key)  # Debugging

# Disable ADC
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

system_prompt = """
    You are TommyChat.
    Answer any question in your best view, question can be any aspect of life, work, academics bedeutungand so on.
    You should also have a sense of humor.
"""

# Initialize Gemini LLM
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # Correct model name
        google_api_key=gemini_key,
        temperature=0.5,
        credentials=None,  # Disable ADC
    )
except Exception as e:
    print(f"Failed to initialize LLM: {e}")
    raise

# Build prompt chain
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")]
)

chain = prompt | llm | StrOutputParser()

# Chat function
def chat(user_input, hist):
    langchain_history = []
    for item in hist:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item['content']))
        elif item['role'] == 'assistant':
            langchain_history.append(AIMessage(content=item['content']))

    try:
        response = chain.invoke({"input": user_input, "history": langchain_history})
        return "", hist + [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": str(response)}
        ]
    except Exception as e:
        return f"Error: {str(e)}", hist

# Clear chat
def clear_chat():
    return "", []

# Build Gradio app
app = gr.Blocks(
    title="Connect with TommyChat",
    theme=gr.themes.Soft(),
)

with app:
    gr.Markdown(
        """
        # Connect with TommyChat
        Start your personal conversation...
        """
    )

    chatbot = gr.Chatbot(
        type= "messages",
        label=None,
        value=[]
    )
    msg = gr.Textbox(show_label=False, placeholder="Ask TommyChat anything....")

    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat")
    clear.click(clear_chat, outputs=[msg, chatbot])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))  # Render gives us a PORT
    app.queue()
    app.launch(server_name="0.0.0.0", server_port=port)
