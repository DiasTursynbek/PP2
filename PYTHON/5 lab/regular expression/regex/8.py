import re
pattern =r'[A-Z][a-z]*'
text = "SplitThisString THgdo"
split_text = re.findall(pattern, text)
print(split_text)