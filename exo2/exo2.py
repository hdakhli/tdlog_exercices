"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""
import string


def solution(first_string: string, second_string: string) -> string:
    second_string_len = len(second_string)
    first_string_end = first_string[-second_string_len:]

    return first_string_end == second_string


print(solution('abc', 'bc'))
print(solution('abc', 'd'))
