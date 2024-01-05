import streamlit as st
from openai import OpenAI

st.title('Simple audio transcription')

api_key = st.text_input("Enter your OpenAI API key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    uploaded_file = st.file_uploader("Upload your audio file", type=['mp3', 'wav', 'ogg'])

    if uploaded_file is not None:
        try:
            # Call to create a transcription using the OpenAI API
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=uploaded_file,
                response_format="text"
            )

            # Display the transcription
            st.text_area("Transcription", transcript, height=200)
        except Exception as e:
            st.error(f"An error occurred: {e}")
