import unittest

import translator


class translateFunctionsTest(unittest.TestCase):

    def test_englishToFrench():
        englishText = "Hello"
        eng_fr = translator.englishToFrench(englishText)
        assertIsNotNone(englishText)
        
        
    def test_frenchToEnglish():
        frenchText = "Hello"
        eng_fr = translator.frenchToEnglish(frenchText)
        assertIsNotNone(frenchText)



    def test_englishToFrench():
        eng_fr = translator.englishToFrench("Hello")
        assertEqual(eng_fr, "Bonjour")
        
        
    def test_frenchToEnglish():
        eng_fr = translator.frenchToEnglish("Bonjour")
        assertEqual(eng_fr, "Hello")

