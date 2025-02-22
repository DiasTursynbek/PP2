
import re

pattern = r"[A-Z][a-z]+"
test_strings = ["Hello", "World", "Python", "hello", "PYTHON"]  #бір үлкен әріп потом кіші әріп жүруі керек

for s in test_strings:
    print(f"{s}: {bool(re.search(pattern, s))}")