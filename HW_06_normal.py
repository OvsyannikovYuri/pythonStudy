# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.
class Person(object):
    def __init__(self,  name, surname,  school):
        self.name = name
        self.surname = surname
        # self.age = age
        self.school = school

    @property
    def _full_name(self):
        return self.surname + ' '+ self.name

    def school(self):
        school = 11
        return school


class Pupil(Person):
    # функция-конструктор - запускается автоматически при создании объекта (экземпляра класса)
    def __init__(self, name, surname, mother, father, class_room, school):
        Person.__init__(self,  name, surname,  school)
        self.mother = mother
        self.father = father
        self.class_room = class_room


    def pupil_class_room(self):
        return self.class_room


class Teacher(Person):
    def __init__(self, name, surname, theme, class_room, school):
        Person.__init__(self, name, surname, school)
        self.theme = theme
        self.class_room = class_room

    def teacher_full_name(self):
        return self.surname + ' '+ self.name

    def teacher_class_rooms(self):
        class_teacher = self.class_room
        return self.class_room

    def __repr__(self):
        return self.__str__()



pupil1 = Pupil("Николай", "Орехов", "Орехова Нина Николаевна", "Орехов Владимир Иванович", "5А", 11)
pupil2 = Pupil("Евгений", "МАслов", "Маслова Инна Николаевна", "Маслов Вадим Иванович", "5А", 11)
pupil3 = Pupil("Елизавета", "Ли", "Ли Елена Игоревна", "Ли Хлоп Пень", "6А", 11)
pupil4 = Pupil("Игорь", "Бутусов", "Бутусова Ирина Николаевна", "Бутусов Марат Андреевич", "6А", 11)
pupil5 = Pupil("Андрей", "Трус", "Трус Мария Николаевна", "Трус Владимир Иванович", "7Б", 11)

teacher1 = Teacher("Николай", "Дроздов", "биология", ["5А", "6А"], 11)
teacher2 = Teacher("Петр", "Капица", "физика", "7Б", 11)
teacher3 = Teacher("Пушкин", "Александр", "литература", ["5А", "6А", "7Б"], 11)










# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе