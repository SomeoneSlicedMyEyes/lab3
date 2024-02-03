def volumeofsphere(r):
    V = 4/3 * 3.14 * r**3
    return V
r = float(input("Radius: "))
print(volumeofsphere(r))