import sys

string = sys.argv[1]

if string == string[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")