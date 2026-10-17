"""
CodeAlpha Artificial Intelligence Internship
Task 2: AI Language Translation Tool
Repository: CodeAlpha_LanguageTranslationTool

A production-grade multilingual translation web application built with Streamlit,
Deep Translator (Google Translate engine), and Google Text-to-Speech (gTTS).
"""

import io
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

# Configure Streamlit page layout and appearance
st.set_page_config(
    page_title="AI Language Translation Tool | CodeAlpha",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling for polished, modern interface
st.markdown(
    """
    <style>
    /* Main container styling */
    .main {
        background-color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header styling */
    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.25rem;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.05rem;
        color: #64748b;
        margin-bottom: 1.5rem;
    }
    
    /* Translation card containers */
    .stTextArea textarea {
        font-size: 1.05rem !important;
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        line-height: 1.6 !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.15) !important;
    }
    
    /* Button overrides */
    div.stButton > button {
        border-radius: 6px;
        font-weight: 600;
        transition: all 0.15s ease-in-out;
    }
    
    /* Custom info callouts */
    .badge-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px 18px;
        margin-top: 10px;
    }
    
    .char-count {
        font-size: 0.85rem;
        color: #64748b;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Supported language mappings: display name -> ISO code
SUPPORTED_LANGUAGES = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN",
    "Arabic": "ar",
    "Bengali": "bn",
    "Marathi": "mr",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Russian": "ru",
    "Portuguese": "pt",
    "Italian": "it",
    "Korean": "ko",
}

SOURCE_OPTIONS = ["Auto Detect"] + list(SUPPORTED_LANGUAGES.keys())
TARGET_OPTIONS = list(SUPPORTED_LANGUAGES.keys())

# Initialize session state variables
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "translated_result" not in st.session_state:
    st.session_state.translated_result = ""
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "Auto Detect"
if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Telugu"
if "translation_history" not in st.session_state:
    st.session_state.translation_history = []


def swap_languages():
    """Swaps source and target languages if source is not Auto Detect."""
    curr_src = st.session_state.source_lang
    curr_tgt = st.session_state.target_lang

    if curr_src != "Auto Detect":
        st.session_state.source_lang = curr_tgt
        st.session_state.target_lang = curr_src
        # Also swap the texts if translated result exists
        if st.session_state.translated_result:
            old_input = st.session_state.input_text
            st.session_state.input_text = st.session_state.translated_result
            st.session_state.translated_result = old_input
    else:
        st.warning("Cannot swap when source language is set to 'Auto Detect'. Select a specific source language.")


def clear_all():
    """Clears text area and translation output."""
    st.session_state.input_text = ""
    st.session_state.translated_result = ""


# Sidebar: Project Info, Demo Presets & History
with st.sidebar:
    st.markdown("### CodeAlpha AI Internship")
    st.caption("Task 2: AI Language Translation Tool")
    st.divider()

    st.markdown("#### Sample Test Presets")
    st.caption("Click to load verified test phrases:")

    if st.button("English to Telugu", use_container_width=True):
        st.session_state.source_lang = "English"
        st.session_state.target_lang = "Telugu"
        st.session_state.input_text = "Welcome to the CodeAlpha Artificial Intelligence Internship program."
        st.session_state.translated_result = ""

    if st.button("Telugu to English", use_container_width=True):
        st.session_state.source_lang = "Telugu"
        st.session_state.target_lang = "English"
        st.session_state.input_text = "నమస్కారం! మీరు కృత్రిమ మేధస్సు గురించి ఏమి నేర్చుకుంటున్నారు?"
        st.session_state.translated_result = ""

    if st.button("English to Hindi", use_container_width=True):
        st.session_state.source_lang = "English"
        st.session_state.target_lang = "Hindi"
        st.session_state.input_text = "Natural language processing connects people across different cultures and languages."
        st.session_state.translated_result = ""

    st.divider()

    st.markdown("#### Translation History")
    if st.session_state.translation_history:
        for idx, item in enumerate(reversed(st.session_state.translation_history[-5:])):
            with st.expander(f"{item['src']} -> {item['tgt']}: {item['input'][:25]}..."):
                st.write(f"**Input:** {item['input']}")
                st.write(f"**Translation:** {item['output']}")
        if st.button("Clear History", use_container_width=True):
            st.session_state.translation_history = []
            st.rerun()
    else:
        st.caption("No translations recorded in this session.")

    st.divider()
    st.caption("Engine: Deep-Translator Google API & gTTS")
    st.caption("Repository: CodeAlpha_LanguageTranslationTool")

# Main Interface Header
st.markdown('<div class="hero-title">AI Language Translation Tool</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-subtitle">Translate text seamlessly with real-time neural translation, automatic language detection, and audio playback.</div>',
    unsafe_allow_html=True,
)

# Language selection controls bar
col_lang1, col_swap, col_lang2 = st.columns([5, 1, 5], vertical_alignment="bottom")

with col_lang1:
    src_idx = SOURCE_OPTIONS.index(st.session_state.source_lang) if st.session_state.source_lang in SOURCE_OPTIONS else 0
    selected_source = st.selectbox(
        "Source Language",
        options=SOURCE_OPTIONS,
        index=src_idx,
        key="source_lang_select",
    )
    st.session_state.source_lang = selected_source

with col_swap:
    st.button("⇄ Swap", on_click=swap_languages, help="Swap source and target languages", use_container_width=True)

with col_lang2:
    tgt_idx = TARGET_OPTIONS.index(st.session_state.target_lang) if st.session_state.target_lang in TARGET_OPTIONS else 0
    selected_target = st.selectbox(
        "Target Language",
        options=TARGET_OPTIONS,
        index=tgt_idx,
        key="target_lang_select",
    )
    st.session_state.target_lang = selected_target

# Text Area Columns
col_input, col_output = st.columns(2)

with col_input:
    st.markdown("**Enter Text to Translate:**")
    user_input = st.text_area(
        label="Input Text Area",
        value=st.session_state.input_text,
        height=220,
        placeholder="Type or paste text here (up to 5,000 characters)...",
        label_visibility="collapsed",
        key="main_input_area",
    )
    st.session_state.input_text = user_input

    # Character count
    char_len = len(user_input)
    st.markdown(f'<div class="char-count">{char_len} / 5000 characters</div>', unsafe_allow_html=True)

    # Action buttons row
    btn_col1, btn_col2 = st.columns([2, 1])
    with btn_col1:
        translate_clicked = st.button("Translate Now", type="primary", use_container_width=True)
    with btn_col2:
        st.button("Clear", on_click=clear_all, use_container_width=True)

# Translation Processing
if translate_clicked:
    trimmed_text = user_input.strip()

    # Empty validation
    if not trimmed_text:
        st.error("Please enter some text before translating. The input text cannot be empty.")
    elif len(trimmed_text) > 5000:
        st.error("Input text exceeds the 5,000 character limit. Please shorten your text.")
    else:
        # Determine source and target codes
        source_code = "auto" if st.session_state.source_lang == "Auto Detect" else SUPPORTED_LANGUAGES[st.session_state.source_lang]
        target_code = SUPPORTED_LANGUAGES[st.session_state.target_lang]

        with st.spinner("Connecting to translation engine and translating..."):
            try:
                # Real translation via deep-translator GoogleTranslator
                translator = GoogleTranslator(source=source_code, target=target_code)
                translation = translator.translate(trimmed_text)

                if translation:
                    st.session_state.translated_result = translation
                    # Append to session history
                    st.session_state.translation_history.append({
                        "src": st.session_state.source_lang,
                        "tgt": st.session_state.target_lang,
                        "input": trimmed_text,
                        "output": translation,
                    })
                else:
                    st.error("Translation service returned an empty response. Please try rephrasing.")
            except Exception as e:
                st.error(f"Translation Error: Unable to complete translation. Details: {str(e)}")
                st.info("Tip: Ensure your internet connection is active. Deep-Translator requires outbound connectivity to Google Translate servers.")

with col_output:
    st.markdown("**Translated Text:**")
    st.text_area(
        label="Translation Result Area",
        value=st.session_state.translated_result,
        height=220,
        placeholder="Translation will appear here...",
        label_visibility="collapsed",
        disabled=True,
    )

    # Post-translation tools: Copy and Text-to-Speech
    if st.session_state.translated_result:
        res_col1, res_col2 = st.columns([1, 1])
        
        with res_col1:
            # Native Streamlit code block provides 1-click clipboard copy
            st.code(st.session_state.translated_result, language="text")
            st.caption("Click the copy icon on the top-right of the block above to copy.")

        with res_col2:
            st.markdown("**Audio Pronunciation (TTS):**")
            target_code = SUPPORTED_LANGUAGES.get(st.session_state.target_lang, "en")
            
            # gTTS audio generation
            try:
                # Some gTTS codes might require special mapping (e.g. zh-CN -> zh-CN)
                tts_lang = target_code.split("-")[0]
                tts = gTTS(text=st.session_state.translated_result, lang=tts_lang, slow=False)
                audio_bytes = io.BytesIO()
                tts.write_to_fp(audio_bytes)
                audio_bytes.seek(0)
                st.audio(audio_bytes, format="audio/mp3")
            except Exception as tts_err:
                st.caption(f"Audio playback not available for this target language ({str(tts_err)})")

# Technical specifications footer
st.markdown("---")
st.markdown(
    """
    <div style="font-size: 0.85rem; color: #64748b; text-align: center;">
        CodeAlpha Artificial Intelligence Internship • Project: AI Language Translation Tool • Developed for CodeAlpha_LanguageTranslationTool
    </div>
    """,
    unsafe_allow_html=True,
)
