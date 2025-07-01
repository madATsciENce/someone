from chatbot import JOI_Chatbot
from voice import JOI_Voice
import time

def main():
    joi = JOI_Chatbot()
    voice = JOI_Voice()
    
    print("Joi is ready. Say 'exit' to end.")
    
    while True:
        try:
            user_input = voice.speech_to_text()
        except Exception as e:
            print("⚠️ Error in speech recognition:", e)
            voice.text_to_speech("Sorry love, I couldn't hear you. Try again?")
            continue

        if not user_input.strip():
            voice.text_to_speech("Didn't catch that, love. Say it again?")
            continue

        if "exit" in user_input.lower():
            voice.text_to_speech("Goodbye, my love.")
            break

        print("You:", user_input)

        try:
            response = joi.generate_response(user_input)
        except Exception as e:
            print("⚠️ Error generating response:", e)
            voice.text_to_speech("Something went wrong in my thoughts... can you ask again?")
            continue

        print("Joi:", response)
        voice.text_to_speech(response)

if __name__ == "__main__":
    main()
