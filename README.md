This project builds on a txtai project to query a vectorized extraction of English Wikipedia.  The embeddings/documents only cover the introductory section of each Wikipedia entry.

The project uses uv for dependency management.

Clone the repo and sync the packages with

sync packages

`uv sync`

Create a subfolder called `wiki` and populate it with the following files from

https://huggingface.co/NeuML/txtai-wikipedia/tree/main

* config.json
* documents
* embeddings

then run the demo  with 

 `KMP_DUPLICATE_LIB_OK=TRUE uv run main.py`

 The you'll be prompted for search terms and shown 10 results.

 demo at

 https://asciinema.org/connect/e03dc230-620c-42c3-9b58-c161fa42bba7
