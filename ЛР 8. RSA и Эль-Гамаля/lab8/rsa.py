import Crypto.Util.number
from utils import *
import time

def generate_key(bit_num: int):
    p = Crypto.Util.number.getPrime(bit_num, randfunc = Crypto.Random.get_random_bytes)
    q = Crypto.Util.number.getPrime(bit_num, randfunc = Crypto.Random.get_random_bytes)
    print('p: ', p)
    print('q: ', q)

    # Вычисление произведения p и q
    n = p * q
    print('n: ', n)

    # Выбор открытого ключа e
    phi = (p-1)*(q-1)
    e = generate_coprime(phi)
    print ('e: ', e)

    _, d, _ = extended_gcd(e, phi)
    if d < 0:
        d = phi + d
    print('d: ', d)
    return ((e, n), (d, n))


def encode(message : str, package : tuple[int, int]):
    e, n = package
    ciphertext = [pow(ord(c), e, n) for c in message]
    return ciphertext

def decode(ciphertext : str, package):
    d, n = package
    plaintext =''
    for c in ciphertext:
        plaintext += chr(pow(c,d,n))
    return (''.join(plaintext))

def rsa(message: str):
    public, private = generate_key(8)
    print([ord(c) for c in message])
    start_time = time.time()
    encoded = encode(message, public)
    encoding_time = time.time() - start_time
    print('Зашифрованное сообщение: ')
    print(''.join(map(lambda x: str(x),encoded)))
    start_time = time.time()
    decoded = decode(encoded, private)
    decoding_time = time.time() - start_time
    print('Расшифрованное сообщение:', decoded)
    print('Время зашифрования:', encoding_time)
    print('Время расшифрования:', decoding_time)

    len_enc = 0
    for c in encoded:
        len_enc += len(str(c))
    print('Длина шифротекста:', len_enc)