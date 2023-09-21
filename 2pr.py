def f(x):
    return 4.5 * x**4 - 4 * x**3 + x**2 + x - 10

def separate_roots(start, end, step=0.1):
    segments = []
    a = start
    while a <= end:
        b = a + step
        if f(a) * f(b) < 0:
            segments.append((a, b))
        a = b
    return segments

def bisection_method(a, b, eps):
    while abs(a - b) > eps:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Відокремлення коренів
root_segments = separate_roots(-3, 3, 0.1)

# Знаходження коренів за допомогою методу половинного ділення
eps = 0.0001
for segment in root_segments:
    a, b = segment
    root_bisection = bisection_method(a, b, eps)
    print(f"Відрізок: [{a:.2f}, {b:.2f}]")
    print(f"Метод половинного ділення: Корінь: {root_bisection:.4f}")
    print()
