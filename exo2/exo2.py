"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""

"""
Create unit test using those cases:
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
"""

def solution(string, ending):
    return string.endswith(ending)

def test_solution():
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
        ("spam", "eggs"),
    )

    for test_case in fixed_tests_True:
        assert solution(*test_case) is True

    for test_case in fixed_tests_False:
        assert solution(*test_case) is False

test_solution()
