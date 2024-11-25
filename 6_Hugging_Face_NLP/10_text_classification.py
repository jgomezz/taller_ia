from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

import torch

# Hugging Face
print("*"*25)
print("Below example of Text Analysis using Hugging Face package")

# Sample text data”
texts = ["This is a positive sentence.", "This is a negative sentence.", "A neutral statement here."]
				
# Preprocess text and load pre-trained model
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')

# Tokenize and encode the text
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# Perform text classification
outputs = model(**inputs)

# Get predicted labels and probabilities
logits = outputs.logits
predicted_labels = torch.argmax(logits, dim=1)

# Map predicted labels to human-readable class names
class_names = ['positive', 'negative', 'neutral']

for i, text in enumerate(texts):
    print(f"Text: {text}")
    print(f"Predicted Label: {class_names[predicted_labels[i]]}")
    print("")
