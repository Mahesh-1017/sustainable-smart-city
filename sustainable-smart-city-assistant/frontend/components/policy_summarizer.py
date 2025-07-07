import streamlit as st
import requests

def policy_ui(upload_url="http://localhost:8000/policy/upload", search_url="http://localhost:8000/policy/search"):
    st.header("📄 Policy Summarization & Search")
    st.subheader("Upload a Policy Document")    
    file = st.file_uploader("Upload .txt, .csv, or .md", type=["txt", "csv", "md"])
    if st.button("Upload & Summarize") and file:
        with st.spinner("Uploading & summarizing..."):
            res = requests.post(upload_url, files={"file": (file.name, file.getvalue(), "text/plain")})
            st.json(res.json())
            
    st.subheader("Ask a Question about Policies")    
    question = st.text_input("Enter your question")    
    if st.button("Search Policies") and question:
        with st.spinner("Searching policies..."):
            res = requests.post(search_url, json={"question": question})
            st.markdown(res.json().get("answer", "No answer"))
