import os
import numpy as np
import tiktoken
from openai import OpenAI
import uuid
import psycopg
from pgvector.psycopg import register_vector


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# model_name = "text-embedding-3-small"  # text-embedding-3-small, "gpt-5.2"?
model_name = "gpt-5.2"

conn = psycopg.connect(
    "postgresql://rag:rag@localhost:5432/ragdb"
)
register_vector(conn)

def main():
    text = "Hello world! This text will be embedded."

    # Tokenization
    # encoding = tiktoken.encoding_for_model(model_name)
    # tokens = encoding.encode(text)  # BPE (Byte-pair encoding)?
    # print("=== Tokenization ===")
    # print("Text:", text)
    # print("Token count:", len(tokens))
    # print("Tokens:", tokens)

    # Embedding
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    embedding = response.data[0].embedding

    print("\n=== EMBEDDING ===")
    print("Embedding vector length:", len(embedding))
    print("First 10 values:", embedding[:10])

    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO documents (id, source, content, embedding)
            VALUES (%s, %s, %s, %s)
            """,
            (str(uuid.uuid4()), "manual.md", md_text, embedding)
        )
        conn.commit()

    # Numpy conversion (like a into VectorDB)
    vector = np.array(embedding, dtype="float32")

    print("\n=== VECTOR READY FOR DB ===")
    print("Vector dtype:", vector.dtype)
    print("Vector shape:", vector.shape)

    # LLM request
    response = client.responses.create(
        model="gpt-5.2",
        input="Generate a simple Hello World Bourne shell script."
    )

    print("\n=== LLM OUTPUT ===")
    print(response.output_text)


if __name__ == "__main__":
    main()
