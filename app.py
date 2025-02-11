import streamlit as st
from transformers import pipeline

# Initialize the model pipeline
@st.cache_resource()
def load_model():
    return pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", trust_remote_code=True)

pipe = load_model()

# Streamlit UI
st.title("AI Chatbot using DeepSeek-R1")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role = "User" if msg["role"] == "user" else "Bot"
    st.write(f"**{role}:** {msg['content']}")

# User input
user_input = st.text_input("You:", "")
if user_input:
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate response
    response = pipe(user_input)[0]['generated_text']
    
    # Append response to chat history
    st.session_state.messages.append({"role": "bot", "content": response})
    
    # Refresh the page to show updates
    st.rerun()
