import re
pattern = r"^.*\.ab$"
test_strings = ["hello.ab", "test.ab", "word.ab.ab", "nothing"]

for s in test_strings:
    print(f"{s} -> {bool(re.match(pattern, s))}")