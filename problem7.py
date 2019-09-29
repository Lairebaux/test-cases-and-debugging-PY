
"""

The function input is an array as input.
The first element of the array is a string. The second is a number.
Make this function return the string repeated as many times as specified by the second element of the array.
If a negative number or zero is specified, return an empty string.
If any invalid parameters are supplied return undefined.

For example:

f(["foo", 3]) // "foofoofoo"
f(["fo", 3]) // "fofofo"
f(["foo", -1]) // ""
"""


inputs = [
    ["foo", 3],
    ["abs", -1],
    ["ab", 3],
    [3, "jilg"],
    ["12345 ", 5],

]

outputs = [
    "foofoofoo",
    "",
    "ababab",
    None,
    "12345 12345 12345 12345 12345 "
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


def f(x):
    if not isinstance(x[0], str) and not isinstance(x[1], int):
        return None
    if x[1] <= 0:
        return ""
    return x[0] * x[1]


def run_test(i):
    expected = outputs[i]
    actual = f(inputs[i])
    verify_equals(expected, actual)


for t in range(len(inputs)):
    run_test(t)
print("All tests passed for " + __file__)
