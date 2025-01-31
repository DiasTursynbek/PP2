from itertools import permutations

def print_permutations(s):
    for p in permutations(s):
        print(''.join(p))

# Проверка
print_permutations("abc")     #abc acb bac bca cab cba   
