# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

my_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {my_list}")
my_list_2 = []
[my_list_2.append(i) for i in my_list if i not in my_list_2]
print(f"Список из неповторяющихся элементов: {my_list_2}")
