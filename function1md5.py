from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))
s = input("string: ")
print("permutations: ")
print_permutations(s)
