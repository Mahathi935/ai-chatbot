import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="💬")
st.title("💬 AI Chatbot")
st.caption("Ask me anything — I'll do my best to help.")

MAX_HISTORY = 20

# This tells the model HOW to behave. It's never shown in the chat UI —
# it's sent to the API on every request as invisible "background instructions."
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a friendly, helpful assistant. Keep answers clear and concise. "
        "If you don't know something, say so honestly instead of guessing."
    ),
}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your chatbot. Ask me anything."}
    ]

with st.sidebar:
    st.subheader("About")
    st.write("A simple AI chatbot built with Streamlit + Groq (Llama 3.1).")
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

    recent_messages = st.session_state.messages[-MAX_HISTORY:]

    # Put the system prompt FIRST, then the recent conversation after it.
    api_messages = [SYSTEM_PROMPT] + recent_messages

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=api_messages,
        )
    ai_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)
