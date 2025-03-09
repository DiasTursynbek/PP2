import re

pattern = r"[a-z]+_[a-z]+"  # Тек кіші әріптерден тұратын сөздерді '_' арқылы бөлетін үлгі

test_strings = ["hello_world", "test_value", "snake_case", "Hello_World", "python_script", "Upper_Case"]

for s in test_strings:
    match = re.search(pattern, s)  # re.search() - жолдың кез келген жерінен іздейді
    print(f"{s}: {bool(match)}")

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