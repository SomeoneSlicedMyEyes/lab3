def reverse(s):
    n = s.split()
    reversed_sentence = ' '.join(reversed(n))
    return reversed_sentence

n = input("sentence: ")
res = reverse(n)
print("reversed sentence: ", res)
