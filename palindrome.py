def palindrome(str):
    # check id a string is palindrome
    for i, s in enumerate(str):
        if s != str[-1-i]:
            return False
        else:
            return True


def build_palindrome(str):
    # build a palindrome string by reversing it and concatenate the reversed with the original one
    return str[::-1] + str


def split_palindrome_others(str):
    # find the largest palindrome substring in a given string
    for i in range(len(str)):
        if palindrome(str[: -1 - i]):
            return str[: -1 - i], str[-1 - i :]


def build_min_palindrome(str):
    # starting from a given string, build a palindrome string by adding characters from the left side of
    # the original string
    if palindrome(str):
        print("Is already palindrome!")
        return str
    else:
        s_palindrome, s_other = split_palindrome_others(str)
        return s_other[::-1] + str


strs = ['ABA', 'ABBA', 'ADDSGG', 'EXE', 'BCBAZ']

print("First EX.")
for s in strs:
    print(palindrome(s))

print("Second EX.")
built_pal = []
for s in strs:
    built_pal.append(build_palindrome(s))
print(built_pal)
for s in built_pal:
    print(palindrome(s))

print("Third EX.")
built_min_pal = []
for s in strs:
    built_min_pal.append(build_min_palindrome(s))
print(built_min_pal)

print("\n\n\n[CHECK!]\n")
for s in built_min_pal:
    print(palindrome(s))
