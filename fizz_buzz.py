"""
Write a function that accepts an integer i, and
• if i is multiple of 3, print "Fizz" instead of the number.
• if i is multiple of 5, print "Buzz" instead of the number.
• if i is multiple of both 3 and 5, print "FizzBuzz" instead of the number.
• if no conditions are met, print the number i.
Test the function with all the numbers between ad .
"""
def multipleOf3(n):
    return n % 3 == 0
def multipleOf5(n):
    return n % 5 == 0

def FizzBuzz(i):
    if multipleOf3(i) and multipleOf5(i):
        print("FizzBuzz")
    elif multipleOf3(i):
        print("Fizz")
    elif multipleOf5(i):
        print("Buzz")

    else:
        print(i)

N = 15
for i in range(1, N + 1):
    FizzBuzz(i)
