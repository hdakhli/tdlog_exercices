"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""
class Str_true:
    def __init__(self, str1=str, str2=str):
        self._str1 = str1
        self._str2 = str2

    def verify_str_true(self, arg1, arg2):
        self._arg1 = arg1
        self._arg2 = arg2

        condition1=self._arg1.endswith(self._arg2)
        condition2= self._arg2 != ""
        if condition2:
            if condition1:
              return True
            else:
              return False 


'''
Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)'''
r1=fixed_tests_true=Str_true()
r2=fixed_tests_false=Str_true()
print(r1.verify_str_true("samurai", "ai"))
print(r2.verify_str_true("sumo", "omo"))

'''fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)'''

