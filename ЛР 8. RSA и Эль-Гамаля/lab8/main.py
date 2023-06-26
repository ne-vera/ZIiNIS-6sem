import random
import matplotlib.pyplot as plt
import time
import numpy as np
from utils import *
from rsa import *
from elgamal import *

# -----------------------1-----------------------------
a = 5
prime_nums = get_prime(10**3, 10**5)
X = np.random.choice(prime_nums, 5, replace=False)
n = random.getrandbits(1024)
Y = []
start_time = time.time()
for x in X:
    y = a ** x % n
    calculation_time = time.time() - start_time
    Y.append(calculation_time)
    start_time = time.time()
calculation_time = time.time() - start_time
plt.plot(X, Y, '-ro')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Зависимость времени вычисления от параметров')
plt.show()

# -----------------------2-----------------------------
message = 'prigodich vera valeryevna'

# with open('text.txt',  encoding='utf8') as file:
#     message = file.read().lower()

print('\n--RSA--')
rsa(message)
print('\n--Эль-Гамаля--')
elgamal(message)