import numpy as np
alphabet = list('abcdefghijklmnopqrstuvwxyz')

def remove(keyword : str):
    keyword_list = []
    for character in keyword:
        # удаляем повторяющиеся символы в ключевом слове
        if character not in keyword_list:
            keyword_list.append(character)
        # удаляем символы ключевого слова из алфавита
        if character in alphabet:
            alphabet.remove(character)
    return keyword_list, alphabet

def insert(keyword: str):
    keyword_alphabet = remove(keyword)
    for character in keyword_alphabet[1]:
        keyword_alphabet[0].append(character)
    return keyword_alphabet[0]

def form_table(keyword : str):
    table = insert(keyword)
    additional_chars = ['?', ';', ',', '.']
    table = table + additional_chars
    table = np.reshape(table, (6,5))
    return table

def trithemius_encrypt(keyword : str, text : str):
    res = ''
    new_alphabet = form_table(keyword)
    for row in new_alphabet:
        print(row)
    for character in text:
        if character in new_alphabet:
            i, j = np.where(new_alphabet == character)
            if i == 5:
                encoded_character = ''.join(str(x) for x in new_alphabet[0, j])
                res += encoded_character
            else:
                encoded_character = ''.join(str(x) for x in new_alphabet[i+1, j])
                res += encoded_character
        else:
            res += ' '
    return res

def trithemius_decrypt(keyword: str, text: str):
    res = ''
    new_alphabet = form_table(keyword)
    for character in text:
        if character in new_alphabet:
            i, j = np.where(new_alphabet == character)
            if i == 0:
                encoded_character = ''.join(str(x) for x in new_alphabet[5, j])
                res += encoded_character
            else:
                encoded_character = ''.join(str(x) for x in new_alphabet[i-1, j])
                res += encoded_character
        else:
            res += ' '
    return res