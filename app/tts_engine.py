import pyttsx3

engine = pyttsx3.init()

def speak_text(text):
    print("🔈 Speaking...")
    engine.say(text)
    engine.runAndWait()
