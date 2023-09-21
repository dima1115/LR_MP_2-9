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

def chord_method(a, b, eps):
    max_iterations = 1000  # Запобігаємо безкінечному циклу
    iteration = 0
    while abs(f(b) - f(a)) > eps and iteration < max_iterations:
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        iteration += 1
    return (a + b) / 2

# Відокремлення коренів
root_segments = separate_roots(-3, 3, 0.1)

# Знаходження коренів за допомогою методу половинного ділення і методу хорд
eps = 0.0001
for segment in root_segments:
    a, b = segment
    root_bisection = bisection_method(a, b, eps)
    root_chord = chord_method(a, b, eps)
    print(f"Відрізок: [{a:.2f}, {b:.2f}]")
    print(f"Метод половинного ділення: Корінь: {root_bisection:.4f}")
    print(f"Метод хорд: Корінь: {root_chord:.4f}")
    print()
