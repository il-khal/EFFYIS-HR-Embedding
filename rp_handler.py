import runpod
from tokenizer import process_text
from model import get_embeddings
from fastapi.encoders import jsonable_encoder

def process_input(input):
    text = input['text']
    processed_text = process_text(text)
    embeddings = get_embeddings(processed_text)

    return jsonable_encoder({
        embeddings: embeddings
    })

def handler(event):
    return process_input(event['input'])


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})