def convert_grams_to_ounces(g):
    o = 28.3495231 * g
    return o

g = float(input("g: "))
o= convert_grams_to_ounces(g)

print(f"g = {g} => ounces = {o}.")
