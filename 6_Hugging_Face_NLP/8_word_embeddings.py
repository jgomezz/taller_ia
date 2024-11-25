from transformers import DistilBertTokenizer, DistilBertModel

# Install PyTorch package

# Huggingface
print("*"*25)
print("Below example of Word Embeddings using Huggingface package")

# Load the pre-trained DistilBERT tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Tokenize a sentence
text = "Hugging Face's Transformers library is fantastic!"
tokens = tokenizer(text, padding=True, truncation=True, return_tensors="pt")

# Load the pre-trained DistilBERT model
model = DistilBertModel.from_pretrained("distilbert-base-uncased")

# Get word embeddings for the tokens
output = model(**tokens)

# Access word embeddings for the [CLS] token (you can access other tokens as well)
word_embeddings = output.last_hidden_state[0]  # [CLS] token's embeddings

# Convert the tensor to a numpy array
word_embeddings = word_embeddings.detach().numpy()

# Print the word embeddings
print(word_embeddings)