import re
from openai import OpenAI
import streamlit as st

st.set_page_config(layout="wide")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.header('Audio To Srt', divider='violet')
st.caption('created by Education Victory')


audio_file = st.file_uploader('Please upload the audio.', type=["flac", "m4a", "mp3", "mp4", "mpeg", "mpga", "oga", "ogg", "wav", "webm"])

if audio_file and openai_api_key:
    # Display the uploaded file name
    st.write(f"Uploaded file: {audio_file.name}")

    # Button to start transcription
    if st.button('Transcribe Audio'):
        # Set the OpenAI API key
        client = OpenAI(api_key=openai_api_key)

        # Call the OpenAI API for transcription
        with st.spinner('Processing...'):
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="srt",
            )
            # Provide a download button for the SRT file
            st.download_button(label='Click To Download SRT File', data=transcription, file_name=audio_file.name + '.srt')
