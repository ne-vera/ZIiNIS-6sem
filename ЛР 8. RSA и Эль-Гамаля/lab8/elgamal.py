import Crypto.Util.number
from utils import *
import time

def primitive_root(p_val):
    while True:
        g = random.randrange(3, p_val)
        if pow(g, 2, p_val) == 1:
            continue
        if pow(g, p_val, p_val) == 1:
            continue
        return g

def generate_key(bit_num: int):
    p = Crypto.Util.number.getPrime(bit_num, randfunc = Crypto.Random.get_random_bytes)
    print('p:', p)

    g = primitive_root(p)
    print('g:', g)

    x = random.randint(1, p-1)
    print('x:', x)

    y = g**x % p
    print('y:', y)

    return ((p,g,y), (p,g,x))

def encode(message, package):
    p, g, y = package
    a = []
    b = []
    for m in message:
        k = random.randint(1, p-1)
        a.append(pow(g,k,p))
        b.append(pow(y, k) * ord(m) % p)
    ciphertext = [(a[i], b[i]) for i in range(0, len(b))]
    return ciphertext

def decode(ciphertext, package):
    p, g, x = package
    plaintext = []
    for c in ciphertext:
        a_x = pow(c[0], x)
        _, a_r, _ = extended_gcd(a_x, p)
        if a_r < 0:
            a_r = p + a_r
        plaintext.append(chr((c[1]*a_r) % p))
    return (''.join(plaintext))
          

def elgamal(message):
    print('Генерация ключевой информации')
    public, private = generate_key(8) 
    start_time = time.time()
    encoded = encode(message, public)
    encoding_time = time.time() - start_time
    print('Зашифрованное сообщение:', encoded)
    start_time = time.time()
    decoded = decode(encoded, private)
    decoding_time = time.time() - start_time
    print('Расшифрованное сообщение:', decoded)
    print('Время зашифрования:', encoding_time)
    print('Время расшифрования:', decoding_time)

    len_enc = 0
    for c in encoded:
        len_enc += len(str(c[0])) + len(str(c[1]))
    print('Длина шифротекста:', len_enc)