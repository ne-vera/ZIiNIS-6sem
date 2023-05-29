import random

def mod_inverse(num, mod):
    # Функция для нахождения обратного элемента по модулю
    return pow(num, -1, mod)

def is_quadratic_residue(num, mod):
    # Проверка, является ли число квадратным вычетом
    return pow(num, (mod-1)//2, mod) == 1

def calculate_y(x, a, b, p):
    # Функция для нахождения значений y на ЭК для заданного x
    x_cubed = (x**3 + a*x + b) % p

    if not is_quadratic_residue(x_cubed, p):
        return None  # x_cubed не является квадратным вычетом, точка не находится на кривой

    y = pow(x_cubed, (p+1)//4, p)  # Используем алгоритм квадратного корня Ферма
    return y

def get_points_in_range(x_min, x_max, a, b, p):
    points = []
    for x in range(x_min, x_max+1):
        y = calculate_y(x, a, b, p)
        if y is not None:
            points.append((x, y))
            points.append((x, p - y))  # Добавляем и отрицательное значение y
    return points

def is_on_curve(point, a, b, p):
    # Проверка находится ли точка на кривой
    x, y = point
    return (y * y - x * x * x - a * x - b) % p == 0

def point_addition(point1, point2, a, p):
    # Функция для сложения двух точек на ЭК

    if point1 is None:
        return point2
    if point2 is None:
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 == -y2 % p:
        return None  # Сложение точки с ее обратной дает бесконечно удаленную точку
    
    if x1 == x2 and y1 == y2:
        lam = (3 * x1**2 + a) * mod_inverse(2 * y1, p) % p
    else:
        lam = (y2 - y1) * mod_inverse(x2 - x1, p) % p

    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return x3, y3

def point_multiplication(point, number,  a, p):
    # Функция умножения точки на число
    result = None
    current = point
    while number > 0:
        if number & 1 == 1:
            result = point_addition(result, current, a, p)
        current = point_addition(current, current, a, p)
        number >>= 1
    return result

def point_negation(point, p):
    # Возращает обратную точку
    if point is None:
        return None
    
    x, y = point
    return x, -y % p

def sign(hash_int, G, q, d, a, p):
    r = 0
    s = 0

    while not r or not s:
        k = random.randint(1, q)
        x, y = point_multiplication(G, k, a, p)
        r = x % q
        s = ((hash_int + r * d) * mod_inverse(k, q)) % q
    print('k', k)
    print('x', x)
    return r, s

def verify(hash_int, signature, G, Q, q, a, p):
    r, s = signature
    w = mod_inverse(s, q)
    u1 = (hash_int * w) % q
    u2 = (w * r) % q

    Gu1 = point_multiplication(G, u1, a, p)
    Qu2 = point_multiplication(Q, u2, a, p)
    x, y = point_addition(Gu1, Qu2, a, p)

    return (r % q) == (x % q)