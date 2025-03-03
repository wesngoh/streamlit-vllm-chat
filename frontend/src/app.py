import streamlit as st
import requests
import json
import os

st.set_page_config(page_title="vLLM Chatbot", page_icon="💬", layout="wide")
st.title("AI Chatbot with vLLM")

# initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# initialize session state for system prompt
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = "You are a helpful assistant."

# generate response using vLLM API
vllm_api_url = os.getenv("VLLM_API_URL")

def generate_response(messages):
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "unsloth/tinyllama-chat-bnb-4bit",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(vllm_api_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error calling vLLM API: {str(e)}")
        return None

# sidebar settings
with st.sidebar:
    st.header("Settings")
    
    # system prompt input
    new_system_prompt = st.text_area("System Prompt", st.session_state.system_prompt, 
                                   help="Instructions for how the AI assistant should behave")
    if new_system_prompt != st.session_state.system_prompt:
        st.session_state.system_prompt = new_system_prompt

    if st.button("Submit"):
        st.session_state.messages = []
        st.rerun()

# main chatbot interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message here...")
if user_input:
    # add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # prepare messages for API call
    api_messages = [{"role": "system", "content": st.session_state.system_prompt}] + st.session_state.messages
    
    # display thinking animation
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.write("Thinking...")
        
        # call API and get response
        assistant_response = generate_response(api_messages)
        
        if assistant_response:
            # display assistant response
            message_placeholder.write(assistant_response)
            
            # add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})