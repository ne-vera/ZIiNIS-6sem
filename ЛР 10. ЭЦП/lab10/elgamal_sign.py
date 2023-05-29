from hashlib import sha256


def gcd_extended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)


class Elgamal:
    def __init__(self, p, g, x):
        self.p = p
        self.g = g
        self.x = x
        self.y = (g ** x) % p
        self.public_key = (self.p, self.g, self.y)
        self.private_key = (self.p, self.g, self.x)
    
    def get_hash(self, m: str):
        return int.from_bytes(sha256(m.encode('utf-8')).digest(), 'big') % self.p
    
    def get_signature(self, m):
        h = self.get_hash(m)
        k = 2
        while gcd_extended(k, self.p - 1)[0] != 1:
            k += 1
        k_r = gcd_extended(k, self.p - 1)[1]
        a = (self.g ** k) % self.p
        b = ((h - self.x * a) * k_r) % (self.p - 1)
        return (a, b)
    
    def check_signature(self, m, s):
        h = self.get_hash(m)
        a = s[0]
        b = s[1]
        return ((self.g ** h) % self.p) == ((self.y ** a) * (a ** b)) % self.p
