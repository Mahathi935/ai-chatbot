import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="💬")
st.title("💬 AI Chatbot")
st.caption("Day 3: smarter memory + clear chat button")

# How many past messages (user+assistant combined) to actually send to the model.
# Keeps requests fast and avoids hitting the model's context limit on long chats.
MAX_HISTORY = 20

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your chatbot. Ask me anything."}
    ]

# --- Sidebar: clear chat button ---
with st.sidebar:
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm your chatbot. Ask me anything."}
        ]
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Only send the most recent MAX_HISTORY messages to the model.
    # Full history still stays in st.session_state.messages so the UI shows everything;
    # we just trim what we SEND to the API.
    recent_messages = st.session_state.messages[-MAX_HISTORY:]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=recent_messages,
    )
    ai_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)
