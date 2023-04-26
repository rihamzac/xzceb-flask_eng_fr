import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):


    def test_english_to_french(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")
        self.assertNotEqual(result,None)

    def test_french_to_english(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")
        self.assertNotEqual(result,None)

if __name__ == '__main__':
    unittest.main()
