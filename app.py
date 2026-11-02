
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
import time
# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
if not api_key:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=api_key)
MODEL = "gemini-3.8-flash"

# Streamlit page configuration
st.set_page_config(
    page_title="Datheon AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Datheon AI Chatbot")
st.caption("Task 4 - Interactive Full-Stack AI Chatbot")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):

    # Display user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Prepare Gemini conversation
    conversation = "\n".join(
        f'{message["role"]}: {message["content"]}'
        for message in st.session_state.messages
    )

    # Generate Gemini response
    
    with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            for attempt in range(3):
                try:
                    response = client.models.generate_content_stream(
                        model=MODEL,
                        contents=conversation
                    )

                    for chunk in response:
                        if chunk.text:
                            full_response += chunk.text
                            response_placeholder.markdown(full_response + "▌")

                    break

                except Exception as error:
                    if attempt < 2:
                        response_placeholder.info(
                            f"Gemini is busy. Retrying in {5 * (attempt + 1)} seconds..."
                        )
                        time.sleep(5 * (attempt + 1))
                    else:
                        full_response = f"Gemini request failed: {error}"
                        response_placeholder.error(full_response)

            if full_response and not full_response.startswith("Gemini request failed:"):
                response_placeholder.markdown(full_response)

# Sidebar
with st.sidebar:
    st.header("Chat Settings")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.write("Powered by Gemini")
    st.write("Built with Streamlit")
