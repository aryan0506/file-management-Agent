import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI File Manager Agent", page_icon="📁")
st.title("📁 File Manager AI Agent")


# Input form
user_input = st.text_input("Enter a command for the agent:")

if st.button("Run Agent"):
    if user_input.strip():
        response = requests.post(
            f"{API_URL}/ask",
            json={"prompt": user_input},
        )
        if response.status_code == 200:
            result = response.json()
            st.success(result["response"])
        else:
            st.error(f"Error: {response.text}")
    else:
        st.warning("Please type a command")


st.subheader("🔧 Available Tools")
if st.button("Show Tools"):
    response = requests.get(f"{API_URL}/tools")
    if response.status_code == 200:
        tools = response.json().get("tools", [])
        st.json(tools)


st.subheader("📜 Agent Logs")
if st.button("Show Logs"):
    response = requests.get(f"{API_URL}/logs")
    if response.status_code == 200:
        logs = response.json().get("logs", [])
        st.code("\n".join(logs))
