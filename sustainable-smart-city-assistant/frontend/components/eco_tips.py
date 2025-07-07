import streamlit as st
import requests

def eco_ui(api_url="http://localhost:8000/eco-tips/"):
    st.header("🌱 Eco‑Tips Generator")
    topic = st.text_input("Enter a sustainability topic (e.g., plastic, energy, water)")
    if st.button("Generate Tips") and topic:
        with st.spinner("Generating tips..."):
            res = requests.post(api_url, json={"topic": topic})
            st.markdown(res.json().get("tips", "No tips returned"))
