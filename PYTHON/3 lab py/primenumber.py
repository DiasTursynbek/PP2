def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, input("Введите числа через пробел: ").split()))
prime_numbers = list(filter(lambda x: prime(x), numbers))
print(prime_numbers)