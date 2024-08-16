import runpod
from tokenizer import tokenize, embed_text, embed_sentences, embed_words
from fastapi.encoders import jsonable_encoder

def process_input(input):
    text = input['text']
    full_text, sentences, words = tokenize(text)
    # embedded_full_text = embed_text(full_text)
    # embedded_sentences = embed_sentences(sentences)
    embedded_words = embed_words(words)

    return jsonable_encoder({
        # "sentences" : embedded_sentences, 
        "words" : embedded_words
    })

def handler(event):
    return process_input(event['input'])


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})