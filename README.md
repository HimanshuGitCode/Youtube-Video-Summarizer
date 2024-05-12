# YouTube Video Summarizer

This repository contains a Python application built with Streamlit that converts YouTube video transcripts into detailed notes using Google's Generative AI.

![1](https://github.com/HimanshuGitCode/Youtube-Video-Summarizer/blob/main/img/Screenshot%20(1051).png)
![2](https://github.com/HimanshuGitCode/Youtube-Video-Summarizer/blob/main/img/Screenshot%20(1052).png)


## Overview

The application allows users to input a YouTube video URL, which is then used to extract the transcript using the `youtube_transcript_api`. The extracted transcript is then fed into Google's Generative AI model (Gemini Pro) along with a predefined prompt to generate a detailed summary of the video content.

## Features

- **YouTube Video URL Input**: Users can input the URL of the YouTube video they want to summarize.
  
- **Thumbnail Display**: The application displays the thumbnail image of the input YouTube video.
  
- **Transcript Extraction**: Utilizes the `youtube_transcript_api` to extract the transcript from the provided YouTube video URL.

- **Generation of Detailed Notes**: Utilizes Google's Generative AI model (Gemini Pro) to generate a detailed summary of the video content based on the extracted transcript and a predefined prompt.
  
- **Streamlit Interface**: The application is built using Streamlit, allowing for a user-friendly and interactive interface.

## Installation and Usage

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/HimanshuGitCode/Youtube-Video-Summarizer.git
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

4. **Input YouTube Video URL**: Enter the YouTube video URL in the provided text input field and click on the "Get Detailed Notes" button.

5. **View Detailed Notes**: Once the detailed notes are generated, they will be displayed on the interface.

## Dependencies

- `streamlit`: Open-source Python library that makes it easy to create web apps for machine learning and data science.
- `dotenv`: Loads environment variables from a `.env` file.
- `google.generativeai`: Google's Generative AI library for content generation.
- `youtube_transcript_api`: Python library for extracting transcripts from YouTube videos.

## Contributing

Contributions to the project are welcome! Feel free to open issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more information and contributions, visit the [GitHub repository](https://github.com/HimanshuGitCode/Youtube-Video-Summarizer).
