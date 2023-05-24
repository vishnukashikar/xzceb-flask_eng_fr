import unittest
from translator import engtofr , frtoeng

class TestenglishToFrench(unittest.TestCase):
 def test1(self):
  self.assertEqual(engtofr('hello'),'Bonjour')
  self.assertNotEqual(engtofr('hello'),'oui')
class TestfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frtoeng('bonjour'),'Hello')
        self.assertNotEqual(frtoeng('bonjour'),'bye')
unittest.main()       

