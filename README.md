# Real-time-text-translator

# Real-Time Multi-Language Speech Translator

## 📌 Overview

This project is a **Real-Time Multi-Language Speech Translator** built using **Streamlit**. It allows users to:

- **Translate speech into multiple languages** using **Google Translator API**.
- **Convert translated text to speech (TTS)** using **gTTS**.
- **Manually input text for translation** if voice input is not preferred.

## 🚀 Features

- 🎤 **Speech-to-Text**: Recognizes speech using Google Speech Recognition.
- 🌍 **Multi-Language Support**: Supports **English, Spanish, French, German, Chinese, Hindi, Arabic, Russian, Tamil, Japanese, Korean, Telugu**, and more.
- 🔊 **Text-to-Speech (TTS)**: Converts translated text into speech and plays it in Streamlit.
- 📝 **Manual Text Translation**: Allows users to input text manually for translation.

## 🛠️ Requirements

- Python 3.x
- Streamlit
- SpeechRecognition
- Deep Translator
- gTTS
- PyAudio
- Base64 (for audio encoding)

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/real-time-speech-translator.git
   cd real-time-speech-translator
   ```
2. Install dependencies:
   ```bash
   pip install streamlit speechrecognition deep-translator gtts pyaudio
   ```

## 📌 Usage

### 1️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

### 2️⃣ Select Input Mode

- Click **'🎤 Record Voice & Translate'** to capture speech and translate it.
- Enter text manually in the text box and click **'Translate Text'**.

### 3️⃣ Choose Source and Target Languages

- Select the source and target languages from the dropdown menus.
- The recognized text will be translated and displayed.
- The translated text will be converted to speech and played automatically.

## 🔧 Configuration

Modify `translator.py` to add or remove supported languages:

```python
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
```

## 🏆 Supported Languages

Supports **multiple languages** using Google Translator API. Check the full list [here](https://cloud.google.com/translate/docs/languages).

## 🛑 Limitations

- Requires an **internet connection** for translation and speech recognition.
- Background noise may affect **speech recognition accuracy**.

