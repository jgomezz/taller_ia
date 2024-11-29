from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
# Cargar el tokenizer y el modelo
# https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

# Texto en español
texto = "Este producto es excelente y superó mis expectativas."
# texto = "Este producto no es bueno y apenas cubre algo de mis expectativas."
# texto = "Este producto no es bueno y no cubre mis expectativas."

# Tokenización
inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)

# Inferencia
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits

# Obtener la predicción
probabilidades = torch.nn.functional.softmax(logits, dim=-1)
estrellas = torch.argmax(probabilidades, dim=1).item() + 1  # Agregar 1 porque el índice comienza en 0

print(f"Calificación de sentimiento: {estrellas} estrellas")

'''
indice_pred = torch.argmax(probabilidades, dim=1).item()
etiquetas = ['Negativo', 'Neutro', 'Positivo']
sentimiento = etiquetas[indice_pred]
print(f"Sentimiento: {sentimiento}")
'''