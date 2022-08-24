"""
Write a function that accepts an integer i, and
• if i is multiple of 3, print "Fizz" instead of the number.
• if i is multiple of 5, print "Buzz" instead of the number.
• if i is multiple of both 3 and 5, print "FizzBuzz" instead of the number.
• if no conditions are met, print the number i.
Test the function with all the numbers between ad .
"""
def multipleOf(n, d):
    return n % d == 0


def grater_than(n1, n2):
    return n1 > n2


def FizzBuzz(n, v1, v2, function):
    cond1 = function(n, v1)
    cond2 = function(n, v2)

    if cond1 and cond2:
        print("FizzBuzz")
    elif cond1:
        print("Fizz")
    elif cond2:
        print("Buzz")

    else:
        print(i)

N = 15
value1 = 3
value2 = 5

functions = {
    '1': grater_than,
    '2': multipleOf}

sel = input(f"insert the type condition: \n{functions}\n ")

print(functions[sel])
for i in range(1, N + 1):
    FizzBuzz(i, value1, value2, functions[sel])
