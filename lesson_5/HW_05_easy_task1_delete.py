import os

# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

for x in range(1,10):
    name = "dir_"+str(x)
    os.rmdir(name)