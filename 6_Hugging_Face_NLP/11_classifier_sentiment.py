from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


# Cargar el tokenizer y el modelo
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

# Texto en español
texto = "Este producto es excelente y superó mis expectativas."

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