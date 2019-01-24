import random
import os

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
a = []
for x in range(10):
    a.append(random.randint(-10, 10))

func = lambda x: x**2
level_2 = [func(x) for  x in a]
print(level_2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

dict_fruits = {}
fruits = []
with open("fruits.txt", mode="r", encoding="UTF-8") as f:
    fruits = f.read().splitlines()

fruits_sort = list(filter(None, fruits))

number = []
for x in range(283):
    number.append(x)

dict_fruits = dict(zip(number, fruits_sort))

fruits_1 = []
for i in range(10):
    fruits_1.append(fruits_sort[random.randint(0, len(fruits_sort))])
fruits_2 = []
for i in range(20):
    fruits_2.append(fruits_sort[random.randint(0, len(fruits_sort))])
a = set(fruits_1)
b = set(fruits_2)
c = list(set(a) & set(b))
if len(c) > 0:
    print(c)
else:
    print("Пересечений нет")











# for i in fruits_copy:
#     if len(fruits_copy[i]) > 0:
#         fruits_sort.append(fruits_copy[i])


# fruit_1 = ['киви', 'лимон', 'яблоко', 'ананас', 'лайм', 'банан', 'виноград', 'слива']
# fruit_2 = ['киви', 'купуасу', 'померанец', 'терн', 'ананас', 'банан', 'свити', 'рамбутан', 'лонган']

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
list_res = []
list_int = []
for y in range(50):
    list_int.append(random.randint(-10, 40))
for z in list_int:
    if (list_int[z] > 0 and list_int[z]%3 == 0) and list_int[z]%4 != 0:
        list_res.append(list_int[z])
#

print(list_res)
