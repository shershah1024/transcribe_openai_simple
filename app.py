import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client with your API key

st.title('Simple audio transcription')

api_key = st.text_input("Enter your OpenAI API key", type="password")

# Only proceed with the rest of the program if the API key is entered
if api_key:
    openai = OpenAI(api_key=api_key)

uploaded_file = st.file_uploader("Upload your audio file", type=['mp3', 'wav', 'ogg'])

client = OpenAI()

if uploaded_file is not None:
    try:
        # Call to create a transcription using the OpenAI API
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=uploaded_file,
            response_format="text"
        )

        print(transcript)


        # Display the transcription
        st.text_area("Transcription", transcript, height=200)
    except Exception as e:
        st.error(f"An error occurred: {e}")
