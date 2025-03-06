import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64
import os

# Function to play audio in Streamlit
def play_audio(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()
    audio_html = f"""
        <audio autoplay controls>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

# Streamlit UI
st.title("🎙 Real-Time Multi-Language Speech Translator 🔊")

# Select source and target languages
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-CN",
    "Hindi": "hi",
    "Arabic": "ar",
    "Russian": "ru",
    "Tamil": "ta",
    "Japanese": "ja",
    "Korean": "ko",
    "Telugu": "te"
}

source_lang = st.selectbox("Select Source Language:", list(languages.keys()))
target_lang = st.selectbox("Select Target Language:", list(languages.keys()))

# Speech-to-Text (Voice Input)
recognizer = sr.Recognizer()
if st.button("🎤 Record Voice & Translate"):
    with sr.Microphone() as source:
        st.write("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language=languages[source_lang])
            st.success(f"Recognized Text: {text}")

            # Translate the recognized text
            translated_text = GoogleTranslator(source=languages[source_lang], target=languages[target_lang]).translate(text)
            st.success(f"Translated Text ({target_lang}): {translated_text}")

            # Convert translated text to speech
            tts = gTTS(translated_text, lang=languages[target_lang])
            tts.save("translated_audio.mp3")

            # Play audio
            play_audio("translated_audio.mp3")

        except sr.UnknownValueError:
            st.error("Sorry, could not recognize the speech. Try again!")
        except sr.RequestError:
            st.error("Could not request results. Please check your internet connection.")

# Manual Text Input Translation
text_input = st.text_area("Or enter text to translate:")
if st.button("Translate Text"):
    if text_input:
        translated_text = GoogleTranslator(source=languages[source_lang], target=languages[target_lang]).translate(text_input)
        st.success(f"Translated Text ({target_lang}): {translated_text}")

        # Convert translated text to speech
        tts = gTTS(translated_text, lang=languages[target_lang])
        tts.save("translated_audio.mp3")

        # Play audio
        play_audio("translated_audio.mp3")
    else:
        st.warning("Please enter text to translate.")