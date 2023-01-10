import unittest
from translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishtofrench("hello"),"hola")
        self.assertEqual(englishtofrench("hello"),"Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(frenchtoenglish("Bonjour"),"hola")
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
        
unittest.main()