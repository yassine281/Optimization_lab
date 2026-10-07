from typing import Callable, Tuple, List


def dsk_method(f: Callable[[float], float], x0: float, h: float) -> Tuple[float, float]:
    """
    Алгоритм Дэвиса-Свенна-Кэмпи для поиска отрезка локализации минимума.
    """
    f0 = f(x0)
    f_right = f(x0 + h)

    if f0 > f_right:
        a = x0
        x1 = x0 + h
        f1 = f_right
        k = 2
        step = h
    else:
        f_left = f(x0 - h)
        if f_left >= f0:
            return x0 - h, x0 + h
        else:
            b = x0
            x1 = x0 - h
            f1 = f_left
            k = 2
            step = -h

    xk_prev = x0
    fk_prev = f0
    xk = x1
    fk = f1

    while True:
        xk_next = xk + (2 ** (k - 1)) * step
        fk_next = f(xk_next)

        if fk_prev <= fk:
            if step > 0:
                return xk_prev, xk_next
            else:
                return xk_next, xk_prev
        else:
            if step > 0:
                a = xk_prev
            else:
                b = xk_prev

        xk_prev = xk
        fk_prev = fk
        xk = xk_next
        fk = fk_next
        k += 1


def dichotomy(f: Callable[[float], float], a: float, b: float, eps: float) -> Tuple[float, float, int, int, List]:
    """
    Метод дихотомии.
    """
    delta = eps / 10.0
    history = []
    iters = 0
    fevals = 0

    while (b - a) / 2.0 >= eps:
        x1 = (a + b) / 2.0 - delta
        x2 = (a + b) / 2.0 + delta
        f1, f2 = f(x1), f(x2)
        fevals += 2

        history.append((iters, a, b, (a + b) / 2, f((a + b) / 2)))

        if f1 <= f2:
            b = x2
        else:
            a = x1
        iters += 1

    x_star = (a + b) / 2.0
    history.append((iters, a, b, x_star, f(x_star)))
    return x_star, f(x_star), iters, fevals, history


def fibonacci_search(f: Callable[[float], float], a: float, b: float, eps: float) -> Tuple[
    float, float, int, int, List]:
    """
    Метод Фибоначчи.
    """
    fib = [1, 1]
    while fib[-1] < (b - a) / eps:
        fib.append(fib[-1] + fib[-2])
    N = len(fib) - 1

    x1 = a + (fib[N - 2] / fib[N]) * (b - a)
    x2 = a + (fib[N - 1] / fib[N]) * (b - a)
    f1, f2 = f(x1), f(x2)
    fevals = 2
    history = []

    for k in range(1, N - 1):
        history.append((k - 1, a, b, (a + b) / 2, f((a + b) / 2)))
        if f1 <= f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (fib[N - k - 2] / fib[N - k]) * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (fib[N - k - 1] / fib[N - k]) * (b - a)
            f2 = f(x2)
        fevals += 1

    delta = eps / 10.0
    x2 = x1 + delta
    f2 = f(x2)
    fevals += 1
    if f1 <= f2:
        b = x2
    else:
        a = x1

    x_star = (a + b) / 2.0
    history.append((N - 2, a, b, x_star, f(x_star)))
    return x_star, f(x_star), N - 2, fevals, history