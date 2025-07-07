import streamlit as st
import requests

def chat_ui(api_url="http://localhost:8000/chat/"):
    st.header("💬 Smart City Chat Assistant")
    user_input = st.text_input("Ask your question about sustainability...")
    if st.button("Ask") and user_input:
        with st.spinner("Getting answer..."):
            res = requests.post(api_url, json={"user_input": user_input})
            st.success(res.json().get("response", "No answer"))
