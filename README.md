SOUL LINK DEMO - README

1. Setup Virtual Environment
-----------------------------
python -m venv myenv
.\myenv\Scripts\activate
pip install --upgrade pip

2. Install Requirements
-----------------------
pip install --force-reinstall --no-cache-dir -r requirements.txt

3. Run Demo Script
------------------
python soul_link_demo.py

4. What It Does
---------------
- Reads audio from audio_input.wav
- Converts speech to text
- Detects emotion (positive/negative/neutral)
- Translates text to Spanish
- (Optional) Generates empathetic response if using OpenAI or Groq

5. Notes
--------
- Make sure audio_input.wav is in the same folder.
- Internet connection is required.
