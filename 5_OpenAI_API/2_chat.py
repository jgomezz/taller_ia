from openai import OpenAI

import os

client = OpenAI()

client.api_key = os.getenv("OPENAI_API_KEY")

def math_chatbot():
    """
    A simple interactive chatbot for answering math-related questions.
    """
    #print("Math Chatbot: Ask me any math-related question. Type 'exit' to quit.")
    print("Math Chatbot: Consultame preguntas de matemática. Escribe 'exit' para salir.")
    
    # Initial conversation context
    conversation = [
#        {"role": "system", "content": "You are a math expert who answers math-related questions accurately and clearly."}
         {"role": "system", "content": "Eres un experto en matematica que responde preguntas en forma clara y concisa."}
    ]
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == "exit":
            print("Math Chatbot: Goodbye!")
            break
        
        # Add the user's input to the conversation
        conversation.append({"role": "user", "content": user_input})
        
        try:
            # Make the API call to OpenAI
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # You can use gpt-4o or gpt-4o-mini
                messages=conversation
            )
            
            # Get the AI's response
            assistant_response = response.choices[0].message.content
            
            # Print the assistant's response
            print(f"Math Chatbot: {assistant_response}")
            
            # Add the assistant's response to the conversation context
            conversation.append({"role": "assistant", "content": assistant_response})
        
        except Exception as e:
            print(f"An error occurred: {e}")


# Run the chatbot
if __name__ == "__main__":
    math_chatbot()


