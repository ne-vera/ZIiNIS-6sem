# • выполнять зашифрование/расшифрование текстовых документов (объемом не менее 500 знаков)
# 8 вариант
# Английский 
# 1. Маршрутная перестановка (маршрут – зигзагом; параметры таблицы – по указанию преподавателя) 
# 2. Множественная перестановка, ключевые слова – собственные имя и фамилия
# формировать гистограммы частот появления символов для исходного и зашифрованного сообщений; 
# • оценивать время выполнения операций зашифрования/расшифрования
import matplotlib.pyplot as plt 
from zigzag_route_cipher import *
from multiple_permutation import *

keyword_column = 'prigodіch'
keyword_row = 'vera'

# with open('message.txt',  encoding='utf8') as file:
#     message = file.read().lower()

message = 'hello i am ciphrotext for ziinis lab'

message_probs = get_letters_amount(message)

zigzag_probs = zigzag_route_cipher(message, 4)
multiple_probs = multiple_permutation(keyword_column, keyword_row, message)

#строим гистограммы по словарям
fig, a = plt.subplots(2,2, figsize=(12, 10))
a[0][0].set_title('Исходное соо')
a[0][0].bar(list(message_probs.keys()), message_probs.values(), color='g')  
a[0][1].set_title('Зигзаг')
a[0][1].bar(list(zigzag_probs.keys()), zigzag_probs.values(), color='b')
a[1][0].set_title('Множественная перестановка')
a[1][0].bar(list(multiple_probs.keys()), multiple_probs.values(), color='r')  
a[1][1].set_title('Зигазаг - множественная')
a[1][1].bar(list(zigzag_probs.keys()), zigzag_probs.values(), color='r')
a[1][1].bar(list(multiple_probs.keys()), multiple_probs.values(), color='b')  
plt.show() 