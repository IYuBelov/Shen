# -*- coding: utf-8 -*-


# Задачи без массивов


# 1.1.1 Даны две целые переменные a, b. Составьте фрагмент программы, после исполнения которого значения переменных поменялись
# бы местами (новое значение a равно старому значению b и наоборот).
def swap(a, b):
    t = a
    a = b
    b = t
    return a, b

# Решите предыдущую задачу, не используя дополнительных
# переменных (и предполагая, что значениями целых переменных могут
# быть произвольные целые числа)
def swap_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# 1.1.3. Дано целое число а и натуральное (целое неотрицательное)
# число n. Вычислите a ^ n
# Другими словами, необходимо составить программу, при исполнении которой значения переменных а и n не меняются, а значение некоторой другой переменной (например, b) становится
# равным a ^ n. (При этом разрешается использовать и другие переменные.)
def pow(a, n):
    b = 1
    while n > 0:
        b *= a
        n -= 1
    return b

# 1.1.4. Решите предыдущую задачу, если требуется, чтобы число
# действий (выполняемых операторов присваивания) было порядка log n
# (то есть не превосходило бы 𝐶 log n для некоторой константы 𝐶; log n |
# это степень, в которую нужно возвести 2, чтобы получить n).
def super_pow(a, n):
    b = 1
    c = a
    k = n
    while k > 0:
        if k % 2 == 0:
            k = k // 2
            c = c * c
        else:
            k -= 1
            b *= c
    return b

# 1.1.5. Даны натуральные числа а, b. Вычислите произведение a · b,
# используя в программе лишь операции +, -, =, <>.
def multiply(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1

    return result

# 1.1.6. Даны натуральные числа а и b. Вычислите их сумму а + b.
# Используйте операторы присваивания лишь вида
#      ⟨переменная1⟩ := ⟨переменная2⟩,
#      ⟨переменная⟩ := ⟨число⟩,
#      ⟨переменная1⟩ := ⟨переменная2⟩ + 1.
# Решение.
# ...
# {инвариант: c = a + k}

def specialMultiply(a, b):
    k = 0
    result = 0
    while k != b:
        k += 1
        result += a
    return result

# 1.1.7. Дано натуральное (целое неотрицательное) число а и целое
# положительное число d. Вычислите частное q и остаток r при делении а
# на d, не используя операций div и mod.
def div(a, d):
    assert d > 0, "d must by greater then 0"
    assert a >= 0, "d must by greater or equal by 0"

    q = r = 0
    while a >= d:
        q += 1
        a = r = a - d

    return q, r


# 1.1.8. Дано натуральное n, вычислите n! (0! = 1, n! = n · (n − 1)!).
def factorial(n):
    assert n >= 0, "factorial must by >= 0"
    result = 1
    for k in range(1, n + 1):
        result *= k
    return result

# 1.1.9. Последовательность Фибоначчи определяется так: a0 = 0,
# a1 = 1, ak = ak-1 + ak-2 при k > 2. Дано n, вычислите an.
def fib(n):
    assert n >= 0, "n must be greater or equal 0"

    if n == 0:
        return 0

    if n == 1:
        return 1

    prev = 0
    result = 1
    for k in range(2, n + 1):
        prevPrev = prev
        prev = result
        result = prev + prevPrev

    return result


# 1.1.10. Та же задача, если требуется, чтобы число операций было
# пропорционально log n. (Переменные должны быть целочисленными.)
# [Указание. Пара соседних чисел Фибоначчи получается из предыдущей умножением на матрицу
#
# | так что задача сводится к возведению матрицы в степень n. Это
# можно сделать за 𝐶 log n действий тем же способом, что и для чисел.]

class MatrixFibonacci:
    Q = [[1, 1],
         [1, 0]]

    def __init__(self):
        self.__memo = {}

    def __multiply_matrices(self, M1, M2):
        """Умножение матриц
        (ожидаются матрицы в виде списка список размером 2x2)."""

        a11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
        a12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
        a21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
        a22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
        r = [[a11, a12], [a21, a22]]
        return r

    def __get_matrix_power(self, M, p):
        """Возведение матрицы в степень (ожидается p равная степени двойки)."""

        if p == 1:
            return M
        if p in self.__memo:
            return self.__memo[p]
        K = self.__get_matrix_power(M, int(p/2))
        R = self.__multiply_matrices(K, K)
        self.__memo[p] = R
        return R

    def get_number(self, n):
        """Получение n-го числа Фибоначчи
        (в качестве n ожидается неотрицательное целое число)."""
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Разложение переданной степени на степени, равные степени двойки,
        # т.е. 62 = 2^5 + 2^4 + 2^3 + 2^2 + 2^0 = 32 + 16 + 8 + 4 + 1.
        powers = [int(pow(2, b))
                  for (b, d) in enumerate(reversed(bin(n-1)[2:])) if d == '1']
        # Тоже самое, но менее pythonic: http://pastebin.com/h8cKDkHX

        matrices = [self.__get_matrix_power(MatrixFibonacci.Q, p)
                    for p in powers]
        while len(matrices) > 1:
            M1 = matrices.pop()
            M2 = matrices.pop()
            R = self.__multiply_matrices(M1, M2)
            matrices.append(R)
        return matrices[0][0][0]


def fibMatrix(n):
    assert n >= 0, "n must be greater or equal 0"
    return MatrixFibonacci().get_number(n)


# 1.1.11. Дано натуральное n, вычислите 1/ 1! + 1/2! + 1/3!
def calculateRange(n):
    assert n >= 0, "n must be greater or equal 0"
    result = 0
    for i in range(n + 1):
        result += 1.0 / factorial(i)
    return result


# 1.1.12. То же, если требуется, чтобы количество операций (выполненных команд присваивания
# ) было бы порядка n (не более 𝐶n для некоторой константы 𝐶).
def fastCalculateRange(n):
    assert n >= 0, "n must be greater or equal 0"
    result = 1
    prevFactorial = 1
    for i in range(1, n + 1):
        factorial = prevFactorial * i
        result += 1.0/factorial
        prevFactorial = factorial

    return result

# 1.1.13. Даны два натуральных числа a и b, не равные нулю одновременно. Вычислите НОД(a,b)
# наибольший общий делитель а и b
def nod1(a, b):
    assert not (a == 0 and b == 0), "a and b mustn't by zero!"
    if a == 0 or b == 0:
        return 0

    k = a if a < b else b
    result = 1
    while k > 0:
        if b % k == 0 and a % k == 0:
            result = k
            break
        k -= 1
    return result

# 1.1.14. Напишите модифицированный вариант алгоритма Евклида,
# использующий соотношения НОД(a,b) = НОД(a mod b, b) при a > b,
# НОД(a,b) = НОД(a, b mod a) при b > a.

def nod2(a, b):
    """Алгоритм Евклида gcd"""
    while b:
        a, b = b, a % b
    return abs(a)


# 1.1.15. Даны натуральные a и b, не равные 0 одновременно. Найдите
# d = НОД(a,b) и такие целые x и y, что d = a · x + b · y.
