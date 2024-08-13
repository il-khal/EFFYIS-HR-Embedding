import nltk
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('stopwords')

# Clean the text by removing punctuation, converting it to lower case, and removing extra spaces
def clean(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    text = ' '.join(text.split())
    return text

# Split the text into words
def to_words(text):
    words = word_tokenize(text)

    stop_words_french = set(stopwords.words('french'))
    stop_words_english = set(stopwords.words('english'))
    stop_words = stop_words_french.union(stop_words_english)
    
    words = [word for word in words if word not in stop_words]
    return words

# Split the text into sentences
def to_sentences(text):
    sentences = sent_tokenize(text)
    return sentences

# Example for testing with multiple languages
text = "Hello tout le monde! Ceci est un test text. Let's clean, tokenize, and split it."
cleaned_text = clean(text)
words = to_words(cleaned_text)
sentences = to_sentences(cleaned_text)

print(f"Cleaned Text: {cleaned_text}")
print(f"Words: {words}")
print(f"Sentences: {sentences}")
