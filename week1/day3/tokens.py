import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key= my_api_key)

model = "llama-3.3-70b-versatile"
role:"user"

#//3 prompts

prompt1 = "Hi!"
prompt2 = "Explain time travel in Detail but under 100 words"
prompt3 = "Write a 1000 word essay on Machine learning"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message={
        "role": "user",
        "content": prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages = messages, max_tokens=5000)
    usage = response.usage
    print(f"\nPrompt: {prompt}")
    print(f"Prompt Tokens: {usage.prompt_tokens}")
    print(f"Completion Tokens: {usage.completion_tokens}")
    print(f"Total Tokens: {usage.total_tokens}")
    print(f"Finish Reason: {response.choices[0].finish_reason}")

# prompt="Do you know Padho with Pratyush"
# # message me role and content
# message={
#     "role": role,
#     "content": prompt
# }

# messages=[message]

# response=client.chat.completions.create(model=model, messages=messages)