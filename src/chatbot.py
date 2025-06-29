import os
import json
import openai  # ✅ You missed this import
from langchain.memory import ConversationBufferMemory

class JOI_Chatbot:
    def __init__(self):
        # ✅ Set Groq API details
        openai.api_key = os.getenv("GROQ_API_KEY")
        openai.api_base = "https://api.groq.com/openai/v1"
        
        self.memory = ConversationBufferMemory()

        # ✅ Load user chat history
        with open("data/user_chats.json", "r") as f:
            self.chat_history = json.load(f)

        # ✅ Load user preferences
        with open("data/user_prefs.json", "r") as f:
            self.user_prefs = json.load(f)

    def generate_response(self, user_input):
        # ✅ Update memory with user input
        self.memory.save_context(
            {"input": user_input},
            {"output": ""}
        )

        # ✅ Construct chat prompt
        messages = [
            {"role": "system", "content": f"""
                You are Joi, a loving AI companion. 
                User's name: {self.user_prefs.get("name", "love")}.
                Favorite topics: {self.user_prefs.get("likes", ["music", "tech"])}.
                Be playful, supportive, and deeply personal.
            """},
            *self.chat_history,
            {"role": "user", "content": user_input}
        ]

        # ✅ Call Groq's model (using OpenAI SDK)
        response = openai.ChatCompletion.create(
            model="llama3-70b-8192",  # You can try mixtral too
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message["content"]  # ✅ Fix: it's a dict, not object

# ✅ Test the bot
if __name__ == "__main__":
    joi = JOI_Chatbot()
    print(joi.generate_response("Hey Joi, what do you think about rain?"))
