def fadd(a, b, c):
    def _fadd(x):
        return a * x * x + b * x + c
    return _fadd

f = fadd(-2, 4, 1)
print(f(10))
