import operator
import functools

"""
The function takes an array. 
The array has length 3. The first element of the array is a string that represents an operation.
If the operation is "add", return the sum of the two other elements of the array. 
"sub" return their difference. "mult" return their product.  
Anything else return undefined. 
For example:
f(["add", 10, 20]); // 30
f(["mult", 2, 3]); // 6
f(["spoof", 10, 10]); // undefined

"""



inputs = [
    ["add", 10, 20],
    ["sub", 20, 10],
    ["", 10, 20],
    ["mult", 10, 20],
    ["asdf", 0],
    [0, 0, 0]
,]

outputs = [
    30, 10, None, 200, None, None
]


def f(x):
    if x[0] == "add":
        return functools.reduce(operator.add, x[1:])
    elif x[0] == "sub":
        return functools.reduce(operator.sub, x[1:])
    elif x[0] == "mult":
        return functools.reduce(operator.mul, x[1:])
    else:
        return None


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
