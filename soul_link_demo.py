import speech_recognition as sr
from textblob import TextBlob
from deep_translator import GoogleTranslator
from langchain_groq import ChatGroq
import os

# Set Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize LangChain Groq
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def speech_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
            print("\n[Speech-to-Text]")
            print("Transcribed Text:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError:
            print("API request failed")
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
    print("\n[Emotion Detection]")
    print(f"Detected Emotion: {emotion}")
    return emotion

def translate_text(text, dest_language='es'):
    translated = GoogleTranslator(source='auto', target=dest_language).translate(text)
    print(f"\n[Translation]")
    print(f"Translated Text ({dest_language}): {translated}")
    return translated

def generate_empathy_prompt(user_text):
    prompt = f"A person said: '{user_text}'. Write an empathetic response:"
    response = llm.invoke(prompt)
    print("\n[Empathy Prompt]")
    print("Empathy Response:", response.content)
    return response

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
        print("No valid text to process further.")
