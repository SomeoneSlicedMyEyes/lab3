def unique_elements(lst):
    unique = []
    for e in lst:
        if e not in unique:
            unique.append(e)
    return unique
n = input("numbers: ")
list = [int(x) for x in n.split()]
res = unique_elements(list)
print(res)
