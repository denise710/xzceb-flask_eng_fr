"""This module realizes a Translator for English>French and French>English"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """This function translates Text from English to French"""
    french_text = MyMemoryTranslator("en-GB", "fr-FR").translate(english_text)
    return french_text

def french_to_english(french_text):
    """This function translates Text from French to English"""
    english_text = MyMemoryTranslator("fr-FR","en-GB").translate(french_text)
    return english_text
