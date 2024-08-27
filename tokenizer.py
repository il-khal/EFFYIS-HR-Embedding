import re
import nltk

nltk.download('punkt_tab')

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s.,]', '', text)  
    return text.strip()

def tokenize_into_sentences(text):
    from nltk.tokenize import sent_tokenize
    return sent_tokenize(text)

def process_text(text):
    cleaned_text = clean_text(text)
    sentences = tokenize_into_sentences(cleaned_text)
    return sentences