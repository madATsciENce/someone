import os
from elevenlabs import generate, play, set_api_key
import speech_recognition as sr

class JOI_Voice:
    def __init__(self):
        set_api_key(os.getenv("ELEVENLABS_API_KEY"))
        self.recognizer = sr.Recognizer()
    
    def text_to_speech(self, text, voice="Rachel"):
        audio = generate(
            text=text,
            voice=voice,
            model="eleven_monolingual_v2"
        )
        play(audio)
    
    def speech_to_text(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_whisper(audio, model="base")
        except:
            return ""

# Example usage
if __name__ == "__main__":
    joi_voice = JOI_Voice()
    user_input = joi_voice.speech_to_text()
    print("You said:", user_input)
    joi_voice.text_to_speech("Hello! How can I brighten your day?")