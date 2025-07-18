import streamlit as st
from analyzer import analyze_logs

st.set_page_config(page_title="Log Analyzer", layout="centered")
st.title("🪵 Log Analyzer (GPT-4 Powered)")

st.markdown("Paste logs below or upload a `.txt` file to get an AI-powered explanation.")

uploaded_file = st.file_uploader("Upload log file", type=["txt"])
log_input = st.text_area("Or paste your logs here:", height=300)

logs = ""

if uploaded_file is not None:
    logs = uploaded_file.read().decode("utf-8")
elif log_input.strip():
    logs = log_input.strip()

if st.button("Analyze Logs"):
    if logs:
        with st.spinner("Analyzing logs with GPT-4..."):
            analysis = analyze_logs(logs)
        st.subheader("🧠 Analysis")
        st.write(analysis)
    else:
        st.warning("Please upload or paste some logs.")
