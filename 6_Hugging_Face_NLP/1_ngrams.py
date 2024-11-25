
from transformers import AutoTokenizer

print("*" * 25)
print("Below example of N Grams is using Hugging Face package")

text = "This is an example sentence for creating n-grams with Hugging Face Transformers."
				
# Choose a pretrained tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the text
tokens = tokenizer.tokenize(text)

# Generate bigrams
bigrams = [(tokens[i], tokens[i + 1]) for i in range(len(tokens) - 1)]

# Generate trigrams
trigrams = [(tokens[i], tokens[i + 1], tokens[i + 2]) for i in range(len(tokens) - 2)]

# Print the bigrams
for bigram in bigrams:
    print(bigram)

# Print the trigrams
for trigram in trigrams:
    print(trigram)

