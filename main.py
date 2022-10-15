def fadd(a, b, c):
    def _fadd(x):
        return a * x * x + b * x + c
    return _fadd

# Комментарий обычный
if __name__ == "__main__":
    f = fadd(-2, 4, 1)
    print(f(10))