from transformers import pipeline

# HuggingFace
print("*" * 25)
print("Below example of Sentiment using HuggingFace package")

# Load a pre-trained sentiment analysis model
nlp = pipeline("sentiment-analysis")

# Sample text for sentiment analysis
text = "I love this product! It's amazing."

# Perform sentiment analysis
results = nlp(text)

# Output results
for result in results:
    label = result["label"]
    score = result["score"]
    print(f"Sentiment Label: {label}, Score: {score:.4f}")
