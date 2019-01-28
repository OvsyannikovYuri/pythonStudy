# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# def my_round(number, ndigits):
#     pass
#
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# def lucky_ticket(ticket_number):
#     ticket = tuple(map(int, ticket_number))
#     n = len(ticket)
#     sum(ticket[:n / 2]) == sum(ticket[n / 2:])
#     return
def lucky_ticket(string):
    string = str(string)
    nums = [int(n) for n in string]
    if sum(nums[:3]) == sum(nums[-3:]):
        answer = "Lucky"
    else:
        answer = "not luck"

    return answer


print(lucky_ticket(123006))
print(lucky_ticket(123216))
print(lucky_ticket(436751))