from asyncio.windows_events import NULL
import unittest
from translator import french_to_english, english_to_french

class TestenglishToFrench(unittest.TestCase):
    def testen2fr_is_null(self):
        """Test for null input"""
        self.assertEqual(english_to_french(None), None)
    
    def testen2fr_translation(self):
        """Test for correct translation"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestfrenchToEnglish(unittest.TestCase): 
    def testfr2en_is_null(self):
        """Test for null input"""
        self.assertEqual(french_to_english(None), None)
    
    def testen2fr_translation(self):
        """Test for correct translation"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()