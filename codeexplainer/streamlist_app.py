import streamlit as st
from explain import explain_code

st.set_page_config(page_title="Code Explainer", layout="centered")

st.title("🧠 Code Explainer")
st.markdown("Explain code using OpenAI's GPT-4")

code_input = st.text_area("Paste your code below:", height=250, placeholder="e.g. for i in range(5): print(i)")

if st.button("Explain"):
    if code_input.strip():
        with st.spinner("Thinking..."):
            explanation = explain_code(code_input)
        st.subheader("💡 Explanation:")
        st.write(explanation)
    else:
        st.warning("Please paste some code.")
