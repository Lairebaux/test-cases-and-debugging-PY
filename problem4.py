"""
return letter at specified position in string which is second position
in list
"""

inputs = [
    ["hello", 4],
    ["python", 0],
    ["escape", 1],
    [5, "error"],
    ["devoir", -1],
    ["bonjour", 5],
    ["walking outside", 6],
    ["septembre", 3]
]


outputs = [
    "o", "p", "s", None, "r", "u", "g", "t"
]


def f(arr):
    word = arr[0]
    idx = arr[1]
    if not isinstance(word, str) and not isinstance(idx, int):
        return None
    return word[idx]


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

