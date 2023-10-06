"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

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
from solution_module import solution

import unittest

# Importez votre fonction solution ici
# from votre_module import solution

class TestSolution(unittest.TestCase):
    def test_true_cases(self):
        fixed_tests_true = [
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        ]
        for s, ending in fixed_tests_true:
            with self.subTest(s=s, ending=ending):
                self.assertTrue(solution(s, ending), f"'{s}' should end with '{ending}' but returned False")

    def test_false_cases(self):
        fixed_tests_false = [
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        ]
        for s, ending in fixed_tests_false:
            with self.subTest(s=s, ending=ending):
                self.assertFalse(solution(s, ending), f"'{s}' should not end with '{ending}' but returned True")

if __name__ == '__main__':
    unittest.main()

