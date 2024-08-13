import runpod
from tokenizer import tokenize



def process_input(input):
    text = input['text']
    full_text, sentences, words = tokenize(text)

    return {
        "Full text" : full_text,
        "Sentences" : sentences, 
        "Words" : words
    }

def handler(event):
    return process_input(event['input'])


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})