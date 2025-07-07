import streamlit as st
import requests

def kpi_ui(api_url="http://localhost:8000/kpi/upload"):
    st.header("📊 KPI Forecast & Anomaly Detection")
    file = st.file_uploader("Upload KPI CSV", type="csv")
    if st.button("Analyze") and file:
        with st.spinner("Analyzing KPI data..."):
            res = requests.post(api_url, files={"file": (file.name, file.getvalue(), "text/csv")})
            if res.status_code == 200:
                data = res.json()
                st.subheader("Forecast for Next Period:")
                st.metric(label="Predicted Value", value=f"{data['forecast']:.2f}")
                st.subheader("Detected Anomalies:")
                if data["anomalies"]:
                    st.json(data["anomalies"])
                else:
                    st.write("No anomalies detected.")
            else:
                st.error("Error processing file.")
