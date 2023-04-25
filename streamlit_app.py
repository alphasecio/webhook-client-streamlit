import requests
import streamlit as st

st.title("Webhook Client")
url = st.text_input("Webhook URL", "https://webhook-server.com/webhook-1")
payload = st.text_input("JSON Payload", "{}")

if st.button("Submit"):
    if not url.strip() == "":
        response = requests.post(url, data = payload)
        st.success(f"Response: {response.text}")
    else:
        st.error(f"Response: Please provide the Webhook URL.")
