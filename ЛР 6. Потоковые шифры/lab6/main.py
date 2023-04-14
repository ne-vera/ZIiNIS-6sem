# Генерация ПСП Вариант 2 RSA p, q, e – 256-разрядные числа
# Алгоритм RC4  Вариант 8  n = 6 Ключ: 20, 21, 22, 23, 60, 61, оценка скорости 
from prs import *
from rc4 import *
from datetime import datetime

print('--------------- ПСП ---------------')
print('Введите длину последовательности t:')
t = int(input())
start_time = datetime.now()
prs = generate_rsa_prs(t)
print('\nПСП:', prs)
print(f'Время генерации ПСП RSA: {datetime.now() - start_time}')

print()

print('--------------- RC4 ---------------')
print('Введите сообщение:')
message = input()
key = '20 21 22 23 60 61'
print(f'RC4 ключ: {key}')
cipher = rc4_encrypt(message, key)
print(f'Зашифрованное сообщение: {cipher}')
decipher = rc4_decrypt(cipher, key)
print(f'Дешифрованное сообщение: {decipher}\n')

start_time = datetime.now()
gen = stream_generation(key_scheduling([ord(char) for char in key]))
print(gen)
print(f'Время генерации ПСП RC4: {datetime.now() - start_time}')