﻿
__author__ = 'Овсянников Юрий Леонидович'
# coding : utf-8
import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number = int (input("введите произвольное целое число"))
number = str(number)
n = len(number)
i = 0
max = 0
while i < n:
    number_temp = int (number[i])
    if number_temp > max:
        max = number_temp
    else:
        pass
    i += 1
print(max)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int (input("введите первую переменную"))
b = int (input("введите вторую переменную"))

a = a + b
b = b - a
b = -b
a = a - b
print(a)
print(b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

coifficient_A = float (input("введите коэффициент А"))
coifficient_B = float (input("введите коэффициент B"))
coifficient_C = float (input("введите коэффициент C"))

Diskreminant = coifficient_B**2 - (4*coifficient_A*coifficient_C)
if Diskreminant > 0:
    x1 = ((coifficient_B* -1) + math.sqrt(Diskreminant)) / (2*coifficient_A)
    x2 = ((coifficient_B* -1) - math.sqrt(Diskreminant)) / (2*coifficient_A)
    print("первый корень равен", x1)
    print("второй корень равен", x2)
elif Diskreminant == 0:
    x3 = (coifficient_B * -1)/ (2*coifficient_A)
    print("единственный корень равен", x3)
else:
    print("корней нет")
