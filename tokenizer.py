from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop_words
import spacy
import string

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def tokenize(text):
    full_text = clean(text)
    sentences = to_sentences(text)
    words = [j for i in sentences for j in to_words(i)]

    return full_text, sentences, words

def clean(text):
    # Remove punctuation and extra spaces
    text = ' '.join(text.split()).lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

def to_words(text):
    # Tokenize text into words and remove stop words
    doc = nlp(text)
    stop_words = set(nlp.Defaults.stop_words).union(fr_stop_words)
    words = [token.text for token in doc if token.text not in stop_words]
    return words

def to_sentences(text):
    # Tokenize text into sentences
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    sentences = [clean(sent) for sent in sentences]
    return sentences