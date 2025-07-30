
# 🎙️ SpeakGenie AI Voice Tutor

**SpeakGenie** is an interactive AI-powered voice tutor for kids. It listens to what they say, understands with GPT, and speaks back—helping them practice English naturally through fun roleplay scenarios like “school” or “shopping”.

---

## ✨ Features

- 🎧 Real-time speech-to-text using [Vosk](https://alphacephei.com/vosk/)
- 🧠 Smart, friendly responses powered by OpenAI GPT-3.5
- 🔈 Clear spoken replies using `pyttsx3` TTS engine
- 🎭 Built-in fun roleplay topics (e.g., school, store) to engage children

---

## 🚀 How to Run

```bash
python app/main.py
```

---

## ⚙️ Setup

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Add your OpenAI API key in a `.env` file at the root level:

```
OPENAI_API_KEY=sk-xxx
```

---

## 📁 Project Structure

```
ai-voice-chatbot/
├── app/
│   ├── main.py                # Main script to run the voice tutor
│   ├── gpt_responder.py       # GPT reply logic
│   ├── voice_transcriber.py   # Vosk-based voice to text
│   ├── tts_engine.py          # Text-to-speech output
│   └── roleplay.py            # Prompt flow and topics
├── static/
│   └── audio/
│       └── emojis.json        # Optional fun elements
├── vosk-model/                # Offline Vosk language model
├── .env                       # Your API key (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 💡 Use Case

Perfect for:
- Young learners practicing English
- Fun speaking activities at home or school
- Building confidence in conversational English

---

## 🤖 Tech Stack

- Python 3.10+
- Vosk (offline STT)
- OpenAI GPT (language understanding)
- pyttsx3 (text-to-speech)
- dotenv

---

## 📌 Note

This app currently uses OpenAI's GPT. Make sure you have enough quota on your account. You can replace it with Gemini if needed, with a few small tweaks.

---

## 🛠️ Future Ideas

- Web-based version
- More engaging voice personalities
- Progress tracking for learners

---

Built with ❤️ for AI learning by [Anshi Goyal](https://github.com/aansheeagrwal)
