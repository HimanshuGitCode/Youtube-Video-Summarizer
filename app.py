import streamlit as st
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi #it will try to idea of video and reterive all the datas from the video

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a Youtube Video Summarizer. You will be taking the transcript text of a Youtube video and generating a summary of the video in points within 350 words. The transcript text will be appended here : """

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
    except Exception as e:
        raise e

def generate_gemini_content(transcript_text,prompt):
    
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text
    