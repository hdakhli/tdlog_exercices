"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""
import unittest

def solution(string, ending):
    return string.endswith(ending)

class TestSolution(unittest.TestCase):
    def test_true_cases(self):
        fixed_tests_True = [
            ( "samurai", "ai"    ),
            ( "ninja",   "ja"    ),
            ( "sensei",  "i"     ),
            ( "abc",     "abc"   ),
            ( "abcabc",  "bc"    ),
            ( "fails",   "ails"  ),
        ]
        
        for x in fixed_tests_True:
            input_string, ending_string = x
            self.assertTrue(solution(input_string, ending_string))

    def test_neg_cases(self):
        fixed_tests_False = [
            ( "sumo",    "omo"   ),
            ( "samurai", "ra"    ),
            ( "abc",     "abcd"  ),
            ( "ails",    "fails" ),
            ( "this",    "fails" ),
            ( "spam",    "eggs"  )
        ]
        for x in fixed_tests_False:
            input_string, ending_string = x
            self.assertFalse(solution(input_string, ending_string))

if __name__ == '__main__':
    unittest.main()

    


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
