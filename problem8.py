"""

Make this function return the input string, reversed.
For example "hello" would return "olleh" and "how are you" would return "uoy era woh".
You must use at least one for loop for this exercise.

"""


inputs = [
    "hello",
    "how are you",
    "abcd",
    "1 2 3 4",
    ""

]

outputs = [
    "olleh",
    "uoy era woh",
    "dcba",
    "4 3 2 1",
    "toi&moi"

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


def f(word):
    ans = ""
    for letter in word:
        ans = letter + ans
    return ans


def run_test(i):
    expected = outputs[i]
    actual = f(inputs[i])
    verify_equals(expected, actual)


for t in range(len(inputs)):
    run_test(t)
print("All tests passed for " + __file__)
