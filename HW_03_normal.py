import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):
    fibonacci_number_list = []
    for i in range(n,m+1):
        fib_number = int(((((1 + math.sqrt(5)) / 2) ** i) - (((1 - math.sqrt(5)) / 2) ** i))/math.sqrt(5))
        fibonacci_number_list.append(fib_number)
    return fibonacci_number_list
# print(fibonacci(1,8))

#
# # Задача-2:
# # Напишите функцию, сортирующую принимаемый список по возрастанию.
# # Для сортировки используйте любой алгоритм (например пузырьковый).
# # Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
#
# def sort_to_max(origin_list):
#     i = 0
#     while i < len(origin_list):

nums = [1, 4, 5, 4, 4, 33, 2, -2]
def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        mini = min(origin_list[i:]) #find minimum element
        min_index = origin_list[i:].index(mini) #find index of minimum element
        origin_list[i + min_index] = origin_list[i] #replace element at min_index with first element
        origin_list[i] = mini
    return origin_list



# print(sort_to_max(nums))




# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
point_A = [0,0]
point_B = [0,1]
point_C = [3,1]
point_D = [3,0]
len_AB = math.sqrt((((point_B[0]-point_A[0]))**2)+(((point_B[1]-point_A[1]))**2))
len_CD = math.sqrt((((point_D[0]-point_C[0]))**2)+(((point_D[1]-point_C[1]))**2))
len_AD = math.sqrt((((point_D[0]-point_A[0]))**2)+(((point_D[1]-point_A[1]))**2))
len_BC = math.sqrt((((point_C[0]-point_B[0]))**2)+(((point_C[1]-point_B[1]))**2))

if len_AB == len_CD and len_BC == len_AD:
    print("Это параллелограмм")
else:
    print("НЕ параллелограмм")
