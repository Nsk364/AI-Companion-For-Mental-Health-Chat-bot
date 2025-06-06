# 🤗 AI Companion for Mental Health Chatbot

A comforting AI-based mental health chatbot built using **Streamlit** and **powerful open-source LLMs** via LangChain and Together AI. The bot is designed to offer **empathy-driven responses**, motivation, and small self-care steps to users who might be struggling or seeking mental well-being support.

---

## 🧠 About the Project

Mental health is as important as physical health, and access to empathetic, non-judgmental support is vital. This chatbot acts as a **digital mental health companion**, helping users:

- Express emotions freely in a safe space.
- Receive calming, solution-oriented, and reassuring responses.
- Get **actionable mental health tips** from a curated dataset.
- Switch between multiple AI personalities (**Mistral**, **LLaMA**, **DeepSeek**, and **Cohere**).

---

## 🌟 Key Features

- 🧘‍♀️ **Mental Health Focused Prompting** with a warm, positive tone.
- 🤖 **Multiple LLM Choices** – Choose your AI companion model.
- 🧠 **Keyword Context Awareness** – Augments replies with relevant insights from a local JSON dataset.
- 🌿 **Aesthetic UI** – Custom blurred background with neon chat bubbles using CSS.
- 📊 **Session Memory** – Keeps track of your chat history per session.
- 🔐 **Secure API Handling** – Keys are accessed via environment variables.
- 🚀 **One-click deployment support** on [Render](https://render.com/).

---

## 💻 Tech Stack

| Area          | Tools Used                                       |
|---------------|--------------------------------------------------|
| Frontend      | Streamlit, HTML/CSS                              |
| Backend       | Python, LangChain, LangChain-Community, Together |
| LLMs          | Mistral 7B, DeepSeek, LLaMA 3.3 Turbo, Cohere    |
| Data Storage  | Local JSON (`MentalHeathHelpDatabase.json`)      |
| Deployment    | Render.com                                       |

---

## 🚀 Getting Started Locally

Follow these steps to set it up on your machine:

```bash
# 1. Clone the repository
git clone https://github.com/Nsk364/AI-Companion-For-Mental-Health-Chat-bot.git
cd AI-Companion-For-Mental-Health-Chat-bot

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys as environment variables
export TOGETHER_API_KEY=your_together_api_key
export COHERE_API_KEY=your_cohere_api_key
# (On Windows use `set` instead of `export`)

# 5. Run the app
streamlit run Chatbot.py
```

---

## 🌐 Deploying to Render

- Make sure the following files are present in the **root** directory:
  - `Chatbot.py`
  - `bg.jpg`
  - `MentalHeathHelpDatabase.json`
- In the **Render dashboard**, set the following:
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `streamlit run Chatbot.py --server.port $PORT`
  - **Environment Variables**: Add `TOGETHER_API_KEY` and `COHERE_API_KEY`

---

## 📁 Project Structure

```
AI-Companion-For-Mental-Health-Chat-bot/
│
├── Chatbot.py                    # Main Streamlit application
├── bg.jpg                        # Background image used in UI
├── MentalHeathHelpDatabase.json  # Local knowledge base of mental health tips
├── requirements.txt              # All Python dependencies
└── README.md                     # You're reading it!
```

---

## 📷 UI Preview

> ✨ A beautifully styled chat interface with blurred glass effect, glowing chat bubbles, and personalized AI companions. *(Add screenshots here if needed)*

---

## 🔒 API Usage Notes

- **Together AI**: You can get a free API key at [https://together.ai](https://together.ai).
- **Cohere**: Sign up and obtain your key at [https://cohere.com](https://cohere.com).

All API keys are loaded using `os.getenv(...)` to avoid hardcoding sensitive information.

---

## 🙋‍♂️ Author

**Nipun Sai Kokonda**  
 @ SRM University, AP  
🔗 GitHub: [@Nsk364](https://github.com/Nsk364)  
📬 Feel free to connect for collaborations or suggestions!

---

## ⭐️ Acknowledgements

- **LangChain & Together AI** for enabling easy access to advanced LLMs.
- **Streamlit** for making beautiful UI development effortless.
- **Cohere** for the amazing Command-Xlarge model.

---

> _This is not a replacement for professional mental health help. It is only meant to provide comfort and motivational support in moments of distress._
