import functools
import operator

"""
Make this function return the sum of all the numbers in the input array.
If any element in the array is not a number, skip it.
If the array is empty, return zero.

"""


inputs = [
    [1,2,3,4,5, ""],
    [],
    [100, "", 56]
]

outputs = [
    15,
    0,
    156
]


def f(l):
    pass

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



