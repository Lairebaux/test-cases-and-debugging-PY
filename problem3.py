"""
Make this function return the sum of the two numbers that are passed to it. 
If the input array length is not 2, or if anything other than numbers are passed return undefined.

"""

# we need 7 test cases. I've provided 2.

inputs = [
    ["str", "list"],
    [123456],
    [-10, "xxx"],
    [7, 3],
    [100, 100],
    [-150, 25],
    [0, 9],
]

outputs = [
    None,
    None,
    None,
    10,
    200,
    -125,
    9
]


def f(l):
    if len(l) != 2 or not isinstance(l[0], int)\
            or not isinstance(l[1], int):
        return None
    return l[0] + l[1]



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

