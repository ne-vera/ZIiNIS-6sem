# Вариант 3
# DES-EDE3
# Приложение должно реализовывать следующие операции: 
# • разделение входного потока данных на блоки требуемой длины с необходимым дополнением последнего блока; 
# • выполнение требуемых преобразований ключевой информации; 
# • выполнение операций зашифрования/расшифрования; 
# • оценка скорости выполнения операций зашифрования/расшифрования; 
# • пошаговый анализ лавинного эффекта с подсчетом количества изменяющихся символов по отношению к исходному слову

from des import *
import random
from datetime import datetime

print('Input message to encrypt:')
message = input().encode()

# key_string = b'hi i am key for des ede3'
key_string = ''
while True:
    print('Input key:')
    key_string = input().encode()
    if len(key_string) != 24:
        print('Key must be 24 bytes long')
    else:
        break

print('--------------- DES-EDE3 ---------------')
alg = triple_des(key_string, padmode=PAD_PKCS5)

start_time = datetime.now()
cipher = alg.encrypt(message)
encrypt_time = datetime.now() - start_time
print(f'Data: {message}')
print(f'Raw cipher: {cipher}')
start_time = datetime.now()
print(f'Decripted data: {alg.decrypt(cipher)}')
decrypt_time = datetime.now() - start_time
print(f'Encrypt time: {encrypt_time}')
print(f'Decrypt time: {decrypt_time}\n')

# replacing one random letter
random_index = random.randint(0, len(message)-1)
random_letter = message[random_index]
modified_letter = random.choice([chr(i) for i in range(97, 123)]).encode()
modified_message = message[:random_index] + modified_letter + message[random_index+1:]

print('Avalanche effect for DES-EDE3:')
print(f'Data: {message}')
print(f'Raw cipher: {cipher}')
print(f'Modified message: {modified_message}')
av_cipher = alg.encrypt(modified_message)
print(f'Modified message: {modified_message}')
print(f'Modified message cipher: {av_cipher}\n')

print('Weak keys for DES-EDE3:')
for key in WEAK_KEYS:
    cryptor = triple_des(key + key + key)
    cipher = cryptor.encrypt(message)
    cipher = cryptor.encrypt(cipher)
    print(des_cipher_to_string(cipher))
print()


print('Weak keys avalanche effect for DES-EDE3:')
for key in WEAK_KEYS:
    cryptor = triple_des(key + key + key, padmode=PAD_PKCS5)
    cipher1 = cryptor.encrypt(message)
    cipher2 = cryptor.encrypt(modified_message)
    print(cipher1)
    print(cipher2)
    print()
print()


print('Half weak keys for DES-EDE3:')
for key in HALF_WEAK_KEYS:
    cipher = triple_des(key + key + key).encrypt(message)
    decipher = triple_des(HALF_WEAK_PAIRS[key] + HALF_WEAK_PAIRS[key]).encrypt(cipher)
    print(des_cipher_to_string(decipher))
print()


print('Half weak keys avalanche effect for DES-EDE3:')
for key in HALF_WEAK_KEYS:
    cryptor = triple_des(key + key + key, padmode=PAD_PKCS5)
    cipher1 = cryptor.encrypt(message)
    cipher2 = cryptor.encrypt(modified_message)
    print(cipher1)
    print(cipher2)
    print()
print()