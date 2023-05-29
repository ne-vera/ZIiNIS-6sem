from hashlib import sha256


def gcd_extended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)


class Schnorr:
    def __init__(self, p, q, g, x):
        self.p = p
        self.q = q
        self.g = g
        self.x = x
        self.y = (g ** (q - x)) % p
        self.public_key = (self.p, self.q, self.g, self.y)
        self.private_key = (self.p, self.q, self.g, self.x)
    
    def get_hash(self, m: str):
        return int.from_bytes(sha256(m.encode('utf-8')).digest(), 'big') % self.p
    
    def get_signature(self, m):
        k = 2
        while gcd_extended(k, self.p - 1)[0] != 1:
            k += 1
        a = (self.g ** k) % self.p
        h = self.get_hash(m + str(a))
        b = (k + self.x * h) % self.q
        return (h, b)
    
    def check_signature(self, m, s):
        h = s[0]
        b = s[1]
        X = ((self.g ** b) * (self.y ** h)) % self.p
        return h == self.get_hash(m + str(X))