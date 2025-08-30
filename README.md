TommyChat

TommyChat is a conversational AI chatbot built with Gradio, LangChain, and Google's Gemini 1.5 Flash model. It allows users to engage in interactive, humorous conversations on topics related to life, work, academics, and more. The chatbot maintains conversation history for context-aware responses and features a user-friendly web interface.

Features





Interactive Chat: Engage in real-time conversations with TommyChat, which responds with a touch of humor.



Conversation History: Maintains context by storing previous messages in the session.



Web Interface: Powered by Gradio, providing a clean and intuitive UI.



Customizable: Configurable via environment variables for the Gemini API key. 

Installation





Clone the Repository:

git clone https://github.com/your-username/tommychatbot.git
cd tommychatbot



Set Up a Virtual Environment (optional but recommended):

python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux



Install Dependencies:

pip install python-dotenv langchain-core langchain-google-genai gradio



Create a .env File: In the project root directory (tommychatbot/), create a .env file with your Gemini API key:

GEMINI_API_KEY=your_actual_api_key_here

Obtain your API key from Google AI Studio or Google Cloud Console.

Usage





Run the Application:

python main2.py



Access the Chatbot:





Open your web browser and navigate to http://127.0.0.1:7860 (default Gradio URL).



Enter a message in the textbox and press Enter to chat with TommyChat.



Click the "Clear Chat" button to reset the conversation history.



Share Publicly (Optional): To create a public URL for sharing:





Update main2.py to set app.launch(share=True, debug=True).



Ensure you have a Hugging Face token for authentication:

pip install huggingface_hub
huggingface-cli login



Add HF_TOKEN=your_hugging_face_token_here to the .env file.



Run python main2.py and check the terminal for the public URL (e.g., https://<some-id>.gradio.live).

Troubleshooting





Import Errors: Ensure all dependencies are installed in the correct Python environment. Run pip list to verify.



API Key Issues: Confirm your GEMINI_API_KEY is valid and correctly formatted in the .env file.



No Public Link: Check your internet connection, firewall settings, and ensure the FRP binary (frpc_windows_amd64_v0.2) is present in the Gradio package directory. See the Gradio documentation for more details.



Chat Format Errors: The chatbot uses the messages format ([{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]). Ensure type="messages" is set in the gr.Chatbot component.

Project Structure





main2.py: Main script implementing the chatbot logic and Gradio interface.



.env: Environment file for storing the Gemini API key (not tracked in Git).



README.md: This file, providing project documentation.


License

This project is licensed under the MIT License. See the LICENSE file for details.