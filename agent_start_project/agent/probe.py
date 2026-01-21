import os
import numpy as np
import tiktoken
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    text = "Hello world! This text will be embedded."

    # Tokenization
    encoding = tiktoken.encoding_for_model("text-embedding-3-small")
    tokens = encoding.encode(text)

    print("=== Tokenization ===")
    print("Text:", text)
    print("Token count:", len(tokens))
    print("Tokens:", tokens)

    # Embedding
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    embedding = response.data[0].embedding

    print("\n=== EMBEDDING ===")
    print("Embedding vector length:", len(embedding))
    print("First 10 values:", embedding[:10])

    # Numpy conversion (like a into VectorDB)
    vector = np.array(embedding, dtype="float32")

    print("\n=== VECTOR READY FOR DB ===")
    print("Vector dtype:", vector.dtype)
    print("Vector shape:", vector.shape)

if __name__ == "__main__":
    main()
