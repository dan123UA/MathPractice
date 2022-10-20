from math import sin


def core(f, a, b, n):
    print("\n Поточне число розбиття: ", n)
    h = (b-a)/float(n)
    print("Поточний крок:", h)
    total = sum([f((a + (k*h))) for k in range(0, n)])
    result = h * total
    print("Поточний результат: ", result)
    return result


def f(x):
    return (2.71828**-2*x + 1) * sin(x+3)

print("Використовуєм формулу лівих прямокутників")
"""2.71828 == value of Euler(e)"""
print("Інтегрована функція: f(x) = (2.71828^-2*x + 1) * sin(x+3)")
print("Точність: 0.001")

n = 2
a1 = core(f, 1, 10, n)
n *= 2
a2 = core(f, 1, 10, n)

"""Абсолютна величина числа (ABS) – це число без знака"""
while abs(a1 - a2) > 0.001:
    n *= 2
    a1 = core(f, 1, 10, n)
    n *= 2
    a2 = core(f, 1, 10, n)

print("\n Відповідь:", a2, "\n Кількість розбиття:", n)