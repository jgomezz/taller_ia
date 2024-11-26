from transformers import AutoTokenizer, AutoModelForCausalLM

# Cargar el tokenizer y el modelo
# https://huggingface.co/datificate/gpt2-small-spanish
tokenizer = AutoTokenizer.from_pretrained("datificate/gpt2-small-spanish")
model = AutoModelForCausalLM.from_pretrained("datificate/gpt2-small-spanish")

# Definir eos_token y pad_token si no están definidos
if tokenizer.eos_token is None:
    tokenizer.eos_token = '<|endoftext|>'
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Actualizar el modelo si hemos añadido nuevos tokens
model.resize_token_embeddings(len(tokenizer))

# Establecer los IDs de tokens especiales en el modelo
model.config.eos_token_id = tokenizer.eos_token_id
model.config.pad_token_id = tokenizer.pad_token_id

# Verificar que los tokens y sus IDs están correctamente establecidos
print("pad_token_id:", tokenizer.pad_token_id)
print("pad_token:", tokenizer.pad_token)
print("eos_token_id:", tokenizer.eos_token_id)
print("eos_token:", tokenizer.eos_token)

# Frase inicial
entrada = "La inteligencia artificial es"
entrada = "Que es Python?"
entrada = "Que es Java?"
entrada = "Puede generar la suma de 2 numeros enteros en Python?"

# Tokenización
inputs = tokenizer(entrada, return_tensors="pt", padding=True)

# Generación de texto
outputs = model.generate(
    input_ids=inputs['input_ids'],
    attention_mask=inputs.get('attention_mask'),
    max_length=100,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    num_beams=5,
    early_stopping=True,
    eos_token_id=tokenizer.eos_token_id,
    pad_token_id=tokenizer.pad_token_id
)

# Decodificar y mostrar el resultado
texto_generado = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(texto_generado)
