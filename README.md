# 🎙️ SpeakGenie: AI Voice Tutor for Kids

**SpeakGenie** is a real-time AI-powered voice tutor designed to help children practice conversational English in a fun and interactive way. It listens, understands, and responds — like a friendly speaking partner!

Powered by:
- 🔊 **Vosk** for real-time voice transcription
- 🧠 **OpenAI GPT (3.5)** for generating replies
- 🗣️ **pyttsx3** for speaking back responses

---

## ✨ Key Features

✅ Real-time speech recognition  
✅ Friendly and age-appropriate GPT-powered responses  
✅ Natural voice feedback using text-to-speech  
✅ Interactive **roleplay scenarios** (e.g., school, shopping, greetings)  
✅ Easy to extend with new topics or use cases  

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/aansheeagrwal/ai-voice-chatbot.git
cd ai-voice-chatbot
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
```ini
OPENAI_API_KEY=your-openai-api-key
```
###4. Run the Tutor
```bash
python app/main.py
```
## 🛠️ Folder Structure
```bash
.
├── app/
│   ├── main.py               # Main driver for the app
│   ├── gpt_responder.py      # Handles GPT replies
│   ├── voice_transcriber.py  # Transcribes user speech using Vosk
│   ├── tts_engine.py         # Speaks replies aloud
│   └── roleplay.py           # Roleplay topic prompts
├── static/
│   └── audio/                # Placeholder for any static audio/emojis
├── vosk-model/               # Vosk speech model (you can download smaller/lighter models)
├── .env                      # Your API key (should NOT be pushed)
├── requirements.txt          # All Python dependencies
└── README.md                 # This file
```

##🤖 Tech Stack
* Python 3.10+

* Vosk for offline voice transcription

* OpenAI GPT-3.5 for natural replies

* pyttsx3 for voice output

## 👩‍💻 Author
Anshi Goyal

