import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # reads the .env file and loads GROQ_API_KEY into the environment

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="💬")
st.title("💬 AI Chatbot")
st.caption("Day 2: now powered by a real LLM (Groq / Llama 3.1)")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your chatbot. Ask me anything."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Send the ENTIRE conversation so far to the model, not just the last message.
    # This is what lets the AI "remember" earlier turns in this chat.
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages,
    )
    ai_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)
