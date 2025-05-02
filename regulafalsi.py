# Regula Falsi Method in Python

def f(x):
    # Define your function here
    return x**3 - x - 2

def regula_falsi(a, b, tol):
    if f(a) * f(b) >= 0:
        print("The function must have opposite signs at a and b.")
        return None

    c = a  # Initialize result
    while (b - a) >= tol:
        # Find the point that touches x-axis
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        # Check if the root is found
        if f(c) == 0.0:
            break

        # Decide the side to repeat the steps
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c

# Example usage
a = 1  # Lower bound
b = 2  # Upper bound
tolerance = 1e-6  # Tolerance level

root = regula_falsi(a, b, tolerance)
if root is not None:
    print(f"The root of the function is approximately: {root}")