
import re

pattern = r"\b[A-Z][a-z]+\b"
test_strings = ["Hello", "World", "Python", "hello", "PYTHON"]

for s in test_strings:
    print(f"{s}: {bool(re.search(pattern, s))}")