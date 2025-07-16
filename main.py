from txtai import Embeddings
import json
import time

# Load the local embeddings index
embeddings = Embeddings({"path": "sentence-transformers/all-MiniLM-L6-v2", "content": True})
embeddings.load("wiki")

print("Ask a question (type 'exit' to quit):")

while True:
    query = input("****\n>> ")
    if query.lower() in {"exit", "quit"}:
        break

    # Search top 3 results
    start=time.time()
    results = embeddings.search(query, 10)
    print(f"Time elapsed: {time.time() - start:.6f} seconds\n")

    for i in results:
        print("id:", i['id'])
        print("text", i['text'])
        print("score:", i['score'], "\n")

    print(f"Time elapsed: {time.time() - start:.6f} seconds\n")
    print("---\n")

