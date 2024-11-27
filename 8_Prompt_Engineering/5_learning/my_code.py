import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

texto = "Hola, ¿cómo estás? Espero que todo vaya bien."
tokens = word_tokenize(texto)
stop_words = set(stopwords.words('spanish'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
ps = PorterStemmer()
stemmed = [ps.stem(word) for word in filtered_tokens]

print("Tokens:", tokens)
print("Tokens filtrados:", filtered_tokens)
print("Tokens con stemming:", stemmed)