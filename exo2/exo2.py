"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""
def solution(s, ending):
    return s.endswith(ending)

# Examples:
print(solution('abc', 'bc'))  # True
print(solution('abc', 'd'))   # False

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

class TestSolution(unittest.TestCase):

    def test_true_cases(self):
        for s, ending in fixed_tests_True:
            with self.subTest(s=s, ending=ending):
                self.assertTrue(solution(s, ending))

    def test_false_cases(self):
        for s, ending in fixed_tests_False:
            with self.subTest(s=s, ending=ending):
                self.assertFalse(solution(s, ending))

# Cas de tests fournis
fixed_tests_True = (
    ("samurai", "ai"),
    ("ninja", "ja"),
    ("sensei", "i"),
    ("abc", "abc"),
    ("abcabc", "bc"),
    ("fails", "ails"),
)

fixed_tests_False = (
    ("sumo", "omo"),
    ("samurai", "ra"),
    ("abc", "abcd"),
    ("ails", "fails"),
    ("this", "fails"),
    ("spam", "eggs")
)

if __name__ == '__main__':
    unittest.main()
