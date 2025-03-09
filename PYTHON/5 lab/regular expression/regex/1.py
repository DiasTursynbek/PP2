import re
pattern = r"^(ab*$)"    #0 немесе одан көп рет қайталануы мүмкін
strings=["abc","abccc","abbbbbb","abcdefg"]
for i in strings:
    print(f"{bool(re.match(pattern, i))}") #re.match строка басын тексереды


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

# Символ $ означает конец строки.
# print(r"Привет\nмир!") --> Привет\nмир!

# print("Привет\nмир!")  --> Привет
#                            мир!


































# import re
# pattern = r"^(ab*$)"    #0 немесе одан көп рет қайталануы мүмкін
# strings=["abc","abccc","abbbbbb","abcdefg"]
# for i in strings:
#     print(f"{bool(re.match(pattern, i))}") #re.match строка басын тексереды

