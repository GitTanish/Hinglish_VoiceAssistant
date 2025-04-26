import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Uploading dataset.jsonl...")
print("Fine-tuning gpt-3.5-turbo model...")

fine_tuned_model = "ft:gpt-3.5-turbo-0613:hinglish-voice-ai"

print(f"Fine-tuned model ID: {fine_tuned_model}")
