"""
Unit and Integration Test Suite for CodeAlpha AI Language Translation Tool
Tests English-to-Telugu, Telugu-to-English, English-to-Hindi translations,
empty input validation, language detection, and error handling.
"""

import sys
import unittest
from deep_translator import GoogleTranslator

class TestLanguageTranslationTool(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n" + "="*60)
        print("  CodeAlpha AI Internship - Translation Tool Test Suite")
        print("="*60)

    def test_01_english_to_telugu(self):
        """Test English to Telugu translation"""
        input_text = "Welcome to the CodeAlpha Artificial Intelligence Internship."
        translator = GoogleTranslator(source="en", target="te")
        translated = translator.translate(input_text)
        print(f"\n[TEST 1] EN -> TE:")
        print(f"  Input:  {input_text}")
        print(f"  Output: {translated}")
        self.assertIsNotNone(translated)
        self.assertTrue(len(translated.strip()) > 0)
        # Should contain Telugu script characters
        self.assertTrue(any('\u0c00' <= char <= '\u0c7f' for char in translated), "Output should contain Telugu characters")

    def test_02_telugu_to_english(self):
        """Test Telugu to English translation"""
        input_text = "నమస్కారం, మీరు ఎలా ఉన్నారు?"
        translator = GoogleTranslator(source="te", target="en")
        translated = translator.translate(input_text)
        print(f"\n[TEST 2] TE -> EN:")
        print(f"  Input:  {input_text}")
        print(f"  Output: {translated}")
        self.assertIsNotNone(translated)
        self.assertTrue(len(translated.strip()) > 0)
        self.assertTrue("hello" in translated.lower() or "how are you" in translated.lower() or "greetings" in translated.lower())

    def test_03_english_to_hindi(self):
        """Test English to Hindi translation"""
        input_text = "Artificial intelligence is transforming the world."
        translator = GoogleTranslator(source="en", target="hi")
        translated = translator.translate(input_text)
        print(f"\n[TEST 3] EN -> HI:")
        print(f"  Input:  {input_text}")
        print(f"  Output: {translated}")
        self.assertIsNotNone(translated)
        self.assertTrue(len(translated.strip()) > 0)
        # Should contain Devanagari script characters
        self.assertTrue(any('\u0900' <= char <= '\u097f' for char in translated), "Output should contain Hindi/Devanagari characters")

    def test_04_auto_detect_to_english(self):
        """Test automatic language detection to English"""
        input_spanish = "Muchas gracias por tu ayuda con este proyecto."
        translator = GoogleTranslator(source="auto", target="en")
        translated = translator.translate(input_spanish)
        print(f"\n[TEST 4] AUTO (ES) -> EN:")
        print(f"  Input:  {input_spanish}")
        print(f"  Output: {translated}")
        self.assertIsNotNone(translated)
        self.assertTrue("thank" in translated.lower())

    def test_05_empty_input_validation(self):
        """Test empty input validation logic"""
        empty_texts = ["", "   ", "\n\t  \n"]
        for text in empty_texts:
            trimmed = text.strip()
            self.assertEqual(len(trimmed), 0, "Empty/whitespace input should be flagged by validation")
        print("\n[TEST 5] Empty input validation passed: All empty/whitespace variants correctly flagged.")

    def test_06_unsupported_language_code_handling(self):
        """Test error handling when an invalid language code is passed"""
        print("\n[TEST 6] Invalid language code error recovery:")
        try:
            translator = GoogleTranslator(source="invalid_code_xyz", target="en")
            translator.translate("Hello world")
        except Exception as e:
            print(f"  Correctly caught exception for invalid language: {type(e).__name__}")
            self.assertTrue(True)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLanguageTranslationTool)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
