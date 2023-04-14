import random
from datetime import datetime
import sys

# def generate_superincreasing_sequence(z : int) -> list:
#     seq = [1] # начинаем с единицы
#     while len(seq) < z:
#         next_num = sum(seq) + 1 # следующее число в последовательности
#         seq.append(next_num)
#     return seq

def generate_superincreasing_sequence(n):
    high_bit = 100
    seq = [random.getrandbits(high_bit)] # начинаем с случайного 100-битного числа
    while len(seq) < n:
        next_num = sum(seq) + 1 # следующее число в последовательности
        seq.append(next_num)
    return seq

def get_public_key(seq : list, a : list, n : list) -> list:
    public_key = []
    for num in seq:
        public_key.append((a * num) % n)
    return public_key

def extended_gcd(a : int, b : int):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def generate_coprime(phi : int) -> int:
    while True:
        e = random.randrange(2, phi)
        gcd, x, y = extended_gcd(e, phi)
        if gcd == 1:
            return e

def generate_constants(seq : list) -> int:
    n =  sum(seq) + 1
    a = generate_coprime(n)
    return a, n

def encode(message : str, seq : list, a: int, n : int,  z : int) -> list:
    public_key = get_public_key(seq, a, n)
    print('Публичный код:', public_key)

    binary_str = ''.join(format(ord(x), '08b') for x in message) 
    binary_list = [binary_str[i:i+z] for i in range(0, len(binary_str), z)]

    print('Сообщение:')
    for bin in binary_list:
        print(bin)
    print()
    encoded = []
    for bin in binary_list:
        s = 0
        for i in range(len(bin)):
            if bin[i] == '1':
                s += public_key[i]
        encoded.append(s)
    return encoded

def get_knapsack_set(value: int, seq: list) -> str:
    result = ''
    seq.sort(reverse=True)
    for num in seq:
        if num <= value:
            result = '1' + result
            value -= num
        else: result = '0' + result
    return result

def decode(encoded : list, seq : list, a : int, n : int) -> str:
    _, a_r, _ = extended_gcd(a, n)
    if a_r < 0:
        a_r = n + a_r
    decoded_seq = []
    for c in encoded:
        decoded_seq.append((c * a_r) % n)
    print('S:', decoded_seq)
    decoded_bin = []
    for num in decoded_seq:
        decoded_bin.append(get_knapsack_set(num, seq))
    print('Расшированное сообщение в бинарном виде:')
    for bin in decoded_bin:
        print(bin)
    decoded = ''
    for bin in decoded_bin:
        decoded += chr(int(bin, 2))
    return decoded


def knapsack(message: str, z : int):
    seq = generate_superincreasing_sequence(z)
    print('Сверхвозрастающая последовательность:', seq)
    a, n = generate_constants(seq)
    print('a = ', a, 'n = ', n)

    start_time = datetime.now()
    encoded = encode(message, seq, a, n, z)
    print(f'Время зашифрования: {datetime.now() - start_time}')
    start_time = datetime.now()
    decoded = decode(encoded, seq, a, n)
    print()
    print(f'Время дешифрования: {datetime.now() - start_time}')
    print('Расшифрованное сообщение:', decoded)
