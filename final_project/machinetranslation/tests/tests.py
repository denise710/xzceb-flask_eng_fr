import unittest
import translator

class TranslatorTestMethods(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertEqual(translator.english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(translator.english_to_french("Hello"), "Hallo")

    def testFrenchToEnglish(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english("Bonjour"), "Hallo")