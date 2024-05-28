def sum_of_digits(n):
    if len(n) == 1:
        return int(n)
    return int(n[0]) + sum_of_digits(n[1:])

number = "234"
result = sum_of_digits(number)
print(f"Jumlah digit dari {number} adalah {result}.")