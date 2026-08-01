import streamlit as st

st.set_page_config(page_title="AI Chatbot", page_icon="💬")
st.title("💬 AI Chatbot")
st.caption("Day 1: basic chat interface — AI brain gets wired in on Day 2")

# Keep the conversation in memory for this session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your chatbot. Ask me anything."}
    ]

# Show past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Get new user input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Placeholder reply — Day 2 will replace this with a real AI call
    placeholder_reply = "(Placeholder reply — real AI answer coming on Day 2!)"
    st.session_state.messages.append({"role": "assistant", "content": placeholder_reply})
    with st.chat_message("assistant"):
        st.write(placeholder_reply)
