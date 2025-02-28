import streamlit as st
import requests


st.title("Math Question Generator")

# Define the API endpoint URL
api_url = "http://127.0.0.1:8000/generate_question"

# Optionally, allow the user to select a category (here we assume only one category for now)
category = st.selectbox("Select Category", ["Number Sense and Place Value"])

if st.button("Generate Question"):
    # Call the API endpoint
    params = {"category": category}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = response.json()
        st.write("Generated Question:")
        st.write(data["text"])
    except requests.exceptions.RequestException as e:
        st.error(f"Error calling API: {e}")
