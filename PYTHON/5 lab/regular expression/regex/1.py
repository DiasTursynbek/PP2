import re
pattern = r"^(ab*$)"
strings=["abc","abccc","abbbbbb","abcdefg"]
for i in strings:
    print(f"{bool(re.match(pattern, i))}") #re.match строка басын тексереды