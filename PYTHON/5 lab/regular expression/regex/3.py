import re

pattern = r"\b[a-z]+_[a-z]+\b"
test_strings = ["hello_world", "test_value", "snake_case", "Hello_World"]

for s in test_strings:
    print(f"{s}: {bool(re.search(pattern, s))}")