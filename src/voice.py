import os
import speech_recognition as sr
from elevenlabs import generate, play, set_api_key

from dotenv import load_dotenv
load_dotenv()

class JOI_Voice:
    def __init__(self):
        set_api_key(os.getenv("ELEVENLABS_API_KEY"))
        self.recognizer = sr.Recognizer()
    
    def text_to_speech(self, text, voice="21m00Tcm4TlvDq8ikWAM"):
        audio = generate(
            text=text,
            voice=voice,
            model="eleven_monolingual_v1"
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
