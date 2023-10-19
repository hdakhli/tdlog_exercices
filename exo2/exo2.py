import unittest

def solution(string, ending):
    return string.endswith(ending)

class Exo2_Test(unittest.TestCase):

    def test_true_cases(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )
        for string, ending in fixed_tests_True:
            self.assertEqual(solution(string, ending),True)
    
    
    def test_false_cases(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )
        for string, ending in fixed_tests_False:
            self.assertEqual(solution(string, ending),False)

