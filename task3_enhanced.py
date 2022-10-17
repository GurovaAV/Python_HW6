# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def summa_nechet(input_list: list=[]):
    summa = []
    input_list = [x for idx,x in enumerate(input_list) if idx % 2]
    # здесь использовала функцию enumerate
    res = sum(input_list)
    return(res)
    
input_string = input('Введите элементы списка через пробел: ')
string_splitted = input_string.split(' ')            
input_list = list(map(int,string_splitted))
# тут у меня ранее уже была использована функция map для преобразования в int

print(f'Сумма нечетных элементов введенного списка равна: {summa_nechet(input_list)}')

