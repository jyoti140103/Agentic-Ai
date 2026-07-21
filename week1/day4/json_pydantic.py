import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import json
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API not found")

# Create the Groq client
client = Groq(api_key=my_api_key)

# Model name
model = "llama-3.3-70b-versatile"


# Structure it
class Ticket(BaseModel):
    name: str
    email: str
    issue: str


schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema and give a JSON output.

Schema:
{schema}
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

text = """
Hello My name is Pratyush.
Yesterday I broke up with my girlfriend Sheetal.
I have an iPhone which is not working at all.
My address is Delhi.
My email is abc@gmail.com.
My contact number is 82134.
"""

prompt = f"""
This is a customer ticket. Please extract the personal information from this.

{text}
"""

message = {
    "role": "user",
    "content": prompt
}

messages = [message_system, message]

# Call the Groq API
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

answer = response.choices[0].message.content

# Read the JSON
raw_json = answer
data_file = json.loads(raw_json)

# Validate using Pydantic
ticket = Ticket(**data_file)

# Print the values
print(ticket.name)
print(ticket.email)
print(ticket.issue)