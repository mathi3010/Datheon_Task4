# Datheon Task 4: Interactive Full-Stack AI Chatbot

## Project Overview
This project is an interactive AI chatbot built using Streamlit and Google's Gemini API. It provides a conversational interface that supports multiple questions, conversation history, and streaming responses.

## Features
- Interactive chatbot interface using Streamlit
- Gemini AI integration
- Conversation history
- Session state management
- Streaming AI responses
- Clear chat functionality
- Error handling for API failures

## Technologies Used
- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- Python-dotenv

## Project Structure
```text
Datheon_Task4/
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment on Windows:

```powershell
venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

## Run the Application

```bash
streamlit run app.py
```

The application opens at:

`http://localhost:8501`

## Usage
Enter a question in the chatbot input box. Gemini generates a response, and the conversation remains visible during the session. Use the Clear Chat button to reset the conversation.

## Conclusion
This project demonstrates an interactive AI chatbot using Streamlit, Gemini, conversation history, and streaming responses.

