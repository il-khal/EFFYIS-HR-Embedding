import runpod
from tokenizer import tokenize, embed_text, embed_sentences, embed_words


def process_input(input):
    text = input['text']
    full_text, sentences, words = tokenize(text)
    embedded_full_text = embed_text(full_text)
    embedded_sentences = embed_sentences(sentences)
    embedded_words = embed_words(words)

    return {
        "Full text" : embedded_full_text,
        "Sentences" : embedded_sentences, 
        "Words" : embedded_words,
    }

def handler(event):
    return process_input(event['input'])


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})