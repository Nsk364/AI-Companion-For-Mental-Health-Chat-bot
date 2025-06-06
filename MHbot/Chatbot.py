import streamlit as st

# ✅ MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Your AI Companion", layout="wide")

import json
import time
import os
import base64
from langchain_together import Together
from langchain.llms import Cohere
import datetime

# Set API Key
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "1e7a5e10482ad3bce271180e403c1b4e9a785a00ec66c9821621d036d354ae72")

# Load dataset function
@st.cache_data
def load_mental_health_data():
    with open(r"MentalHeathHelpDatabase.json", "r") as file:
        return json.load(file)

# System prompt for AI behavior
SYSTEM_PROMPT =  """
You are a kind, compassionate, and supportive mental health assistant.  
Your goal is to **uplift, encourage, and provide clear, practical advice** to users in distress.

**How to Respond:**
- **Keep the response a bit short**.
- **Start every response with a strong, reassuring sentence in CAPITALS and bold.**  
- Focus on **empowering solutions** rather than just acknowledging distress.  
- Use a **warm, hopeful tone**, reminding them that **things can improve and they are capable**.  
- Offer **small, achievable steps** for self-care, deep breathing, and positive self-talk.  
- If a user feels **overwhelmed, remind them of their inner strength**.  
"""

# Encode image to Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_data = base64.b64encode(img_file.read()).decode()
        return f"data:image/png;base64,{b64_data}"

background_image = get_base64_image("MHbot/bg.jpg")  # your local image file

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize AI models
models = {
    "Breezy (Mistral AI)": Together(model="mistralai/Mistral-7B-Instruct-v0.3", together_api_key=TOGETHER_API_KEY),
    "Luna (LLaMA 3.3 Turbo)": Together(model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", together_api_key=TOGETHER_API_KEY),
    "Thinky (DeepSeek R1)": Together(model="deepseek-ai/deepseek-r1-distill-llama-70b-free", together_api_key=TOGETHER_API_KEY),
    "Visionary (LLaMA Vision)": Together(model="meta-llama/Llama-Vision-Free", together_api_key=TOGETHER_API_KEY),
    "Dash (Cohere Command)": Cohere(model="command-xlarge", cohere_api_key="sWmE1lyhhw4XomK8LVSW58LlX0fe4ke89B1fxFvz")
}

# UPDATED get_response FUNCTION
def get_response(model_name, user_query, dataset):
    # Append relevant context from dataset
    for keyword, advice in dataset.items():
        if keyword in user_query.lower():
            user_query += f"\n[Additional Context: {advice}]"
    
    full_prompt = SYSTEM_PROMPT + "\nUser: " + user_query + "\nAI:"
    try:
        # First attempt with full tokens and system prompt
        response = models[model_name].invoke(full_prompt, max_tokens=1024).strip()
        
        # Retry attempts - always include the system prompt + user input again
        retry_attempts = 3
        while (not response.endswith(".") and retry_attempts > 0):
            # Retry prompt still includes system prompt and user query for consistency
            retry_prompt = SYSTEM_PROMPT + "\nUser: " + user_query + "\nAI: " + response
            additional = models[model_name].invoke(retry_prompt, max_tokens=256).strip()
            response += " " + additional
            retry_attempts -= 1
        
        return response if isinstance(response, str) else str(response)
    except Exception as e:
        return f"⚠️ Error: {str(e)}"
# Overlay + Chat CSS
st.markdown("""
    <style>
        .chat-container {
            max-width: 700px;
            margin: auto;
            background: rgba(255, 255, 255, 0.15);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 255, 200, 0.3);
            backdrop-filter: blur(10px);
        }
        .chat-message {
            padding: 12px;
            border-radius: 8px;
            margin: 10px 0;
            font-size: 16px;
            animation: fadeIn 0.5s forwards;
            display: inline-block;
        }
        .user-message {
            background: linear-gradient(135deg, #007aff, #00c6ff);
            color: white;
            text-align: right;
            border-radius: 15px 15px 0 15px;
            padding: 10px 15px;
        }
        .ai-message {
            background: linear-gradient(135deg, #00e676, #1de9b6);
            color: black;
            text-align: left;
            border-radius: 15px 15px 15px 0;
            padding: 10px 15px;
        }
        .typing-indicator {
            font-size: 14px;
            color: #00e676;
            display: flex;
            align-items: center;
        }
        .dot {
            width: 6px;
            height: 6px;
            margin: 0 3px;
            background: #00e676;
            border-radius: 50%;
            animation: blink 1.5s infinite;
        }
        .dot:nth-child(2) { animation-delay: 0.3s; }
        .dot:nth-child(3) { animation-delay: 0.6s; }
        @keyframes blink {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }
        .send-button {
            background: linear-gradient(135deg, #007aff, #00c6ff);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            font-size: 16px;
            transition: 0.3s;
        }
        .send-button:hover {
            background: linear-gradient(135deg, #00c6ff, #007aff);
            transform: scale(1.05);
        }
        .send-button:active {
            transform: scale(0.95);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div style="text-align: center;">
  <h1 style="
    color: #c9c5c5; 
    font-weight: bold;
    display: inline-block;
  ">
    🤗 AI Companion Chatbot
  </h1>
</div>
""", unsafe_allow_html=True)
st.write("🌿 **A calming AI companion for your mental well-being.**")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [("ai-message", "<strong>NSK :</strong> Hello! I am here for you. How are you feeling right now?", datetime.datetime.now().strftime("%H:%M:%S"))]

# Model Selection
model_choice = st.selectbox("Select the type of your AI Friend", list(models.keys()))

# Chat Container
chat_container = st.container()
with chat_container:
    for role, text, timestamp in st.session_state.messages:
        st.markdown(f'<div class="chat-container"><div class="chat-message {role}">{text} <br><small style="color:gray;">🕒 {timestamp}</small></div></div>', unsafe_allow_html=True)

# Input + Buttons
user_input = st.text_input("💬 Type your message here...")
col1, col2 = st.columns([4, 1])
with col1:
    send_btn = st.button("Send", key="send-btn")
with col2:
    clear_btn = st.button("🗑 Clear Chat", key="clear-btn")

# Clear Chat Logic
if clear_btn:
    st.session_state.messages = []
    st.rerun()

# Send Message Logic
if send_btn:
    if user_input.strip():
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        st.session_state.messages.append(("user-message", f"<strong>You:</strong> {user_input}", timestamp))
        with st.spinner("OK..."):
            time.sleep(1.5)
            dataset = load_mental_health_data()
            response = get_response(model_choice, user_input, dataset)
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        st.session_state.messages.append(("ai-message", f"<strong>{model_choice}:</strong> {response}", timestamp))
        st.rerun()
    else:
        st.warning("⚠️ Please type a message before sending.")
