# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

nummber = int(input("Введите число которое необходимо разложить на множители: "))
i = 2
my_list = []
simple_multipliers = nummber
while i <= nummber:
    if nummber % i == 0:
        my_list.append(i)
        nummber //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {simple_multipliers} приведены в списке: {my_list}")
