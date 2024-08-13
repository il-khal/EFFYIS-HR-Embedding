import spacy
import string

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def clean(text):
    # Remove punctuation and extra spaces
    text = ' '.join(text.split()).lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

def to_words(text):
    # Tokenize text into words and remove stop words
    doc = nlp(text)
    stop_words = set(nlp.Defaults.stop_words)
    words = [token.text for token in doc if token.text not in stop_words]
    return words

def to_sentences(text):
    # Tokenize text into sentences
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    sentences = [clean(sent) for sent in sentences]
    return sentences

# Example usage with mixed language text
text = "Hello tout le monde! Ceci est un test text. Let's clean, tokenize, and split it."
cleaned_text = clean(text)
words = to_words(cleaned_text)
sentences = to_sentences(text)

print(f"Cleaned Text: {cleaned_text}")
print(f"Words: {words}")
print(f"Sentences: {sentences}")
