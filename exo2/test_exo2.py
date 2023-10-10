import unittest
from exo2 import EndCompare

class Exo2Test(unittest.TestCase):
    
    def test_endComparaison_true_cases(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )
        for test_case in fixed_tests_True:
            input_str, ending_str = test_case
            self.assertTrue(EndCompare.endComparaison(input_str, ending_str))


    def test_endComparaison_false_cases(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )
        for test_case in fixed_tests_False:
            input_str, ending_str = test_case
            self.assertFalse(EndCompare.endComparaison(input_str, ending_str))

if __name__ == '__main__':
    unittest.main()