# 💬 AI Chatbot

A ChatGPT-like chatbot built with Streamlit and Groq's Llama 3.1 model. It holds a real conversation (remembers earlier messages in the session), has a configurable personality via a system prompt, and lets you clear the chat anytime.

## Features
- Real-time AI responses powered by Llama 3.1 (via Groq's free, fast API)
- Multi-turn memory — the bot remembers context from earlier in the conversation
- Clear chat button to start fresh
- Clean, simple chat interface

## Live demo
👉 https://ai-chatbot-re5nnbjlyp47hkr877uf4a.streamlit.app/

## Tech stack
Python · Streamlit · Groq API

## Run it locally
1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```
2. Copy `.env.example` to `.env` and add your own Groq API key
3. Run the app:
```bash
streamlit run app.py
```

## Setup notes
When deploying, add your `GROQ_API_KEY` as a secret in your hosting platform's settings — never commit it directly.
