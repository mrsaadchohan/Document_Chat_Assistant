import os
import streamlit as st
import tempfile
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


st.title("Chat with PDF")

uploaded=st.file_uploader("Upload a pdf", type="pdf")
query=st.text_input("Ask question about document")




@st.cache_resource
def load_file(path):
    loader=PyPDFLoader(path)
    docs=loader.load()
    return docs


def split_chunks(documents,chunk_size=800,chunk_overlap=50):
    splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

@st.cache_resource
def get_embeddings():
    return OpenAIEmbeddings(api_key=os.environ["OPENAI_API_KEY"])


def vector_db(chunks):
    embeddings=get_embeddings()
    return FAISS.from_documents(chunks,embeddings)

from langchain.chat_models import ChatOpenAI

def get_answer(query, vectordb):
    llm = ChatOpenAI(model="gpt-4", openai_api_key=os.environ["OPENAI_API_KEY"])
    chain = load_qa_chain(llm, chain_type="stuff")
    matched_docs = vectordb.similarity_search(query, k=3)
    answer = chain.run(input_documents=matched_docs, question=query)
    return answer, matched_docs




if uploaded:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded.read())
        tmp_path=tmp_file.name

    docs=load_file(tmp_path)
    chunks=split_chunks(docs)
    vectorss=vector_db(chunks)


    if query:
        answer, matched_docs = get_answer(query, vectorss)

        st.subheader("Answer:")
        st.write(answer)

        with st.expander("Retrieved Chunks"):
            for doc in matched_docs:
                st.markdown(doc.page_content[:300   ] + "...")



