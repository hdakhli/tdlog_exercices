import unittest

def solution(string, ending):
    return string.endswith(ending)

class Exo2Test(unittest.TestCase):
    def test_true_cases(self):
        true_cases = [
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails")
        ]
        for s, e in true_cases:
            with self.subTest(s=s, e=e):
                self.assertTrue(solution(s, e))

    def test_false_cases(self):
        false_cases = [
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs")
        ]
        for s, e in false_cases:
            with self.subTest(s=s, e=e):
                self.assertFalse(solution(s, e))

if __name__ == '__main__':
    unittest.main()
