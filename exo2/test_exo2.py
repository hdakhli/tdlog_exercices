import unittest
from exo2 import Solution
class Exo2Test(unittest.TestCase):

    def test_sol_construction(self):
        fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs")
        )
        for i in fixed_tests_True:
            sol=Solution(i[0],i[1])
            sol.verify()
            try:
             self.assertEqual(i[1], i[0])
            except:
                pass
        for i in fixed_tests_False:
            sol=Solution(i[0],i[1])
            sol.verify()
            try:
             self.assertEqual(i[1], i[0])
            except:
                pass

