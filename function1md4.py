def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

def filter_prime(n):
    primes = []
    for a in n:
        if is_prime(a):
            primes.append(a)
    return primes

n = input("n: ")
list = [int(a) for a in n.split()]

primes = filter_prime(list)

print("list:", list)
print("Primes:", primes)
