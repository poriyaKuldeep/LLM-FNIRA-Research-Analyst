import os
import time
import pickle
import streamlit as st
from langchain import OpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings




from dotenv import load_dotenv
load_dotenv()

main_placeholder=st.empty()
file_path="faiss_store_openai.pkl"
llm=OpenAI(model="davinci-002",temperature=0.9,max_tokens=500)

st.title("News research Tool ")
st.sidebar.title("News Article Links")

urlss=[]
for i in range(3):
    url=st.sidebar.text_input(f"URL {i+1}")
    if url !='':
        urlss.append(url)

    

process_url_clicked=st.sidebar.button("Process URLs")    

if process_url_clicked:
    # load data
    # loader=UnstructuredURLLoader(urls=urls)
    loader=WebBaseLoader(urlss)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data=loader.load()
    # st.write(len(data))
    # main_placeholder.text(len(data))

    # split data
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs=text_splitter.split_documents(data)

     # create embeddings and save it to FAISS index
    
    # embeddings=OpenAIEmbeddings()
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore_openai=FAISS.from_documents(docs,embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)


    # Save the FAISS index to a pickle file
    with open(file_path,"wb") as f:
        pickle.dump(vectorstore_openai,f)

query= main_placeholder.text_input("question :")  

if query:
    if os.path.exists(file_path):
        with open(file_path,"rb") as f:
            vectorstore=pickle.load(f)
            chain=RetrievalQAWithSourcesChain.from_llm(llm=llm ,retriever=vectorstore.as_retriever())
            result=chain({'question': query} , return_only_outputs=True)
             # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.subheader(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    st.write(source)



 

