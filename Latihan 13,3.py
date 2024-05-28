def sum_odd_series(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        n -= 1
    return n + sum_odd_series(n - 2)

n = 9
result = sum_odd_series(n)
print(f"Jumlah deret bilangan ganjil hingga {n} adalah {result}.")