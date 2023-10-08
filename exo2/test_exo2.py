from exo2 import solution
# Test cases
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

# Test the True cases
for test_case in fixed_tests_True:
    string, suffix = test_case
    result = solution(string, suffix)
    assert result is True, f"Failed for {string}, {suffix}"

# Test the False cases
for test_case in fixed_tests_False:
    string, suffix = test_case
    result = solution(string, suffix)
    assert result is False, f"Failed for {string}, {suffix}"

print("All test cases passed!")