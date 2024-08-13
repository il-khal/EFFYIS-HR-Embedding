import spacy
import string

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

class Tokenizer:
    def clean(self, text):
        # Remove punctuation and extra spaces
        text = ' '.join(text.split()).lower()
        text = ''.join([char for char in text if char not in string.punctuation])
        return text

    def to_words(self, text):
        # Tokenize text into words and remove stop words
        doc = nlp(text)
        stop_words = set(nlp.Defaults.stop_words)
        words = [token.text for token in doc if token.text not in stop_words]
        return words

    def to_sentences(self, text):
        # Tokenize text into sentences
        doc = nlp(text)
        sentences = [sent.text for sent in doc.sents]
        sentences = [self.clean(sent) for sent in sentences]
        return sentences