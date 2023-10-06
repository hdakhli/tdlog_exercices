def solution(word:str, end:str):
    return word.endswith(end)

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


for test in fixed_tests_True:
    input_str, ending_str = test
    assert solution(input_str, ending_str) == True

for test2 in fixed_tests_False:
    input_str, ending_str = test2
    assert solution(input_str, ending_str) == False