# Speech Translator

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A simple desktop app that converts speech to text, translates it to a selected language, and plays back the translated text. Built with Tkinter and Azure Cognitive Services.

## Features

- Speech-to-text using Azure Speech Services
- Text translation using Azure Translator
- Text-to-speech playback
- Basic speaker verification placeholder
- Clean Tkinter UI

## Tech Stack

- Python
- Tkinter (GUI)
- Azure Cognitive Services Speech SDK
- Azure Translator Text API
- Requests

## Requirements

- Python 3.9 or newer
- Azure Speech resource (key + region)
- Azure Translator resource (key + region + endpoint)

## Setup

1. Create a virtual environment (recommended).
2. Install dependencies:
   - azure-cognitiveservices-speech
   - requests
3. Copy the example config and add your keys:
   - Duplicate config.example.py as config.py
   - Fill in SPEECH_KEY, SPEECH_REGION, TRANSLATOR_KEY, TRANSLATOR_REGION, TRANSLATOR_ENDPOINT

## Run

Start the application by running app.py with your Python interpreter.

## Screenshots

Add your screenshots to a folder like screenshots/ and update the links below.

- Main UI: screenshots/main-ui.png
- Translation result: screenshots/translation.png

## Project Structure

- app.py: Tkinter UI and app flow
- speech_to_text.py: Speech recognition using Azure
- translator.py: Text translation using Azure Translator
- text_to_speech.py: Text-to-speech playback
- speaker_recognition.py: Placeholder speaker verification
- config.example.py: Example configuration
- config.py: Your local configuration (not committed)

## Notes

- Speaker verification is currently a stub that returns a fixed message.
- If translation fails, the original text is returned.

## Troubleshooting

- Ensure your Azure keys and regions are correct.
- Confirm your Azure Speech and Translator resources are active.
- Check that your microphone is accessible to the OS.

## License

MIT. See LICENSE.
