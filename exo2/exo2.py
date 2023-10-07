"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""
def solution(word, ends_with):
    l = len(ends_with)
    reconstruct = ""
    for i in range(l):
        reconstruct += word[i-l]         
    return reconstruct == ends_with

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

fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = [("sumo", "omo"), ("samurai", "ra"), ("abc","abcd"), ("ails","fails"), ("this", "fails"), ("spam", "eggs")]

class exo2Test(unittest.TestCase):

    def test_fixed_tests_True_func(self):
        for word, ends_with in fixed_tests_True:
            self.assertTrue(solution(word, ends_with))

    def test_fixed_tests_False_func(self):
        for word, ends_with in fixed_tests_False:
            self.assertFalse(solution(word, ends_with))

