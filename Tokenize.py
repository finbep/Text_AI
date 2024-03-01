from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# 1. Reading data from a text file
def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# 2. Tokenization
def tokenize_text(text):
    return word_tokenize(text)

# Assuming the data is in 'data.txt'
file_path = 'data.txt'
text = read_data(file_path)
tokens = tokenize_text(text)

# Since TfidfVectorizer expects raw text, it internally tokenizes the text.
# We directly move to vectorization using the original text data.
# 3. Vectorization
vectorizer = TfidfVectorizer()
vectorized_data = vectorizer.fit_transform([text])  # Passing text as a list

# 4. Normalization
normalizer = Normalizer()
normalized_data = normalizer.fit_transform(vectorized_data)

# Now 'normalized_data' is ready for machine learning models
