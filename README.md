# Whisper WebUI

## Overview

Whisper WebUI is a user-friendly web application designed to transcribe audio files using the OpenAI Whisper API. This application enhances accessibility and usability by allowing users to upload audio files and receive transcriptions in various formats, catering to a wide range of applications.

## Demo

- ![Check out the demo page here!](#)
- [Whisper WebUI](#)


## Features

- **Multi-format Support**: Upload audio files in various formats, including FLAC, M4A, MP3, MP4, MPEG, MPGA, OGA, OGG, WAV, and WEBM.
- **Language Specification**: Specify the input language to improve transcription accuracy.
- **Custom Prompts**: Provide an optional prompt to guide the transcription style.
- **Flexible Output Formats**: Choose from multiple output formats, including JSON, plain text, SRT, verbose JSON, and VTT.

## Getting Started

### Run Online

1. Visit the [Whisper WebUI](#) page.
2. Provide your OpenAI API Key.
3. Upload an audio file and specify the input language, optional prompt, and desired output format.
4. Click the **"Transcribe Audio"** button to initiate the transcription process.
5. View or download the transcription results.

### Run Locally

To run Whisper WebUI on your local machine, follow these steps:

1. Clone the Repository:

   git clone https://github.com/yourusername/whisper-transcription.git
   cd whisper-transcription
2. Install Required Packages:

    pip install -r requirements.txt
3. Set Up Your OpenAI API Key:
    Ensure you have your OpenAI API key ready. You may need to set it as an environment variable or modify the configuration file.
4. Run the Streamlit Application:
    streamlit run app.py

5. Transcribe Audio:
    1. Upload your audio file and specify the input language, optional prompt, and desired output format.
    2. Click the "Transcribe Audio" button to start the transcription process.
    3. View or download the transcription results.

## Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to submit a pull request or open an issue.
