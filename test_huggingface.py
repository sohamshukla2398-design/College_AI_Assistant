from providers.huggingface_provider import ask_huggingface

answer = ask_huggingface(
    "What is Python? Answer in two simple sentences."
)

print("Hugging Face Response:")
print(answer)
