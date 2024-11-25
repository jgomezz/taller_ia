from openai import OpenAI

import os

client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")

def example_00() :

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
#            { "role": "system", "content": "You are a helpful assistant."},
#            { "role": "user", "content": "Tell me a joke"}
            { "role": "system", "content": "Eres un asistente útil."},
            { "role": "user", "content": "Cuentame una broma"}
        ]
    )

    resp = completion.choices[0].message
    return resp

def example_01() :
    '''
        Introduction to OpenAI API
    '''
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user",  "content": "Write a simple Python script to add two numbers."}
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
            {"role": "user",  "content": "Write a simple Python script to add two numbers."}
        ]
    )

    resp = completion.choices[0].message
    return resp


def example_03() :
    '''
        Using ChatGPT Models
    '''
    completion = client.chat.completions.create(
        model="gpt-4",
#        model="gpt-4o-mini",
#        model="gpt-4o",
        messages=[
            {"role": "user",  "content": "Cuantas R hay en la palabra strawberry?."}
        ]
    )

    resp = completion.choices[0].message
    return resp



if __name__ == "__main__" :
    
    resp = example_03()
    print(resp.content)
