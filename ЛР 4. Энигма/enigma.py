# 8 вариант
# L - V
# M - VI
# R - VII
# Re - C Dunn
# LiMiRi - 1-2-2

import matplotlib.pyplot as plt 

message = 'PRIGODICHVERAVALERYEVNA'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
left_rotor = 'VZBRGITYUPSDNHLXAWMJQOFECK'
middle_rotor = 'JPGVOUMFYQBENHZRDKASXLICTW'
right_rotor = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
reflector = {
    'A': 'R',
    'B': 'D',
    'C': 'O',
    'D': 'B',
    'E': 'J',
    'F': 'N',
    'G': 'T',
    'H': 'K',
    'I': 'V',
    'J': 'E',
    'K': 'H',
    'L': 'M',
    'M': 'L',
    'N': 'F',
    'O': 'C',
    'P': 'W',
    'Q': 'Z',
    'R': 'A',
    'S': 'X',
    'T': 'G',
    'U': 'Y',
    'V': 'I',
    'W': 'P',
    'X': 'S',
    'Y': 'U',
    'Z': 'Q'
}

print('Сообщение:\t', message)
print('Алфавит:\t', alphabet)
print('Правый ротор:\t', right_rotor)
print('Средний ротор:\t', middle_rotor)
print('Левый ротор:\t', left_rotor)
# print('Рефлектор:\t', reflector)

def enigma(message : str, left_rotor : str, middle_rotor : str, right_rotor : str) -> str:
    res = ''
    for character in message:
        letter = right_rotor[alphabet.index(character)]
        letter = middle_rotor[alphabet.index(letter)]
        letter = left_rotor[alphabet.index(letter)]
        letter = reflector[letter]
        letter = alphabet[left_rotor.index(letter)]
        letter = alphabet[middle_rotor.index(letter)]
        letter = alphabet[right_rotor.index(letter)]
        res += letter
        left_rotor = left_rotor[1:] + left_rotor[:1]
        middle_rotor = middle_rotor[2:] + middle_rotor[:2]
        right_rotor = right_rotor[2:] + right_rotor[:2]
    return res

encrypted = enigma(message, left_rotor, middle_rotor, right_rotor)
print('Зашифрованное сообщение:', encrypted)
print('Расшифрованное сообщение:', enigma(encrypted, left_rotor, middle_rotor, right_rotor))

def get_letters_amount(seq):
    letters_dictionary = {}
    for i in seq:
        if i.isalpha():
            if i not in letters_dictionary:
                letters_dictionary[i] = 0
            letters_dictionary[i] += 1
    return dict(sorted(letters_dictionary.items()))

message_probs = get_letters_amount(message)
encrypted_probs = get_letters_amount(encrypted)

fig, a = plt.subplots(2,1, figsize=(12, 10))
a[0].set_title('Исходное сообщение')
a[0].bar(list(message_probs.keys()), message_probs.values(), color='g')
a[1].set_title('Зашифрованное сообщение') 
a[1].bar(list(encrypted_probs.keys()), encrypted_probs.values(), color='b') 
plt.show() 