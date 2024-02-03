def is_palindrome(s):
    snew = ''.join(s.lower().split())
    return snew == snew[::-1]

n = input()
if is_palindrome(n):
    print("It is a palindrome")
else:
    print("It is not a palindrome.")
