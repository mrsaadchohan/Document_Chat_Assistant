# Chat with PDF — Generative AI PDF Q&A App
Welcome to Chat with PDF, a powerful app that lets you interactively chat with any PDF document using the latest advancements in Generative AI! Built with GPT-4, LangChain, FAISS, and Streamlit, this app enables you to upload PDFs and instantly get contextual answers to your questions — making document understanding faster and easier than ever.

## Features
- Upload any PDF file — Easily load your documents into the app
- Ask questions naturally — Query the content with simple questions
- Get contextual answers — Responses are generated based on the specific content of the PDF
- Powered by GPT-4 & LangChain — State-of-the-art language model and chain management
- Efficient similarity search — FAISS vector search for fast retrieval
- Streamlit UI — Clean, interactive, and easy to use interface


## How It Works
- Upload PDF — The app splits the PDF into smaller text chunks.
- Embedding Generation — Each chunk is converted into vector embeddings using OpenAI Embeddings.
- Vector Indexing — FAISS indexes these embeddings for quick similarity search.
- Query Processing — When you ask a question, the app embeds your query and retrieves the most relevant chunks.
- Answer Generation — GPT-4 processes the retrieved chunks and generates a contextual answer.
  This approach is called Retrieval-Augmented Generation (RAG), allowing the LLM to use private or domain-specific data efficiently.


## Getting Started
### Prerequisites
Python 3.8+
OpenAI API key (for GPT-4 and embeddings

## Installation
- git clone https://github.com/mrsaadchohan/Document_Chat_Assistant
- cd Document_Chat_Assistant
- pip install -r requirements.txt

## Running the App
streamlit run app.py

## Contributing
Feel free to open issues or submit pull requests. Let's build the GenAI revolution together!
