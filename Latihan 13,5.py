def combination(n, k):
    if k == 0 or k == n:
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k)

n = 5
k = 2
result = combination(n, k)
print(f"C({n}, {k}) = {result}")