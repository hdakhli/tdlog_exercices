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


class Exo1Test(unittest.TestCase):

    def fixed_tests_True(self):
        fixed_True = [
            ["samurai", "ai"],
            ["ninja",   "ja"],
            ["sensei",  "i"],
            ["abc",     "abc"],
            ["abcabc",  "bc"],
            ["fails",   "ails"],
        ]

        for strings in fixed_True:
            self.assertEqual(True, solution(strings[0], strings[1]))

    def fixed_tests_False(self):
        fixed_False = [
            ["sumo",    "omo"],
            ["samurai", "ra"],
            ["abc",     "abcd"],
            ["ails",    "fails"],
            ["this",    "fails"],
            ["spam",    "eggs"],
        ]

        for strings in fixed_False:
            self.assertEqual(False, solution(strings[0], strings[1]))


if __name__ == "__main__":
    unittest.main()
