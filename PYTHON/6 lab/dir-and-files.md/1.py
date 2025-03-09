import os

path = "."

print("Directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

print("Files:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])



# Функция os.access(path, mode) проверяет доступ к файлу или папке.

# 1.	Импорт модуля os – нужен для работы с файловой системой.
# 2.	path = "." – точка . означает текущую директорию.

# os.path.join(path, d) – Получаем полный путь
# os.listdir(path) – получает все файлы и папки в path.
# os.path.isdir(os.path.join(path, d)) – проверяет, является ли элемент папкой.
# В итоге, в список попадают только папки.

# os.path.isfile(...) – проверяет, является ли элемент файлом.
# В итоге, в список попадают только файлы.