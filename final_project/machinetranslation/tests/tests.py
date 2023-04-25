import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):   
        self.assertEqual(english_to_french(None), '')

    def test_french_to_english(self):
        self.assertEqual(french_to_english(None), '')

    def test_english_to_french(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

    def test_french_to_english(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

if __name__ == '__main__':
    unittest.main()
