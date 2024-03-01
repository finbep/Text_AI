from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
import nltk
from scipy.sparse import save_npz

# Assuming the nltk 'punkt' tokenizer is needed
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# 1. Reading data from a text file
def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# 2. Tokenization (demonstrated but not used directly in vectorization)
def tokenize_text(text):
    return word_tokenize(text)

# Reading and tokenizing the text data
file_path = 'data.txt'
text = read_data(file_path)
tokens = tokenize_text(text)  # Tokenized but not directly used in the next step

# 3. Vectorization (TF-IDF)
vectorizer = TfidfVectorizer()
vectorized_data = vectorizer.fit_transform([text])  # Vectorizing the text

# 4. Normalization
normalizer = Normalizer()
normalized_data = normalizer.fit_transform(vectorized_data)

# Saving the normalized data to a file
normalized_data_file = 'normalized_data.npz'
save_npz(normalized_data_file, normalized_data)

print(f'Normalized data saved to {normalized_data_file}')
