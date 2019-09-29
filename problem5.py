import operator
import functools

# we need 5 test cases.
inputs = [
    [2, 7],
    ["1", "3"]
    [1, 3],
    [0, 1000],
    [1, 99]
]

outputs = [
    14, None, 3, 0, 99
]

"""The input of the function is an array.
Make this function return the product of the two numbers in the array.
If the input array length is not 2, or if anything other than numbers are passed, return undefined."""


def f(x):
    if len(x) != 2:
        return
    if not isinstance(x[0], int) and not isinstance(x[1], int):
        return None
    return functools.reduce(operator.mul, x)


def eq(lhs, rhs):
    if isinstance(lhs, list):
        for i in range(len(lhs)):
            if lhs[i] != rhs[i]:
                return False
            return True
    return lhs == rhs


def verify_equals(lhs, rhs):
    if not eq(lhs, rhs):
        raise Exception("Expected output does not match actual output")


def run_test(i):
    expected = outputs[i]
    actual = f(inputs[i])
    verify_equals(expected, actual)


for t in range(len(inputs)):
    run_test(t)
print("All tests passed for " + __file__)
