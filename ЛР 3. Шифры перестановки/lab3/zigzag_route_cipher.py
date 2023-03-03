import numpy as np
from datetime import datetime

def form_matrix(message : str, route_step : int) -> np.ndarray:
    message_len = len(message)
    if message_len % route_step != 0:
        message += ' ' * (route_step - message_len % route_step)
    matrix = np.array(list(message))
    matrix = matrix.reshape(route_step, -1)
    return matrix

def encrypt(message : str, route_step : int) -> str:
    matrix = form_matrix(message, route_step)
    print('Таблица:')
    for row in matrix:
        print(row)
    res = ''
    i, j = matrix.shape
    for column in range(j):
        if column % 2 == 0:
            for row in reversed(range(i)):
                res += matrix[row, column]
        else:
            for row in range(i):
                res += matrix[row, column]
    return(res)

def decrypt(message: str, route_step : int) -> str:
    message_len = len(message)
    if message_len % route_step != 0:
        message += ' ' * (route_step - message_len % route_step)
    matrix = np.empty((route_step, message_len // route_step), dtype=str)
    i, j = matrix.shape
    for column in range(j):
        if column % 2 == 0:
            for row in reversed(range(i)):
                letter = message[0]
                message = message[1:]
                matrix[row, column] = letter
        else:
            for row in (range(i)):
                letter = message[0]
                message = message[1:]
                matrix[row, column] = letter
    print('Таблица:')
    for row in matrix:
        print(row)
    res = ''.join(matrix.ravel())
    return res

# словарь {символ:количество потворений этого символа} отсортированный по ключу
def get_letters_amount(seq):
    letters_dictionary = {}
    for i in seq:
        if i.isalpha():
            if i not in letters_dictionary:
                letters_dictionary[i] = 0
            letters_dictionary[i] += 1
    return dict(sorted(letters_dictionary.items()))

def zigzag_route_cipher(message: str, route_step : int):
    start_time = datetime.now()
    encrypted = encrypt(message, route_step)
    encrypt_time = datetime.now() - start_time
    print('Зашифрованное сообщение', encrypted)
    start_time = datetime.now()
    decrypted = decrypt(encrypted, route_step)
    decrypt_time = datetime.now() - start_time
    print('Расшифрованное сообщение:', decrypted)
    print('Время зашифрования:', encrypt_time)
    print('Время расшифрования:', decrypt_time)
    return get_letters_amount(encrypted)