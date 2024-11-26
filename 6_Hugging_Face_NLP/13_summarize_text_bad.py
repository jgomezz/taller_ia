from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

'''
# Cargar el tokenizer y el modelo
# https://huggingface.co/JorgeSarry/est5-summarize
tokenizer = AutoTokenizer.from_pretrained("JorgeSarry/est5-summarize")
model = AutoModelForSeq2SeqLM.from_pretrained("JorgeSarry/est5-summarize")

# Texto largo en español
texto = """
El aprendizaje automático es una rama de la inteligencia artificial que permite a las máquinas aprender 
de datos y mejorar con la experiencia, sin ser explícitamente programadas para cada tarea. Es fundamental 
en la era de los big data, donde los algoritmos pueden encontrar patrones y hacer predicciones útiles.
"""


# Preparar entrada
inputs = tokenizer.encode("resumir: " + texto, return_tensors="pt", max_length=512, truncation=True)

# Generación del resumen
outputs = model.generate(inputs, max_length=300, min_length=40, length_penalty=5.0, num_beams=2)

# Decodificar y mostrar el resumen
resumen = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Resumen:")
print(resumen)
'''
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Cargar el tokenizer y el modelo
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("vgaraujov/t5-base-spanish")
model = AutoModel.from_pretrained("vgaraujov/t5-base-spanish")

# Texto largo en español
texto = """
El aprendizaje automático es una rama de la inteligencia artificial que permite a las máquinas aprender de datos y mejorar con la experiencia, sin ser explícitamente programadas para cada tarea. Es fundamental en la era de los big data, donde los algoritmos pueden encontrar patrones y hacer predicciones útiles.
"""

# Preparar entrada
inputs = tokenizer.encode("summarize: " + texto, return_tensors="pt", max_length=512, truncation=True)

# Generación del resumen
outputs = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

# Decodificar y mostrar el resumen
resumen = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Resumen:")
print(resumen)
