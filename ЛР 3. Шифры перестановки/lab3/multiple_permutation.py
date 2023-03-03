import numpy as np
from datetime import datetime

def encrypt(keyword_column : str, keyword_row : str, message: str) -> str:
    # формируем матрицу
    column_list = list(keyword_column)
    row_list = list(' ' + keyword_row)
    row_list = np.reshape(row_list, (len(keyword_row) + 1, 1))

    while len(message) / (len(keyword_column) *  len(keyword_row)) > 1:
        message = message[:-1]
    while len(message) % (len(keyword_column) *  len(keyword_row)) != 0:
        message += ' '

    matrix_message = list(message)
    matrix_message = np.reshape(matrix_message, (len(keyword_row), len(keyword_column)))

    matrix = np.vstack([column_list, matrix_message])
    matrix = np.hstack([row_list, matrix])

    print('Таблица с исходным сообщением')
    for row in matrix:
        print(row)

    # сортируем строки и столбцы матрицы
    matrix = matrix[np.argsort(matrix[:,0])]
    print('Таблица отстортированная по строкам')
    for row in matrix:
        print(row)

    matrix = np.transpose(matrix)
    matrix = matrix[np.argsort(matrix[:,0])]
    matrix = np.transpose(matrix)
    print('Итоговая отсортированная таблица')
    for row in matrix:
        print(row)   

    # записываем сообщения по столбцам
    matrix = matrix[1:, 1:]
    res = ''
    i, j = matrix.shape
    for column in range(j):
        for row in range(i):
            res += matrix[row][column]
    return res

def decrypt(keyword_column : str, keyword_row : str, message: str):   
    # формируем матрицу
    column_list = sorted(keyword_column)
    row_list = sorted(' ' + keyword_row)
    row_list = np.reshape(row_list, (len(keyword_row) + 1, 1))
    matrix_message = np.empty((len(keyword_row), len(keyword_column)), str)

    for i in range(len(keyword_column)):
        for j in range(len(keyword_row)):
            letter = message[0]
            message = message[1:]
            matrix_message[j][i] = letter

    matrix = np.vstack([column_list, matrix_message])
    matrix = np.hstack([row_list, matrix])    

    print('Таблица с зашифрованным сообщением')
    for row in matrix:
        print(row)

    # сортируем матрицу по ключам
    order_rows = []
    for character in sorted(' ' + keyword_row):
        order_rows.append(list(' ' + keyword_row).index(character))
    matrix = matrix[np.argsort(order_rows)]
    print('Таблица с восстановленными строками')
    for row in matrix:
        print(row)

    matrix = np.transpose(matrix)
    order_columns = []
    for character in sorted(' ' + keyword_column):
        order_columns.append(list(' ' + keyword_column).index(character))
    matrix = matrix[np.argsort(order_columns)]
    matrix = np.transpose(matrix)
    print('Таблица с восстановленными столбцами')
    for row in matrix:
        print(row)

    # записывам соощение по строкам
    matrix = matrix[1:, 1:]
    res = ''.join(matrix.flatten())
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

def multiple_permutation(keyword_column : str, keyword_row : str, message: str):
    start_time = datetime.now()
    encrypted = encrypt(keyword_column, keyword_row, message)
    encrypt_time = datetime.now() - start_time
    print('Зашифрованное сообщение', encrypted)
    start_time = datetime.now()
    decrypted = decrypt(keyword_column, keyword_row,encrypted)
    print('Расшифрованное сообщение:', decrypted)
    decrypt_time = datetime.now() - start_time
    print('\nВремя зашифрования:', encrypt_time)
    print('Время расшифрования:', decrypt_time)
    return get_letters_amount(encrypted)

