import json

def create_data_trainig():

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
        }
    ]

    with open('3_data_training.json', 'w') as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')

if __name__ == '__main__':

    create_data_trainig()