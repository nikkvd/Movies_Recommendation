import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai


#Import the Local Environment
from dotenv import load_dotenv
load_dotenv() #Load the Environment
import os

# genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

#Design the Page
st.title("Movie Recommendation System🎥")
user_input = st.text_input("Enter the Movie, Genre or Keywords")
submit = st.button('Submit')


# Google Gemini Model and Source the Recommendations
movie_templates = '''Based on {user_input} provide Movie Recommendations.'''
template = PromptTemplate(input_varibles = ['user_input'],
                          template=movie_templates)

# Initiate the Model
llm = ChatGoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"),model = "gemini-1.5-pro")


if submit:
    prompt = template.format(user_input=user_input)
    recomendations = llm.predict(text=prompt)
    st.write(f"Recommendations for you: {recomendations}")
else:
    st.write("")