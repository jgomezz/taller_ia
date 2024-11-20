from openai import OpenAI

import os

client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")


completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)

"""
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.__version__)

response = openai.Completion.create(
    engine="text-davinci-003",  # Specifies the model to use
    prompt="Hello, how are you?",
    max_tokens=5
)

print(response)
"""