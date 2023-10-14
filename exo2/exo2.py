"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""


#Create unit test using those cases:
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

import unittest

def solution(string, ending):
    return string.endswith(ending)

class TestSolution(unittest.TestCase):

    def test_solution_true(self):
        for test in fixed_tests_True:
            self.assertTrue(solution(*test))

    def test_solution_false(self):
        for test in fixed_tests_False:
            self.assertFalse(solution(*test))

if __name__ == '__main__':
    unittest.main()
    
    