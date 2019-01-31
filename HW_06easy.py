# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

"""
Данный класс для треугольника на плоскости, то есть координаты заданы\n
парой чисел (координата Х, координата У)
"""
import math


class Triangle:

    def __init__(self, coordinat_A, coordinat_B, coordinat_C, ):
        self.coordinat_A = coordinat_A
        self.coordinat_B = coordinat_B
        self.coordinat_C = coordinat_C

    def square(self):
        square = float(0.5 * (math.fabs(((self.coordinat_B[0] - self.coordinat_A[0]) * \
                                         (self.coordinat_C[1] - self.coordinat_A[1])) - (
                                                    (self.coordinat_C[0] - self.coordinat_A[0]) * (
                                                        self.coordinat_B[1] - self.coordinat_A[1])))))

        return square

    def perimetr(self):
        perimetr = math.sqrt(((self.coordinat_B[0] - self.coordinat_A[0]) ** 2) +
                             ((self.coordinat_B[1] - self.coordinat_A[1]) ** 2) + (
                                         (self.coordinat_C[0] - self.coordinat_B[0]) ** 2) +
                             ((self.coordinat_C[1] - self.coordinat_B[1]) ** 2) + (
                                         self.coordinat_C[0] - self.coordinat_A[0]) ** 2) + (
                               (self.coordinat_C[1] - self.coordinat_A[1]) ** 2)
        return perimetr

    def high_triangle(self):
        square = float(0.5 * (math.fabs(((self.coordinat_B[0] - self.coordinat_A[0]) * \
                                         (self.coordinat_C[1] - self.coordinat_A[1])) - (
                                                (self.coordinat_C[0] - self.coordinat_A[0]) * (
                                                self.coordinat_B[1] - self.coordinat_A[1])))))
        high_triangle = (2 * Triangle.square(self)) / math.sqrt(((self.coordinat_C[0] - self.coordinat_A[0]) ** 2) +
                                                                ((self.coordinat_C[1] - self.coordinat_A[1]) ** 2))
        return high_triangle


triangle_test = Triangle([1, 1], [2, 4], [-2, -2])


print("площадь =", triangle_test.square())
print("площадь =", triangle_test.perimetr())
print(triangle_test.high_triangle())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь


class Trapezoid:

    def __init__(self, point_A, point_B, point_C, point_D):
        self.point_A = point_A
        self.point_B = point_B
        self.point_C = point_C
        self.point_D = point_D

    def side_len(self, begin_point, end_point):
        side_len = math.sqrt(((end_point[0] - begin_point[0]) ** 2) + ((end_point[1] - begin_point[1]) ** 2))
        return side_len

    def check_equal_side(self):
        AB = self.side_len(self.point_A, self.point_B)
        CD = self.side_len(self.point_C, self.point_D)
        return AB == CD

    def perimetr(self):
        perimert = self.side_len(self.point_A, self.point_B) + self.side_len(self.point_B,
                                                                             self.point_C) + self.side_len(self.point_C,
                                                                                                           self.point_D) + self.side_len(
            self.point_D, self.point_A)
        return perimert

    def square_trapezoid(self):
        # high_trapezoid = math.sqrt(((self.side_len(self.point_A, self.point_B))**2) - ((((self.side_len(self.point_D,self.point_A) -self.side_len(self.pointB,self.point_C)) )**2 + ((self.side_len(self.point_A, self.point_B))**2)
        #                            -((self.side_len(self.point_C, self.point_D))**2))/(2*(self.side_len(self.point_D,self.point_A) - self.side_len(self.point_B,self.point_C))))**2)
        square_trapezoid = float(((self.side_len(self.point_A, self.point_D) +self.side_len(self.point_B, self.point_C)) / 2) * \
                           (math.sqrt((self.side_len(self.point_C, self.point_D) ** 2) - ((((self.side_len(self.point_A, self.point_D)**2) - (2*self.side_len(self.point_A, self.point_D)*self.side_len(self.point_A, self.point_D))
                            - self.side_len(self.point_B, self.point_C)** 2)) / 4))))
        return square_trapezoid


trapezoid_test = Trapezoid([0, 0], [1, 1], [2, 1], [3 , 0])

print("равнобедренная", trapezoid_test.check_equal_side())
print("S= ", trapezoid_test.square_trapezoid())

print("P= ", trapezoid_test.perimetr())
