import streamlit as st
import requests
from transformers import pipeline

st.title("Document-Based RAG Application")

uploaded_file = st.file_uploader("Upload your document (PDF or TXT)", type=["txt", "pdf"])
if uploaded_file:
    files = {"document": uploaded_file}
    response = requests.post("http://127.0.0.1:8000/upload", files=files)
    
    if response.status_code == 200:
        result = response.json()
        if result.get('status') == 'success':
            content = result.get('content')
            st.write("Document Content:")
            st.text_area("", content, height=200)

            question = st.text_input("Ask a question about the document:", label_visibility="collapsed")
            if question:
                qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
                answer = qa_pipeline(question=question, context=content)
                answer_text = answer['answer']
                start_idx = answer['start']
                end_idx = answer['end']
                context = content[max(0, start_idx - 100):min(len(content), end_idx + 100)]  
                st.write("Answer:", answer_text)
                st.write("Context:", context)
        else:
            st.error(result.get('message'))
