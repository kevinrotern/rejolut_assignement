# Document-Based Retrieval-Augmented Generation (RAG) Application

This is a simple Streamlit web application that allows users to upload documents (PDF or TXT) and ask questions about the content. The app uses a **BERT-based model** for question answering, retrieving relevant information from the document to generate accurate answers.

## Features

- **Document Upload**: Users can upload a document in PDF or TXT format.
- **Ask Questions**: Users can ask questions related to the content of the uploaded document.
- **Answer Retrieval**: The application uses a BERT-based model to process the document and generate accurate answers based on the content.
- **Context Display**: The app provides the relevant context (text around the answer) from the document to help users understand the response.

## Technologies Used

- **Streamlit**: For building the interactive web interface.
- **Transformers (Hugging Face)**: For using pre-trained BERT models for question answering.
- **PyTorch**: Backend deep learning library used for running the BERT model.
- **Django**: For handling document uploads and serving the content.
- **Requests**: For sending data between the frontend and backend.

## Installation and Setup

Follow these steps to set up and run the application on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/kevinrotern/rejolut_assignement.git


python -m venv rejoult
.\rejoult\Scripts\activate

cd backend
pip install -r requirements.txt
python manage.py runserver

cd frontend
streamlit run app.py

