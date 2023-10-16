import unittest

from exo2 import solution

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


class Exo2Test(unittest.TestCase):


    def test_solution_True(self):
        for string, ending in fixed_tests_True:
            self.assertTrue(solution(string, ending))

    def test_solution_False(self):
        for string, ending in fixed_tests_False:
            self.assertFalse(solution(string, ending))

if __name__ == '__main__':
    unittest.main()
