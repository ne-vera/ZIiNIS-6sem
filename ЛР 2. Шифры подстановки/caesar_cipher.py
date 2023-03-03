# y = (x + k) % N
# x, y – индекс (порядковый номер, начиная с 0) символа в используемом алфавите; k – ключ.
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
def insert(keyword, key):
    keyword_alphabet = remove(keyword)
    for index, character in enumerate(keyword_alphabet[1]):
        keyword_alphabet[0].insert((key + index)%26, character)
    return keyword_alphabet[0]

def caesar_encrypt(keyword: str, key: int, text: str):
    res = ''
    alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
    keyword = remove(keyword.lower())[0]
    print('\nНормализованное ключевое слово: ',  ''.join(keyword))
    new_alphabet = insert(keyword, key)
    print('\nИсходный алфавит:', alphabet_list)
    print('\nАлфавит с ключем:', new_alphabet)
    for character in text:
            if character in alphabet_list:
                res += new_alphabet[alphabet_list.index(character)]
            else:
                res += character
    return res

def caesar_decrypt(keyword: str, key: int, text: str):
    res = ''
    alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
    new_alphabet = insert(keyword, key)
    for character in text:
            if character in new_alphabet:
                res += alphabet_list[new_alphabet.index(character)]
            else:
                res += character
    return res