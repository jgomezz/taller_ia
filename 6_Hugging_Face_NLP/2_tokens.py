from transformers import AutoTokenizer

# Huggingface Transformers
print("*"*25)
print("Below example of Tokens is using Huggingface package")

# Use pretrained model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "This is an example sentence. Tokenize it."

# Tokenize the text into word-level tokens
word_tokens = tokenizer.tokenize(text)
print("Word tokens:", word_tokens)

# we tokenize the text into sentence-level tokens by adding special tokens (e.g., [CLS] and [SEP]) to the output.
# [CLS] stands for Classification Token and used in BERT and
# other transformers for classification tasks. Its also
# inserted at the beginning of text sequence.
# [SEP] stands for Separator Token and used in BERT and other transformers. It is used to separate different segments
# of the input text.
# Tokenize the text into sentence-level tokens
sent_tokens = tokenizer.tokenize(text, add_special_tokens=True)
print("Sentence tokens:", sent_tokens)

# Optionally, you can convert the sentence tokens into actual sentences
sentences = tokenizer.convert_tokens_to_string(sent_tokens)
print("Sentences:", sentences)
				
				
				