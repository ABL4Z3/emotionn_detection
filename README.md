# Voice Emotion Detector

This is a web application that allows users to upload or record voice audio to detect emotions and receive empathetic responses. The app transcribes the audio to text, analyzes the sentiment, and generates an empathetic message using a language model.

## Features

- Upload audio files (WAV, MP3, M4A) for emotion detection.
- Record live audio in the browser and convert it to WAV format for processing.
- Speech-to-text transcription using Google's speech recognition API.
- Emotion detection based on the transcribed text.
- Empathetic response generation using LangChain Groq LLM.
- Audio playback of recorded or uploaded files.
- User-friendly interface with transcription and emotion display.

## Technologies Used

- Backend: Python Flask, SpeechRecognition, TextBlob, Deep Translator, LangChain Groq
- Frontend: HTML, CSS, JavaScript (MediaRecorder API, Web Audio API)
- Audio processing: Web Audio API for frontend WAV conversion
- No external dependencies like FFmpeg required for audio conversion

## Setup and Installation

1. Clone the repository.

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # Windows
   source myenv/bin/activate  # macOS/Linux
   ```

3. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the `GROQ_API_KEY` environment variable with your LangChain Groq API key or use the default in the code.

5. Run the Flask app:

   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://localhost:5000` to use the app.

## Usage

- Upload an audio file or click the "Start Recording" button to record live audio.
- After recording, the audio is converted to WAV format and sent to the backend.
- The backend transcribes the audio, detects emotion, and generates an empathetic response.
- The transcription, detected emotion, and empathetic response are displayed on the page.

## Notes

- The app currently supports WAV audio files for upload and recording.
- The frontend converts recorded audio to WAV format to ensure backend compatibility.
- No FFmpeg installation is required.
- For best results, use clear speech and quiet environments for recording.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Uses Google's Speech Recognition API via SpeechRecognition Python library.
- Uses LangChain Groq for language model-based empathetic response generation.
- Inspired by modern web audio processing techniques.
