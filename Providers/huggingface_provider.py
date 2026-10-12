
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=HF_TOKEN
)


def ask_huggingface(question):
    if not HF_TOKEN:
        return "Error: HF_TOKEN is missing from the .env file."

    try:
        response = client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful college AI assistant. "
                        "Answer clearly and simply."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=300
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"Hugging Face request failed: {error}"
