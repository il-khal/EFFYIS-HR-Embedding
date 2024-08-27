import runpod
from tokenizer import process_text
from model import get_embeddings
from fastapi.encoders import jsonable_encoder

def process_input(input):
    text = input['text']
    processed_text = process_text(text)
    embeddings = get_embeddings(processed_text)
    
    result = [
        {"sentence": sentence, "embedding": embedding.tolist()} for sentence, embedding in zip(processed_text, embeddings)
    ]

    return jsonable_encoder({
        "embeddings": result
    })

def handler(event):
    return process_input(event['input'])


if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})