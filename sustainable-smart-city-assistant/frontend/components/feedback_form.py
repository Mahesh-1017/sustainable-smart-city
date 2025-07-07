import streamlit as st
import requests

def feedback_ui(api_url="http://localhost:8000/feedback/"):
    st.header("📝 Citizen Feedback Form")
    name = st.text_input("Your Name")    
    category = st.selectbox("Category", ["Water", "Electricity", "Roads", "Environment", "Other"])
    message = st.text_area("Describe the issue or suggestion")    
    if st.button("Submit") and name and message:
        with st.spinner("Submitting feedback..."):
            res = requests.post(api_url, json={"name": name, "category": category, "message": message})
            if res.status_code == 200:
                st.success("Thank you! Feedback submitted.")
            else:
                st.error("Failed to submit feedback.")
