# streamlit-vllm-chat
This repository contains a simple streamlit chatbot that uses vLLM's OpenAI compatible server for text generation. The codebase serve as a good template for quick LLM demonstration.

**current model:** [unsloth/tinyllama-chat-bnb-4bit](https://huggingface.co/unsloth/tinyllama-chat-bnb-4bit)

[rdai_vllm.webm](https://github.com/user-attachments/assets/3a3a9990-7717-419e-a256-5ef31149df90)

---
## How to set up:
1. Follow `env_template.txt` to create a new `.env` file with your own HuggingFace token

2. Run the streamlit frontend and vLLM service through `docker compose up --build`
