from transformers import AutoTokenizer, AutoModelWithLMHead

# Cargar el tokenizer y el modelo
tokenizer = AutoTokenizer.from_pretrained("datificate/gpt2-small-spanish")
model = AutoModelWithLMHead.from_pretrained("datificate/gpt2-small-spanish")

# Frase inicial
entrada = "La inteligencia artificial es"

# Tokenización
inputs = tokenizer.encode(entrada, return_tensors="pt")

# Generación de texto
outputs = model.generate(
    inputs,
    max_length=50,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    early_stopping=True
)

# Decodificar y mostrar el resultado
texto_generado = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(texto_generado)
