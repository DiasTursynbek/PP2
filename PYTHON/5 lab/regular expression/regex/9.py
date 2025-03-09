import re

def insert_spaces(s):
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", s)

print(insert_spaces("HelloWorldAlpdir"))


# .group() возвращает найденное слово. Если совпадений нет, вызовет ошибку.

# s.string – это свойство объекта, которое возвращает исходную строку, в которой производился поиск.
#x.span() → возвращает позицию (начало, конец) найденного совпадения.

#findall --> list кайтарады
# re.search --> match object қайтарады

# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

#|----------------------------------------------------------------------------------------------------------------------------|
#| name = "Dias"                                                                                                              |
#| age = 18                                                                                                                   |
#| print("Меня зовут {} и мне {} лет.".format(name, age)) --> "Меня зовут Dias и мне 18 лет."   -->  it is a old version code |
#|----------------------------------------------------------------------------------------------------------------------------|

# print(r"Привет\nмир!") --> Привет\nмир!

# print("Привет\nмир!")  --> Привет
#                            мир!

# f-строку (formatted string literals) 
# Символ $ означает конец строки.

# ^ --> начало строки
# r --> raw string
	# •	b{2,3} – от 2 до 3 b (то есть bb или bbb).
	# •	b* – 0 или более b (может быть "", b, bb, bbb, bbbb, …).
	# •	b+ – 1 или более b (может быть b, bb, bbb, bbbb, …).
	# •	b? – 0 или 1 b (может быть "" или b).