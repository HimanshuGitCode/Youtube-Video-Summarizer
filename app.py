import streamlit as st
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi #it will try to idea of video and reterive all the datas from the video

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube Video Summarizer tasked with providing an in-depth analysis of a video's content. Your goal is to generate a comprehensive summary that captures the main points, key arguments, and supporting details within a 750-word limit. Please thoroughly analyze the transcript text provided and offer a detailed summary, ensuring to cover all relevant aspects of the video: """

#getting the transcript of the youtube video 

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript = " "
        for i in transcript_text:
            transcript +=  " " + i['text'] 
            
        return transcript
        
    except Exception as e:
        raise e

#getting the summary  based on prompt form google Gemini Pro

def generate_gemini_content(transcript_text,prompt):
    
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("Youtube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter the Youtube Video URL : ")
    
#for displaying thumbnail images

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)
    
if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    
    if transcript_text:
        summary = generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
        
st.markdown("---")
st.write(
    "Made By Himanshu Singh [#Linkedin](https://www.linkedin.com/in/himanshu-singh01/) !"
)
st.markdown(
    "More infos and :star: at [github.com/himanshugitcode/Youtube-Video-Summarizer](https://github.com/HimanshuGitCode/Youtube-Video-Summarizer)  !"
)
