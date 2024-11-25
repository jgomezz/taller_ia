import json
from openai import OpenAI
import os
import time

# https://platform.openai.com/docs/guides/fine-tuning/

client = OpenAI()

FILENAME_DATASET = '3_data_training.jsonl'
client.api_key = os.getenv("OPENAI_API_KEY")

def create_dataset():
    '''
        Prepare and save a fine-tuning dataset in JSONL format.
    '''
    data = [
        {   
            "messages": [
                {"role": "user", "content": "Cual es tu horario laboral?"}, 
                {"role": "assistant", "content": "El horario laboral es de 8 am a 6 pm, de Lunes a Viernes."}
                ]
        },
        {
            "messages": [
                {"role": "user", "content": "A que hora se almuerza en el trabajo?"}, 
                {"role": "assistant", "content": "Se almuerza de 1 pm a 2 pm , de Lunes a Viernes."}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "Pueden pedir permiso laboral?"}, 
                {"role": "assistant", "content": "Se puede solicitar un dia de permiso laboral por temas personales"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "Tienes gratificaciones?"}, 
                {"role": "assistant", "content": "Tengo gratificaciones en los meses de Julio y Diciembre"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "En que meses puedes pedir vacaciones?"}, 
                {"role": "assistant", "content": "Se suele pedir vacaciones en los meses de Enero y Febrero"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "Tienen acceso a utilidades?"}, 
                {"role": "assistant", "content": "No se obtiene utilidades porque es una empresa sin fines de lucro"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "Tienes acceso a alguna capacitación?"}, 
                {"role": "assistant", "content": "Anualmente todo trabajador tiene derecho a una capacitación"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "Tu empresa pertenece al sector público o privado?"}, 
                {"role": "assistant", "content": "La empresa donde laboro pertenece al sector privado"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "Debes tener algún tipo de titulación para trabajar?"}, 
                {"role": "assistant", "content": "Para poder trabajar debes tener un titulo universitario o técnico"}
            ]
        },
        {
            "messages": [
                {"role": "user", "content": "Realizan alguna actividades adicionales?"}, 
                {"role": "assistant", "content": "Anualmente tenemos actividades culturarles fuera del horario laboral"}
            ]
        }
    ]

    with open(FILENAME_DATASET, 'w') as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')

def  upload_dataset() :
    '''
    
    '''
    # Upload the dataset
    file_response = client.files.create(
        file=open(FILENAME_DATASET, 'rb'),
        purpose='fine-tune'
    )

    file_id = file_response.id
    print(f"Uploaded file ID: {file_id}")

    return file_id


def fine_tune_model(file_id):
    """
    Initiate fine-tuning using the uploaded file.
    """
    try:
        response = client.fine_tuning.jobs.create(
                        training_file=file_id,
                        model='gpt-4o-mini-2024-07-18'
                    )
        print(f"Fine-tuning initiated. Fine-tune ID: {response.id}")
        return response.id
    except Exception as e:
        print(f"Error starting fine-tuning: {e}")
        return None
    
def monitor_fine_tune(fine_tune_id):
    """
    Monitor the status of the fine-tuning process.
    """
    while True:
        status_response = client.fine_tuning.jobs.retrieve(fine_tune_id)
        status = status_response.status
        print(f"Job Status: {status}")
        if status in ['succeeded', 'failed', 'cancelled']:
            print("Fine-tuning completed.")
            if status == 'failed':
                print("Fine-tuning job failed.")
                if hasattr(status_response, 'error') and status_response.error is not None:
                    print(f"Error message: {status_response.error.message}")
                else:
                    print("No error message provided.")
            print(f"Fine-tuned model: {status_response.fine_tuned_model}")
            return status_response.fine_tuned_model
            
        time.sleep(20)  # Wait for 20 seconds before checking again

def use_fine_tuned_model(model_id, prompt):
    """
    Use the fine-tuned model to generate a response.
    """
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error using fine-tuned model: {e}")
        return None

if __name__ == '__main__':

     # Step 1: Prepare Dataset
    create_dataset()

    # Step 2: Upload Dataset
    file_id = upload_dataset()
    if not file_id:
        exit(-1)

    # Step 3: Fine-Tune Model
    fine_tune_id = fine_tune_model(file_id)
    if not fine_tune_id:
        exit(-1)

    # Step 4: Monitor Fine-Tuning
    # Fine-tuned model: ft:gpt-4o-mini-2024-07-18:personal::AXHeyHAt
    model_id = monitor_fine_tune(fine_tune_id)
    if not model_id:
        exit(-1)

    # Step 5: Use the Fine-Tuned Model
    print("\nFine-tuned model ready for use!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = use_fine_tuned_model(model_id, user_input + "\n")
        print(f"Bot: {response}")
