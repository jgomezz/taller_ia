from openai import OpenAI

import os

client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")

def example_00() :

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {   "role": "system", 
                "content": "You are a helpful assistant."},
            {   "role": "user",
                "content": "Tell me a joke"}
        ]
    )

def example_01() :
    '''
        Introduction to OpenAI API
    '''
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", 
             "content": "Write a simple Python script to add two numbers."}
        ]
    )

    resp = completion.choices[0].message
    return resp

def example_02() :
    '''
        Using ChatGPT Models
    '''
    completion = client.chat.completions.create(
#        model="gpt-4o",
        model="gpt-4o-mini",
        messages=[
            {"role": "user", 
             "content": "Write a simple Python script to add two numbers."}
        ]
    )

    resp = completion.choices[0].message
    return resp


if __name__ == "__main__" :
    
    resp = example_01()
    print(resp)
    print(resp.content)



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