from openai import OpenAI
import os

import asyncio

client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")


def generate_code(prompt, language='Python'):
    messages = [
        {"role": "system", "content": f"Eres un experto en programación que escribes codigo en {language}."},
        {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        max_tokens=300,
        temperature=0,
    )
    code = response.choices[0].message.content.strip()
    return code

def explain_code(code, language='Python'):
    messages = [
        {"role": "system", "content": f"Eres un experto en programación que conoce el codigo de {language} "},
        {"role": "user", "content": f"Explicame el siguiente código :\n\n{code}"}
    ]
    response =  client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        max_tokens=500,
        temperature=0.5,
    )
    explanation = response.choices[0].message.content.strip()
    return explanation


if __name__ == '__main__':

    prompt = "Escribe un código en Python que me permita simular el protocolo TCP ."
    code = generate_code(prompt)
    print(f"Código generado:\n{code}")

    explanation = explain_code(code)
    print(f"Explicacion:\n{explanation}")
