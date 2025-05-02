def bisection_method(func, a, b, tol=1e-6, max_iter=100):
   
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at a and b.")

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if func(c) == 0:  # Found exact root
            return c
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return (a + b) / 2


# Example usage
if __name__ == "__main__":
    # Define the function
    def f(x):
        return x**3 - x - 2

    # Interval [a, b]
    a = 1
    b = 2

    # Find the root
    try:
        root = bisection_method(f, a, b)
        print(f"The root is approximately: {root}")
    except ValueError as e:
        print(e)