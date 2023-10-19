import unittest

from exo2 import solution

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

class Exo2Test(unittest.TestCase):
	def test_solution(self):
		for coupla_strings in fixed_tests_True:
			self.assertEqual(solution(coupla_strings[0],coupla_strings[1]),True)
		for coupla_strings in fixed_tests_False:
			self.assertEqual(solution(coupla_strings[0],coupla_strings[1]),False)

a = Exo2Test()
a.test_solution()