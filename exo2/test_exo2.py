"""
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
"""
import unittest

from exo2 import solution


class Exo2Test(unittest.TestCase):

    def test_solution(self):
        fixed_test_true = solution("samurai", "ai")
        self.assertEqual(True, fixed_test_true)
        fixed_test_false = solution("samurai", "tai")
        self.assertEqual(False, fixed_test_false)
