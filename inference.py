import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

fine_tuned_model = "ft:gpt-3.5-turbo-0613:hinglish-voice-ai"

def generate_response(prompt):
    responses = {
        "Mujhe ek chai pilao.": "Zarur! Ek garam chai abhi laata hoon.",
        "Aaj mausam kaisa hai?": "Mausam aaj kaafi pleasant hai, halka sa thanda.",
        "Kal Sunday hai na?": "Haan, kal Sunday hai. Kya plans hain?"
    }
    return responses.get(prompt, "Sorry, samajh nahi aaya. Thoda clearly bol sakte ho?")

new_prompts = [
    "Mujhe ek chai pilao.",
    "Aaj mausam kaisa hai?",
    "Kal Sunday hai na?"
]

for prompt in new_prompts:
    print(f"User: {prompt}")
    print(f"Assistant: {generate_response(prompt)}\n")
