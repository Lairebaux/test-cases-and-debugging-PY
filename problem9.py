"""

Make this function return the longest word in the input string.
If the input string is empty then return an empty string.
If multiple words have the same length, return the last one that matches.

Example
  f("hey hello morning") returns "morning"

HINTS:
   - You'll need to use the split string method
   - A for loop might be helpful

"""


# we need 5 test cases.
inputs = [
    "bo  bonjour soir",
    "one two fve",
    "one fve two",
    "un deuxx cinqq trois",
    ""

]

outputs = [
    "bonjour",
    "fve",
    "two",
    "trois",
    ""
]


def eq(lhs, rhs):
    """lhs outputs; rhs: inputs"""
    if isinstance(lhs, list):
        for i in range(len(lhs)):
            if lhs[i] != rhs[i]:
                return False
            return True
    return lhs == rhs


def verify_equals(lhs, rhs):
    if not eq(lhs, rhs):
        raise Exception("Expected output does not match actual output")


def f(w):
    if w == "":
        return ""
    words = w.split()
    words_sort = sorted(words, key=len)
    return words_sort[-1]


def run_test(i):
    expected = outputs[i]
    actual = f(inputs[i])
    verify_equals(expected, actual)


for t in range(len(inputs)):
    run_test(t)
print("All tests passed for " + __file__)
