import os
import shutil
import random

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def change_dir():
    name = 'C:\Projects'
    os.chdir(os.path.join(name))
    return print(os.listdir(name))

def dir_copy():
    name = "dir_" + str(random.randint(1,9))
    os.mkdir(name)
    return print("Успешно создан каталог")



def dir_delete():
    os.rmdir(os.path.join('dir_'))
    return print("Удален каталог")



for m in range(1, 10):
    name = "dir_" + str(m)
    os.mkdir(name)




for k in range(1, 10):
    name = "dir_" + str(k)
    os.rmdir(name)



# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def listing_dir():
    return print(os.listdir())

print(listing_dir())









# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.





shutil.copyfile('HW_05_easy.py', 'HW_05_easy_copy.py')
