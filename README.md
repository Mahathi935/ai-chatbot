# 💬 AI Chatbot

A ChatGPT-like chatbot built in small daily steps.

## Build log
- **Day 1** ✅ — Basic chat UI with Streamlit (placeholder responses)
- **Day 2** ✅ — Connect a real LLM (Groq / Llama 3.1)
- **Day 3** ✅ — Smarter memory (trimmed history) + clear chat button
- **Day 4** ✅ — System prompt (personality) + deployed live

## Live demo
👉 https://ai-chatbot-re5nnbjlyp47hkr877uf4a.streamlit.app/
## Setup notes
Add your `GROQ_API_KEY` as a secret when deploying (see deployment steps below), not as a plain environment variable in code.

## Run it locally
1. Copy `.env.example` to `.env` and paste in your own Groq API key
2. Install dependencies and run:
```bash
pip install -r requirements.txt
streamlit run app.py
```
