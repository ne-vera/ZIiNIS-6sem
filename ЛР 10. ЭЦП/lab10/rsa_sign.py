from hashlib import sha256

def gcd_extended(a, b):
    if a == 0 :
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)

class RSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.n = p * q
        self.e = e
        phi = (p - 1) * (q - 1)
        self.d = gcd_extended(e, phi)[1]
        if self.d < 0:
            self.d = phi + self.d
        self.public_key = (self.n, self.e)
        self.private_key = (self.n, self.d)
    
    def get_hash(self, m: str):
        return int.from_bytes(sha256(m.encode('utf-8')).digest(), 'big') % self.n

    def get_signature(self, m):
        return (self.get_hash(m) ** self.d) % self.n
    
    def check_signature(self, m, s):
        return self.get_hash(m) == ((s ** self.e) % self.n)
