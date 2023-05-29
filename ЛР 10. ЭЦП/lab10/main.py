from rsa_sign import RSA
from elgamal_sign import Elgamal
from schnorr_sign import Schnorr
from hashlib import sha256
from time import time


message = 'v'


print('--------------- RSA ---------------')
rsa = RSA(3, 3, 3)
print(f'p = {rsa.p}')
print(f'q = {rsa.q}')
print(f'n = {rsa.n}')
print(f'e = {rsa.e}')
print(f'd = {rsa.d}')
print(f"Хеш сообщения: {int.from_bytes(sha256(message.encode('utf-8')).digest(), 'big')}")
start = time()
signature = rsa.get_signature(message)
end = time() - start
print(f'Подпись: {signature}')
print(f'Время вычисления: {end}')
print(f'Проверка: {rsa.check_signature(message, signature)}\n\n')


print('--------------- Эль-Гамаль ---------------')
elgamal = Elgamal(3, 2, 2)
print(f'p = {elgamal.p}')
print(f'g = {elgamal.g}')
print(f'x = {elgamal.x}')
print(f'y = {elgamal.y}')
print(f"Хеш сообщения: {int.from_bytes(sha256(message.encode('utf-8')).digest(), 'big')}")
start = time()
signature = elgamal.get_signature(message)
end = time() - start
print(f'Подпись: {signature}')
print(f'Время вычисления: {end}')
print(f'Проверка: {elgamal.check_signature(message, signature)}\n\n')


print('--------------- Шнорр ---------------')
schnorr = Schnorr(48731, 443, 11444, 357)
print(f'p = {schnorr.p}')
print(f'q = {schnorr.q}')
print(f'g = {schnorr.g}')
print(f'x = {schnorr.x}')
print(f'y = {schnorr.y}')
print(f"Хеш сообщения: {int.from_bytes(sha256(message.encode('utf-8')).digest(), 'big')}")
start = time()
signature = schnorr.get_signature(message)
end = time() - start
print(f'Подпись: {signature}')
print(f'Время вычисления: {end}')
print(f'Проверка: {schnorr.check_signature(message, signature)}\n')
