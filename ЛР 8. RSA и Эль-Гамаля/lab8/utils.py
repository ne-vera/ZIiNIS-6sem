from math import sqrt
import random

def get_prime(min, max):
    sieve = []
    a = [0] * (max + 1)

    for i in range(max + 1):
        a[i] = 1
    
    for i in range(2, int(sqrt(max)) + 1):
        if a[i] == 1:
            j = 2
            while i * j <= max:
                a[i * j] = 0
                j = j + 1
    
    for i in range(2, max + 1):
        if a[i] == 1:
            # print(i, end = ' ')
            sieve.append(i)

    sieve = list(filter(lambda num: num >= min, sieve))
    return(sieve)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def generate_coprime(phi):
    while True:
        e = random.randrange(2, phi)
        gcd, x, y = extended_gcd(e, phi)
        if gcd == 1:
            return e