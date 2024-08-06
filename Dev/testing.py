import streamlit as st
import os
import google.generativeai as genai
from ipl_2024_data import ipl_2024_data

os.environ['GOOGLE_API_KEY'] = "AIzaSyAEnHVjbcA7-jrIhtPJULoBe7sIYBhzsYg"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

from ipl_2024_data import ipl_2024_data

def get_response(question):
    """Get the model response for a given question."""
    prompt = (
        "Please analyze the following question and respond accordingly:\n\n"
        "1. If the question is asking for IPL data beyond the year 2024, respond with: "
        "'Sorry, I don't have data beyond 2024. We are working on it. We'll update it soon :)'\n"
        "2. If the question is asking for cricket data but is not related to IPL for data greater than 2022, respond with: "
        "'The question is not related to IPL. Please ask a question related to IPL as it is greater than 2022 :)'\n"
        "3. Otherwise, provide an accurate and informative response to the IPL-related question.\n\n"
        "Here are some sample questions and their answers to guide you:\n"
        f"{ipl_2024_data}\n\n"
        f"Question: {question}"
    )
    return prompt


    response = model.generate_content(prompt)
    return response.text

st.set_page_config(page_title="Cricket Q&A", page_icon="🏏", layout="centered")

st.title("🏏 Cricket Q&A Application")
question = st.text_input("Please ask a question related to Cricket:")
if st.button("Get Answer"):
    if question:
        response_text = get_response("Check 2 conditions before response first check if the question asking data greater than 2023 give response sorry i dont have data we are working on it and if the data is not related to cricket give response that please ask the question related to cricket after checking conditions answer the questions"+question)
        st.write(response_text)
    else:
        st.error("Please enter a question.")
st.sidebar.title("About This Project")
st.sidebar.write(
"Overview: The Cricket Q&A Application is an interactive web application designed to answer users questions related to cricket. Built using Streamlit and powered by GG AI model, this application provides accurate and informative responses to cricket-related queries. The application ensures user queries are properly addressed by implementing checks for data relevance and timeframe.Features")
st.sidebar.write("Project developed by **Manideep**, **Koushik**, **Vignesh**, **Kinnera**, **Sunidhi**, and **Sathvika**. Guided by **Mr. B Kiran Kumar**")
