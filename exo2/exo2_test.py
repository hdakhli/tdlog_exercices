"unit test"

fixed_tests_True = (
    ("aisamur", "ai"),
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
    ("spam", "eggs"),
)

import unittest

from exo2 import solution


class Exo1Test(unittest.TestCase):

    def test_solution_construction(self):
        for strings,ending in fixed_tests_True :
            self.assertEqual(True, solution(strings,ending))
        for strings,ending in fixed_tests_False :
            self.assertEqual(False, solution(strings,ending))

        

