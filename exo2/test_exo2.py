import unittest
from exo2 import Verification


class Exo2Test(unittest.TestCase):
    def test_identique(self):
        self.assertTrue(Verification("abcdef", "def"))

    def test_difference(self):
        self.assertFalse(Verification("abcdef", "xyz"))

    def test_desaccord_de_taille(self):
        self.assertFalse(Verification("abc", "xyzw"))
