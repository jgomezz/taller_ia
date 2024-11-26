from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# Cargar el tokenizer y el modelo
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

# Establecer el idioma de origen y destino
tokenizer.src_lang = "en_XX"
texto_en = "Artificial intelligence is transforming the world."
texto_en = '''
Hugging Face, Inc. is an American company incorporated under the Delaware General Corporation Law[1] and based in New York City that develops computation tools for building applications using machine learning. It is most notable for its transformers library built for natural language processing applications and its platform that allows users to share machine learning models and datasets and showcase their work.
'''

# Tokenización
encoded = tokenizer(texto_en, return_tensors="pt")

# Generación de la traducción
generated_tokens = model.generate(**encoded, forced_bos_token_id=tokenizer.lang_code_to_id["es_XX"])

# Decodificar y mostrar la traducción
traduccion = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
print("Traducción al español:")
print(traduccion)
