import streamlit as st
import os

from utils.index_documents import index_document
from utils.chat import ask_question

st.set_page_config(
    page_title="Multi-Document Knowledge Base",
    page_icon="📚",
    layout="wide"
)

st.title("Multi-Document Knowledge Base")

# Upload PDFs
uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["pdf"],
    accept_multiple_files=True
)

# Process Documents
if uploaded_files:

    st.success(f"{len(uploaded_files)} file(s) uploaded")

    if st.button("Process Documents"):

        os.makedirs("uploads", exist_ok=True)

        for file in uploaded_files:

            pdf_path = os.path.join(
                "uploads",
                file.name
            )

            # Save uploaded file
            with open(pdf_path, "wb") as f:
                f.write(file.getbuffer())

            # Index document
            index_document(pdf_path)

        st.success("Documents indexed successfully!")

st.divider()

# Ask Questions
question = st.text_input(
    "Ask a question about your documents"
)

if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching documents and generating answer..."):

            answer, docs = ask_question(question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for i, doc in enumerate(docs, start=1):

            with st.expander(f"Source {i}"):

                st.write(doc.page_content[:500])