# CodeAlpha AI Language Translation Tool
**Project Name:** `CodeAlpha_LanguageTranslationTool`  
**Domain:** Artificial Intelligence & Natural Language Processing (NLP)  
**Internship Program:** CodeAlpha Artificial Intelligence Internship (Task 2)  
**Author:** Badri Kamtekar  
**License:** MIT  

---

## 📌 Project Overview

The **CodeAlpha AI Language Translation Tool** is a web-based natural language translation application developed as part of the CodeAlpha Artificial Intelligence Internship. It leverages real-world neural machine translation engines (Deep Translator with Google Translate integration & Gemini AI) along with Google Text-to-Speech (gTTS) to provide fast, reliable, and context-aware translation across 20+ major global and Indian languages (including Telugu, Hindi, Tamil, Kannada, Spanish, French, German, Japanese, and more).

This tool is designed with a modern, responsive layout that functions seamlessly across desktop monitors, tablets, and mobile devices.

---

## ✨ Features

1. **Modern, Responsive User Interface:** Built with clean typography, generous whitespace, intuitive controls, and responsive grid layouts.
2. **Automatic Language Detection:** Source language selector includes an "Auto Detect" option that identifies the input language automatically.
3. **Comprehensive Target Language Support:** Supports Indian languages (Telugu, Hindi, Tamil, Bengali, Marathi, Kannada, Malayalam, Gujarati, Punjabi) and international languages (Spanish, French, German, Japanese, Arabic, Russian, Portuguese, Italian, Korean, Chinese).
4. **Large Ergonomic Input Area:** Multi-line text box supporting up to 5,000 characters with auto-expanding line height.
5. **Real-Time Character Counter:** Live tracker displaying character usage with threshold warnings.
6. **One-Click Language Swap (⇄):** Easily swap the source and target languages (and text) when a specific source language is active.
7. **Real Translation API Integration:** Direct integration with Google Translate via `deep-translator` and Google Gemini AI. No mock or hardcoded translations.
8. **Text-to-Speech (TTS) Pronunciation:** Built-in speech synthesis allowing users to listen to the accurate spoken pronunciation of the translated text.
9. **One-Click Copy to Clipboard:** Streamlined copy button to immediately copy translated outputs without manual selection.
10. **Clear All Functionality:** Instant reset button to wipe current input, translation, and audio player states.
11. **Session Translation History:** Sidebar history log preserving recent translations for quick recall during study and review.
12. **Robust Input Validation & Error Handling:** Validates empty or whitespace-only inputs, prevents oversized submissions, and catches network or API timeouts with user-friendly notices.
13. **Preset Quick-Test Buttons:** One-click sample test buttons for instant evaluator demonstration (English ↔ Telugu, English ↔ Hindi).

---

## 🛠️ Technology Stack

- **Programming Language:** Python 3.9+ / 3.10+
- **Frontend Framework:** Streamlit (Python) / React 19 + Tailwind CSS (Web Applet)
- **Translation Engine:** `deep-translator` (Google Translate API) & Google Gemini AI API (`@google/genai`)
- **Speech Synthesis:** `gTTS` (Google Text-to-Speech) / Web Speech Synthesis API
- **Version Control:** Git & GitHub

---

## 📂 Project Directory Structure

```text
CodeAlpha_LanguageTranslationTool/
│
├── app.py                   # Main Streamlit web application entry point
├── test_translation.py      # Automated unit & integration test suite
├── requirements.txt         # Python project dependencies
├── .env.example             # Template for optional environment variables
├── .gitignore               # Git version control exclusions
├── README.md                # Comprehensive documentation and setup guide
│
├── server.ts                # Full-stack Express server for live web deployment
├── src/                     # React web frontend interface
│   ├── App.tsx              # Main UI component with dual-mode view
│   ├── main.tsx             # React client entry point
│   └── index.css            # Tailwind styling setup
└── package.json             # Web application configuration
```

---

## 🚀 Prerequisites & Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/YourUsername/CodeAlpha_LanguageTranslationTool.git
cd CodeAlpha_LanguageTranslationTool
```

### Step 2: Create and Activate a Python Virtual Environment
```bash
# On Linux / macOS:
python3 -m venv venv
source venv/bin/activate

# On Windows (Command Prompt):
python -m venv venv
venv\Scripts\activate

# On Windows (PowerShell):
python -m venv venv
venv\Scripts\Activate.ps1
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

---

## 💻 Running the Application

Launch the Streamlit interactive web interface with:

```bash
streamlit run app.py
```

After running the command, Streamlit will display the local and network URLs:
```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.X:8501
```

Open `http://localhost:8501` in your web browser.

---

## 🧪 Testing & Verification

The project includes an automated test script (`test_translation.py`) that rigorously validates the core translation workflows required by the internship evaluation rubric:

1. **English to Telugu Translation:**
   - Input: `"Welcome to the CodeAlpha Artificial Intelligence Internship."`
   - Verification: Checks for valid Telugu Unicode range (`\u0c00` to `\u0c7f`).
2. **Telugu to English Translation:**
   - Input: `"నమస్కారం, మీరు ఎలా ఉన్నారు?"`
   - Verification: Confirms greeting conversion to English (`"Hello, how are you?"`).
3. **English to Hindi Translation:**
   - Input: `"Artificial intelligence is transforming the world."`
   - Verification: Checks for valid Devanagari Unicode script (`\u0900` to `\u097f`).
4. **Automatic Language Detection:**
   - Input: `"Muchas gracias por tu ayuda con este proyecto."` (Spanish)
   - Verification: Correctly recognizes Spanish and outputs English `"Thank you very much..."`.
5. **Empty Input Validation:**
   - Validates that empty strings, whitespace, or newlines trigger input warnings without crashing.
6. **Error Recovery:**
   - Simulates invalid language requests and network issues to ensure clean user notifications.

### Run the Automated Tests:
```bash
python test_translation.py
```

Or using `pytest`:
```bash
pytest test_translation.py -v
```

---

## 📸 Screenshots & UI Walkthrough

When preparing your submission for CodeAlpha:

1. **Main Screen & Language Dropdown:**
   - Capture a screenshot showing the source language dropdown (with Auto Detect selected) and the target language set to **Telugu**.
2. **Active Translation & Character Counter:**
   - Enter a sentence like `"Welcome to the AI Internship"`.
   - Click **Translate Now**.
   - Show the translated Telugu text `"AI ఇంటర్న్‌షిప్‌కు స్వాగతం"` in the result box and the character counter.
3. **Audio Playback (TTS) & Copy Button:**
   - Demonstrate the audio player waveform playing the Telugu or Hindi pronunciation.
   - Click the Copy icon to showcase clipboard integration.
4. **Mobile Responsiveness:**
   - Open Developer Tools (`F12`), toggle device simulation (iPhone 14 / Pixel 7), and capture the stacked responsive layout.

---

## ⚠️ Limitations & Future Scope

### Limitations
- Requires an active internet connection to query the Google Translate servers.
- The standard Google Translate endpoint is rate-limited for very large batch requests.

### Future Scope
- **Offline Translation:** Support quantized on-device small models (e.g., MarianMT or Opus-MT via HuggingFace Transformers).
- **Document Translation:** Add PDF, DOCX, and TXT file upload and batch translation.
- **Microphone Voice Input:** Integrate live speech-to-text (STT) for two-way spoken conversation translation.

---

## 📄 License & Acknowledgments

This project is submitted under the MIT License for the **CodeAlpha Artificial Intelligence Internship Program**.  
Special thanks to the CodeAlpha mentorship team for the project guidelines and problem statement.
