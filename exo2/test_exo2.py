from exo2 import ends_with


def test_ends_with():
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

    for input_string, ending in fixed_tests_True:
        assert ends_with(input_string, ending) is True

    for input_string, ending in fixed_tests_False:
        assert ends_with(input_string, ending) is False

    print("All tests passed!")


# Run the unit tests
test_ends_with()
