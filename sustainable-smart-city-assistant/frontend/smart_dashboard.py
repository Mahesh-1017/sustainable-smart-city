import streamlit as st
import sys, os

# Ensure components package is importable
components_path = os.path.join(os.path.dirname(__file__), "components")
sys.path.append(components_path)

from components import chat_assistant, eco_tips, feedback_form, kpi_uploader, policy_summarizer

st.set_page_config(page_title="Sustainable Smart City Assistant", layout="wide")
st.title("🏙️ Sustainable Smart City Assistant Dashboard")

choice = st.sidebar.radio("Navigate", ["Chat", "Eco Tips", "Feedback", "KPI Analysis", "Policy Summarizer"])

if choice == "Chat":
    chat_assistant.chat_ui()
elif choice == "Eco Tips":
    eco_tips.eco_ui()
elif choice == "Feedback":
    feedback_form.feedback_ui()
elif choice == "KPI Analysis":
    kpi_uploader.kpi_ui()
elif choice == "Policy Summarizer":
    policy_summarizer.policy_ui()
