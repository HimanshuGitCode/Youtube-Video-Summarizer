import streamlit as st
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a Youtube Video Summarizer. You will be taking the transcript text of a Youtube video and generating a summary of the video in points within 350 words. The transcript text will be appended here : """

def generate_gemini_content(transcript_text,prompt):
    
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text
    