def count_letters(s):
    up=sum(1 for c in s if c.isupper())
    low = sum(1 for c in s if c.islower())
    return up,low
text=input("Input text: ")
print(count_letters(text))