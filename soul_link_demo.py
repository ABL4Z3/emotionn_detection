import speech_recognition as sr
from textblob import TextBlob
from deep_translator import GoogleTranslator
from langchain_groq import ChatGroq
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set Groq API key from environment variable or fallback to provided key
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    logger.warning("GROQ_API_KEY environment variable not set. LangChain Groq may not work properly.")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Initialize LangChain Groq with API key parameter
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0, groq_api_key=GROQ_API_KEY)

def speech_to_text(audio_file, language='en-IN'):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data, language=language)
            logger.info("[Speech-to-Text] Transcribed Text: %s", text)
            return text
        except sr.UnknownValueError:
            logger.error("Could not understand audio")
            return ""
        except sr.RequestError:
            logger.error("API request failed")
            return ""

def detect_emotion(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        emotion = "Positive"
    elif sentiment < 0:
        emotion = "Negative"
    else:
        emotion = "Neutral"
    logger.info("[Emotion Detection] Detected Emotion: %s", emotion)
    return emotion

def translate_text(text, dest_language='es'):
    try:
        translated = GoogleTranslator(source='auto', target=dest_language).translate(text)
        logger.info("[Translation] Translated Text (%s): %s", dest_language, translated)
        return translated
    except Exception as e:
        logger.error("Translation failed: %s", str(e))
        return ""

def generate_empathy_prompt(user_text):
    prompt = f"A person said: '{user_text}'. Write an empathetic response:"
    try:
        response = llm.invoke(prompt)
        logger.info("[Empathy Prompt] Empathy Response: %s", response.content)
        return response
    except Exception as e:
        logger.error("Empathy prompt generation failed: %s", str(e))
        return None

if __name__ == "__main__":
    audio_file = "audio_input.wav"
    
    # Step 1: Speech-to-Text
    text = speech_to_text(audio_file)
    
    if text:
        # Step 2: Emotion Detection
        emotion = detect_emotion(text)
        
        # Step 3: Translation (English → Spanish)
        translated_text = translate_text(text, dest_language='es')
        
        # Step 4: Empathy Prompt
        empathy_response = generate_empathy_prompt(text)
    else:
        logger.info("No valid text to process further.")
