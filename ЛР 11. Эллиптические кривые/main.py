import elliptic_curves
from alphabet_points import *
import hashlib

# 8 вариант
# В основе задания Е751(–1, 1).

print('------Задание 1------')
print('1.1.	Найти точки ЭК для значений х: xmin  = 481 и xmax = 515.')

p = 751
a = -1
b = 1

x_min = 481
x_max = 515

points = elliptic_curves.get_points_in_range(x_min, x_max, a, b, p)

print("Точки на ЭК:")
for point in points:
    print(point)

print('\n1.2.	Разработать приложение для выполнения операций над точками кривой:')
k = 12
l = 5
P = (48, 702)
Q = (69, 241)
R = (98, 338)
kP = elliptic_curves.point_multiplication(P, k, a, p)
print('а) kР =', kP)
PQ = elliptic_curves.point_addition(P, Q, a, p)
print('б) Р + Q =', PQ)
lQ = elliptic_curves.point_multiplication(Q, l, a, p)
neg_R = elliptic_curves.point_negation(R, p)
print('в) kР + lQ – R =', elliptic_curves.point_addition(elliptic_curves.point_addition(kP, lQ, a, p), neg_R, a, p))
neg_Q = elliptic_curves.point_negation(Q, p)
print('г) Р – Q + R =', elliptic_curves.point_addition(elliptic_curves.point_addition(P, neg_Q, a, p), R, a, p))

print('\n------Задание 2------')
print('2.1. Зашифрование/расшифрование на основе ЭК')
G = (0, 1)
d = 34
print('Генерирующая точка G =', G)
print('Тайный ключ d =', d)
Q = elliptic_curves.point_multiplication(G, d, a, p)
print('Открытый ключ Q =', Q)
kQ = elliptic_curves.point_multiplication(Q, k, a, p)
print('kQ = ', kQ)
message = 'ВЕРА'
C_1 = elliptic_curves.point_multiplication(G, k, a, p)
cipher = []
for m in message:
    print(m, ALPHABET_POINTS[m])
    C_2 = elliptic_curves.point_addition(ALPHABET_POINTS[m], kQ, a, p)
    cipher.append((C_1, C_2))
print('Шифр:')
for tup in cipher:
    print('C1 :', tup[0], 'C2:', tup[1])

decipher = ''
print('\nРасшифрование:')
for tup in cipher:
    dC_1 = elliptic_curves.point_multiplication(tup[0], d, a, p)
    neg_dC_1 = elliptic_curves.point_negation(dC_1, p)
    P = elliptic_curves.point_addition(tup[1], neg_dC_1, a, p)
    print(P)
    decipher += [k for k, v in ALPHABET_POINTS.items() if v == P][0]
print('Расшифрованное сообщение:', decipher)

print('\n------Задание 3------')
print('3.1. Генерация/верификация ЭЦП на основе алгоритма ЕСDSA')
G = (416, 55)
print('Генерирующая точка G =', G)
q = 13
print('Порядок q =', q)
d = 9
print('Тайный ключ d =', d)
Q = elliptic_curves.point_multiplication(G, d, a, p)
print('Открытый ключ Q =', Q)

message_hash = hashlib.sha512(message.encode()).digest()
hash_int = int.from_bytes(message_hash, 'big')
z = hash_int >> (hash_int.bit_length() - q.bit_length())
signature = elliptic_curves.sign(z, G, q, a, a, p)
print(signature)
print('Подпись верифицирована:', elliptic_curves.verify(z, signature, G, Q, q, a, p))