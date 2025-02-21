import re


pattern = r"^(ab{2,3})"
strings = ["abc","abccc","abbbbbb","abcdefg"]
for i in strings:
    print(f"{bool(re.match(pattern, i))}")