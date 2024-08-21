import streamlit as st
import google.generativeai as genai

st.title("Welcome to Akash's GPT")

# Configure the API key
genai.configure(api_key="AIzaSyBXBwY5XdcltwCCcd9TvONsw8ffptJz20U")

# Text input from the user
text = st.text_input("Enter Your Question:")

# Check if there's input before making API call

    # Initialize the model with the correct model name
model = genai.GenerativeModel('gemini-pro')  # Use a valid model name
chat = model.start_chat(history=[])
    
   
    # Send the message and get the response
if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
