from transformers import pipeline
# Install tensorflow and keras packages

# HuggingFace
print("*" * 25)
print("Below example of NER is using HuggingFace package")

# Load the NER model
# It will download large model of size around 1.33 GB
"""
If you are getting error as mentioned below uninstall keras and tensorflow packages.
pip uninstall keras tensorflow

1. RuntimeError: Failed to import transformers.models.bert.modeling_tf_bert because of the following error (look up to see its traceback):
Your currently installed version of Keras is Keras 3, but this is not yet supported in Transformers. Please install the backwards-compatible tf-keras package with `pip install tf-keras`.

2. RuntimeError: Failed to import transformers.models.bert.modeling_tf_bert because of the following error (look up to see its traceback):
“module 'tensorflow._api.v2.compat.v2.__internal__' has no attribute 'register_load_context_function'
"""
nlp_ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

text = "Apple Inc. is headquartered in Cupertino, California, and was founded by Steve Jobs."

# Perform NER
entities = nlp_ner(text)

# Display the detected entities
for entity in entities:
    print(f"Entity: {entity['word']}, Label: {entity['entity']}")

