import sys



def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


if __name__ == "__main__":
    args = sys.argv
    print("run as a standalone script")
    print(f"the factorial of {args[1]} is: {factorial(int(args[1]))}")
else:
    print("I am a module")
