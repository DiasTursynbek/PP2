import re


pattern = r"^(ab{2,3})"   #бір А болуы керек және 2,3 b болуы керек 
strings = ["abbbbbbc","abccc","abbbbbb","abcdefg"]
for i in strings:
    print(f"{bool(re.match(pattern, i))}")  #re.match строка басынан іздейді