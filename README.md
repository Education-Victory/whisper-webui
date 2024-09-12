# Whisper WebUI

## Overview

Whisper WebUI is a user-friendly web application designed to transcribe and translate audio files using the OpenAI Whisper API. This application enhances accessibility and usability by allowing users to upload audio files and receive transcriptions or translations in various formats, catering to a wide range of applications.

## Demo

- ![Check out the demo page here!](https://github.com/Education-Victory/whisper-webui/blob/main/demo-page.png?raw=true)
- [Whisper WebUI](https://whisper-webui.streamlit.app/)


## Features

- **Multi-format Support**: Upload audio files in various formats, including FLAC, M4A, MP3, MP4, MPEG, MPGA, OGA, OGG, WAV, and WEBM.
- **Language Specification**: Specify the input language to improve transcription accuracy.
- **Custom Prompts**: Provide an optional prompt to guide the transcription style.
- **Flexible Output Formats**: Choose from multiple output formats, including JSON, plain text, SRT, verbose JSON, and VTT.

## Getting Started

### Run Online

1. Visit the [Whisper WebUI](https://whisper-webui.streamlit.app/) page.
2. Provide your OpenAI API Key.
3. Choose the **"Create transcription"** or **"Create translation"** button based on your usecase.
3. Upload an audio file and specify the  optional prompt, and desired output format.
5. View or download the results.

### Run Locally

To run Whisper WebUI on your local machine, follow these steps:

1. Clone the Repository:

   `git clone git@github.com:Education-Victory/whisper-webui.git`
   `cd whisper-webui`
2. Install Required Packages:

    `pip install -r requirements.txt`
3. Get OpenAI API Key:
    Ensure you have your OpenAI API key ready.
4. Run the Streamlit Application:

    `streamlit run app.py`

## Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to submit a pull request or open an issue.
