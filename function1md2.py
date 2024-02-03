def Celsius(F):
    C = 5/9 * (F - 32)
    return C

F = float(input("Farenheit: "))
C = Celsius(F)

print(f"F = {F} => C = {C}")
