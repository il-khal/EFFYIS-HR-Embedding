## Project Report: API for Text Tokenization and Embedding Generation 

### Introduction 

This project involved creating an API that processes textual input from a PDF, tokenizes the text, and generates embeddings using SpaCy. The goal is to provide a system that can efficiently handle and analyze text data for various applications, such as matching resumes with job descriptions. This report will discuss the implementation of the API and briefly cover the similarity matching done in Java.

### Project Overview 

The API was built to take textual input, process it, and return the processed data and embeddings. The following are the key functionalities of the API:
 
1. **Text Tokenization** : Convert the text into sentences and words, cleaning the text and removing stop words.
 
2. **Embedding Generation** : Generate vector representations (embeddings) for the entire text, individual sentences, and words.
 
3. **Similarity Matching** : Find the most relevant resumes based on cosine similarity between the embeddings of the query and the stored resume data.

### System Design 

#### 1. API Endpoints and Functionality 

The API is designed to process input text through the following steps:
 
- **Text Tokenization** : The text is cleaned, tokenized into sentences, and then further tokenized into words.
 
- **Embedding Generation** : After tokenization, the API generates embeddings for each sentence and word using SpaCy's English model.
 
- **Return Results** : The API returns the sentences and their embeddings, as well as words and their embeddings, in a JSON format.

#### 2. Implementation Details 

The implementation consists of two main parts:
 
1. **Tokenization and Embedding Functions** : Implemented using Python and SpaCy.
 
2. **API Handler** : Implemented to handle requests and responses, originally meant to run on Runpod and later exposed using ngrok.

### Implementation 

#### 1. Tokenization and Embedding Using SpaCy 

The Python code uses SpaCy for natural language processing tasks. Here’s how the different components are implemented:
 
- **Tokenize Function** : This function tokenizes the text into sentences and words, removing punctuation and stop words (including both English and French stop words).
 
- **Embed Functions** : These functions create embeddings for the text, sentences, and words using SpaCy’s language model.

Here is the core part of the implementation:


```python
import spacy
import string
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop_words

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def tokenize(text):
    full_text = clean(text)
    sentences = to_sentences(text)
    words = [j for i in sentences for j in to_words(i)]
    return full_text, sentences, words

def clean(text):
    text = ' '.join(text.split()).lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

def to_words(text):
    doc = nlp(text)
    stop_words = set(nlp.Defaults.stop_words).union(fr_stop_words)
    words = [token.text for token in doc if token.text not in stop_words]
    return words

def to_sentences(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    sentences = [clean(sent) for sent in sentences]
    return sentences

def embed_text(text):
    doc = nlp(text)
    return doc.vector

def embed_sentences(sentences):
    embeddings = [{"sentence": sentence, "embedding": nlp(sentence).vector.tolist()} for sentence in sentences]
    return embeddings

def embed_words(words):
    embeddings = [{"word": word, "embedding": nlp(word).vector.tolist()} for word in words]
    return embeddings
```

#### 2. API Handler and Processing 
The handler function processes the input, tokenizes the text, and generates embeddings. The API is exposed using `ngrok` when running locally due to credit running out on Runpod. The code snippet below outlines the handler function:

```python
import runpod
from tokenizer import tokenize, embed_text, embed_sentences, embed_words
from fastapi.encoders import jsonable_encoder

def process_input(input):
    text = input['text']
    full_text, sentences, words = tokenize(text)
    embedded_sentences = embed_sentences(sentences)
    embedded_words = embed_words(words)

    return jsonable_encoder({
        "sentences": embedded_sentences, 
        "words": embedded_words
    })

def handler(event):
    return process_input(event['input'])

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
```

### Similarity Matching 

The similarity matching component was developed in Java, focusing on finding the closest resume to the query based on cosine similarity:
 
1. **Cosine Similarity Calculation** : The cosine similarity between each word in the query and all words in the resumes is calculated.
 
2. **Max Similarity Score** : For each word in the query, the maximum similarity score with the resumes is identified.
 
3. **Average Score** : The average of the maximum scores is computed to rank the resumes by relevance.

This approach ensures that resumes with the most semantically relevant content to the query are identified effectively.

### Conclusion 

The API developed in this project successfully tokenizes and generates embeddings for text input using SpaCy. By integrating this with a Java-based similarity matching system, the project provides a comprehensive solution for efficient text processing and comparison. This system can be leveraged in various applications such as resume parsing and matching, enhancing the overall recruitment process. Future improvements could include optimizing the embedding storage and retrieval process for larger datasets.
