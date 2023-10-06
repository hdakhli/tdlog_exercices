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
class EXO2(unittest.TestCase):
    def test_solution(self):
        for i in fixed_tests_True:
            s=solution(i[0],i[1])
            self.assertEqual(s,True)
        for j in fixed_tests_False:
            s=solution(j[0],j[1])
            self.assertEqual(s,False)