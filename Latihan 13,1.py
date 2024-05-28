def is_prime(n, i=2):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

number = 29
if is_prime(number):
    print(f"{number} adalah bilangan prima.")
else:
    print(f"{number} bukan bilangan prima.")