from app.voice_transcriber import listen_and_transcribe
from app.gpt_responder import get_gpt_reply
from app.tts_engine import speak_text
from app.roleplay import get_scenario_prompts  # import the new file

def main():
    print("🔊 SpeakGenie AI Voice Tutor is running...")
    print("📚 Available topics: school, store")
    topic = input("👉 Choose a roleplay topic: ").strip().lower()
    prompts = get_scenario_prompts(topic)

    if not prompts:
        print("❌ Invalid topic selected.")
        return

    for prompt in prompts:
        print(f"🧑 Roleplay: {prompt}")
        speak_text(prompt)
        user_input = listen_and_transcribe()
        print(f"👧 You: {user_input}")
        reply = get_gpt_reply(user_input)
        print(f"🤖 Genie: {reply}")
        speak_text(reply)

if __name__ == "__main__":
    main()
