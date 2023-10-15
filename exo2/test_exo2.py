import unittest

from exo2 import solution


class TestSolution(unittest.TestCase):

    def test_true_cases(self):
        true_test_cases = [
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        ]
        for input_str, ending_str in true_test_cases:
            with self.subTest(input_str=input_str, ending_str=ending_str):
                self.assertTrue(solution(input_str, ending_str))

    def test_false_cases(self):
        false_test_cases = [
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        ]
        for input_str, ending_str in false_test_cases:
            with self.subTest(input_str=input_str, ending_str=ending_str):
                self.assertFalse(solution(input_str, ending_str))
