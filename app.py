import re
import streamlit as st
from openai import OpenAI
from iso_639_languages import iso_639_languages

st.set_page_config(layout="wide")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[How to get an OpenAI API key?](https://platform.openai.com/account/api-keys)"

st.header('Create transcription from audio', divider='violet')
st.caption('created by Education Victory')


audio_file = st.file_uploader('Choose an audio file', type=["flac", "m4a", "mp3", "mp4", "mpeg", "mpga", "oga", "ogg", "wav", "webm"])
st.markdown('[How to handle file bigger than 25mb?](https://platform.openai.com/docs/guides/speech-to-text/longer-inputs)')

col1, col2, col3 = st.columns(3)

with col1:
    language_option = st.selectbox(
        "Input Language (Optional):",
        iso_639_languages.keys()
    )
    st.caption("The language of the input audio. Supplying the input language in ISO-639-1 format will improve accuracy and latency.")
    language_code = iso_639_languages[language_option]

with col2:
    prompt = st.text_input("Prompt (Optional)", "")
    st.caption("An optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language.")


with col3:
    format_option = st.selectbox(
        "Output Format (Optional):",
        ['json', 'text', 'srt', 'verbose_json', 'vtt']
    )
    st.caption("The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt.")

if audio_file:
    if not openai_api_key:
        st.info("Please add your OpenAI API key in the sidebar to continue.")
        st.stop()
    # Button to start transcription
    if st.button('Transcribe Audio'):
        # Set the OpenAI API key
        client = OpenAI(api_key=openai_api_key)

        # Call the OpenAI API for transcription
        with st.spinner('Processing...'):
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language=language_code,
                prompt=prompt,
                response_format=format_option,
            )
            if format_option == 'json':
                with st.container(border=True):
                    st.json(transcription.to_json())
            elif format_option == 'text':
                container = st.container(border=True)
                container.write(transcription)
            elif format_option == 'verbose_json':
                with st.container(border=True):
                    st.json(transcription.to_json())
            elif format_option == 'vtt':
                container = st.container(border=True)
                container.write(transcription)
            elif format_option == 'srt':
                # Provide a download button for the SRT file
                st.download_button(label='Click To Download SRT File', data=transcription, file_name=audio_file.name + '.srt')
