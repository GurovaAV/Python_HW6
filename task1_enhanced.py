# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8,
# 13, 21]

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib (n-2)
my_list = []
k = int(input("Введите нужное количество: "))
for i in range(1,k+1):
    my_list.append(fib(i))
# print(my_list)
my_list_rev = sorted(my_list, reverse = True)
my_list_rev2 = []
for idx, x in enumerate(my_list_rev):
    my_list_rev2.append(x * -1 if idx % 2 == 0 else x)
# хотела выше сделать через list comprehension, но выдавал ошибку с list assignment и я решила заморочиться с enumerate для использования индексов
# print(my_list_rev)
my_list_rev2.append(0)
final_list = my_list_rev2 + my_list
print(final_list)

    
