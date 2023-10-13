import unittest
from exo2 import solution

class Exo2Test(unittest.TestCase):

    def test_solution_true(self):
        # Test cases where the function should return True
        test_cases_true = [
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        ]

        for input_str, ending_str in test_cases_true:
            result = solution(input_str, ending_str)
            self.assertTrue(result, f"Expected True for '{input_str}' with '{ending_str}' but got {result}")

    def test_solution_false(self):
        # Test cases where the function should return False
        test_cases_false = [
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        ]

        for input_str, ending_str in test_cases_false:
            result = solution(input_str, ending_str)
            self.assertFalse(result, f"Expected False for '{input_str}' with '{ending_str}' but got {result}")

if __name__ == '__main__':
    unittest.main()
