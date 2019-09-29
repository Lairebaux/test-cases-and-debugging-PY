"""
Make this function return the input string, capitalized. You must use a for loop. For example:

f("hello world"); // Hello World
f("ALL YOUR BASE ARE BELONG"); // All Your Base Are Belong

HINT:
   - Use a for loop to capitalize the letters one by one
"""

# we need 5 test cases.
inputs = [
    "hello world", "bon", "abcd", "BONJOUR", ""
]

outputs = [
    "Hello World", "Bon", "Abcd", "Bonjour", ""
]


def f(s):
    ans = []
    for words in s.split():
        for each_word in (words, " ")[:-1]:
            ans.append(each_word.capitalize())
    return " ".join(ans)


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
