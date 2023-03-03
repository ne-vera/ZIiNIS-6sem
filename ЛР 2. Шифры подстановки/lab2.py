# выполнять зашифрование/расшифрование текстовых документов (объемом не менее 5 тысяч знаков), 
# созданных на основе алфавита языка в соответствии с нижеследующей таблицей вариантов задания
# при этом следует использовать шифры подстановки из третьего столбца данной таблицы
#8 вариант
# Английский
# 1. Шифр Цезаря с ключевым словом, ключевое слово – собственная фамилия, а = 24 
# 2. Таблица Трисемуса, ключевое слово – собственное имя
# сформировать гистограммы частот появления символов для исходного и зашифрованного сообщений;
# оценить время выполнения операций зашифрования/расшифрования
from caesar_cipher import *
from trithemius_cipher import *
import matplotlib.pyplot as plt 
from datetime import datetime
a = 24
caesar_keyword = 'prigodich'
trithemius_keyword = 'vera'

with open('text.txt',  encoding='utf8') as file:
    text = file.read().lower()

print('Шифр Цезаря')

start_time = datetime.now()
caesar_encrypted = caesar_encrypt(caesar_keyword, a, text)
encrypt_time = datetime.now() - start_time
print('\n\nЗашированное сообщение:\n\n')
print(caesar_encrypted)
print('\n\nРасшированное сообщение:\n\n')
start_time = datetime.now()
print(caesar_decrypt(caesar_keyword, a, caesar_encrypted))
decrypt_time = datetime.now() - start_time
print('\nВремя зашифрования:', encrypt_time)
print('Время расшифрования:', decrypt_time)


print('\n\n\nШифр Трисемуса')

start_time = datetime.now()
trithemius_encrypted = trithemius_encrypt(trithemius_keyword, text)
encrypt_time = datetime.now() - start_time
print('\n\nЗашированное сообщение:\n\n')
print(trithemius_encrypted)
print('\n\nРасшированное сообщение:\n\n')
start_time = datetime.now()
print(trithemius_decrypt(trithemius_keyword, trithemius_encrypted))
decrypt_time = datetime.now() - start_time
print('\nВремя зашифрования:', encrypt_time)
print('Время расшифрования:', decrypt_time)

# словарь {символ:количество потворений этого символа} отсортированный по ключу
def get_letters_amount(seq):
    letters_dictionary = {}
    for i in seq:
        if i.isalpha():
            if i not in letters_dictionary:
                letters_dictionary[i] = 0
            letters_dictionary[i] += 1
    return dict(sorted(letters_dictionary.items()))

text_probs = get_letters_amount(text)
encryptes_probs_caesar = get_letters_amount(caesar_encrypted)
encryptes_probs_trithemius = get_letters_amount(trithemius_encrypted)

#строим гистограммы по словарям
fig, a = plt.subplots(2,2, figsize=(12, 10))
a[0][0].set_title('Исходное слово')
a[0][0].bar(list(text_probs.keys()), text_probs.values(), color='g')  
a[0][1].set_title('Шифр Цезаря')
a[0][1].bar(list(encryptes_probs_caesar.keys()), encryptes_probs_caesar.values(), color='b')
a[1][0].set_title('Шифр Трисемуса')
a[1][0].bar(list(encryptes_probs_trithemius.keys()), encryptes_probs_trithemius.values(), color='r')  
a[1][1].set_title('Трисемуса и Цезаря')
a[1][1].bar(list(encryptes_probs_caesar.keys()), encryptes_probs_caesar.values(), color='r')
a[1][1].bar(list(encryptes_probs_trithemius.keys()), encryptes_probs_trithemius.values(), color='b')  
plt.show() 