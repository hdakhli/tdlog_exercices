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
    
    for i in fixed_tests_True:
        print (f' {i}:{solution(i[0],i[1])}')
    for i in fixed_tests_False:
        print (f' {i}:{solution(i[0],i[1])}')
unittest.main()