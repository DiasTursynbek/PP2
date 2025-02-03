def unique_list(lst):
    return list(dict.fromkeys(lst))

# Проверка
print(unique_list([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]