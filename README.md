# TommyChat

TommyChat is a conversational AI chatbot built with [Gradio](https://www.gradio.app/), [LangChain](https://python.langchain.com/), and Google's [Gemini 1.5 Flash](https://ai.google.dev/) model. It enables interactive, humorous conversations on topics like life, work, academics, and more, with a user-friendly web interface and conversation history for context-aware responses.

## Features
- **Interactive Chat**: Engage in real-time conversations with TommyChat, infused with a touch of humor.
- **Conversation History**: Maintains context by storing previous messages in the session.
- **Web Interface**: Powered by Gradio, offering a clean and intuitive UI.
- **Customizable**: Configurable via environment variables for the Gemini API key.

## Prerequisites
- Python 3.8 or higher (tested with Python 3.13)
- A valid [Google Generative AI API key](https://aistudio.google.com/) for Gemini 1.5 Flash
- Git for cloning the repository
- A web browser to access the Gradio interface
- Render hosting platform for deployment 

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SamXI-Codes/tommychatbot.git

2. **Set Up a Virtual Environment (recommended)**:
   ```bash 
   python -m venv venv .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux

3. **Install Dependencies**:
    ```bash
    pip install python-dotenv langchain-core langchain-google-genai gradio

4. **Create a .env File**:
In the tommychatbot/ directory, create a .env file with:
plaintextGEMINI_API_KEY=your_actual_api_key_here
Obtain your API key from Google AI Studio or Google Cloud Console.

5. **When deploying on Render, the entry point in main2.py is already configured for Render’s environment**:
   ```bash
    if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))  # Render gives us a PORT
    app.queue()
    app.launch(server_name="0.0.0.0", server_port=port)
Render will assign your app a public URL automatically after deployment.

## Usage
1. **Run the Application**:
   ```bash
    python main2.py

2. **Access the Chatbot**:
Open http://127.0.0.1:7860 in a web browser (default Gradio URL).
Enter a message in the textbox and press Enter to chat with TommyChat.
Click the "Clear Chat" button to reset the conversation history.

## Deployment on Render 
1. Push your project to GitHub.
2. Log in to Render and create a New Web Service.
3. Connect your GitHub repo.
4. Configure the service:
- Environment:
  ```bash
  Python 3
- Build Command:
   ```bash
   pip install -r requirements.txt
- Start Command:
   ```bash
  python main2.py
- Add your environment variables under Render > Environment:
  ```bash
  GEMINI_API_KEY=your_actual_api_key_here
Once deployed, Render will give you a permanent public URL that you can share with others

## Project Structure

- **main2.py: Main script for the chatbot logic and Gradio interface.**
- **.env: Stores API keys (not tracked in Git).**
- **.gitignore: Excludes sensitive files like .env and venv/.**
- **README.md: This documentation.**
- **LICENSE: MIT License file.**
