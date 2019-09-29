"""
Make this function return the last ter of the string that is passed to it.
If the string does not have a last ter, return undefined

"""

inputs = [
    "abc", "job", "x1x", "eiou", "Rui",""

]

outputs = [
    "c", "b", "x", "u", "i", None
]


def f(s):
    if len(s) == 0:
        return None
    return s[-1]


def eq(lhs, rhs):
    if isinstance(lhs, list):
        for i in range(len(lhs)):
            if lhs[i] != rhs[i]:
                return False
            return True
    return lhs == rhs


#
#
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

