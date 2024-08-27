import torch
from sentence_transformers import SentenceTransformer

MODEL_ID = "Snowflake/snowflake-arctic-embed-m-v1.5"

model = SentenceTransformer(
    MODEL_ID, model_kwargs=dict(add_pooling_layer=False),
)

model.to('cuda')

def get_embeddings(texts):
    embeddings = model.encode(texts, device='cuda')
    return embeddings