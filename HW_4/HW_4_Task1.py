# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = int(input('Введите точность числа Pi (количество знаков после запятой): '))
pi, sign, m = 3, 1, 2
while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
    pi = pi + sign*4/(m**3+3*m**2+2*m)
    sign = -1*sign
    m = m+2
print(f'Вычисленное число {pi=}')
pi = (round((pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2, d))
print(f'С точностью {d=}, число {pi=}; ')
