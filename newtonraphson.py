
def newton_raphson(func, derivative, initial_guess, tolerance=1e-7, max_iterations=100):
    
    x = initial_guess
    for i in range(max_iterations):
        f_x = func(x)
        f_prime_x = derivative(x)
        
        if abs(f_prime_x) < 1e-12:  # Avoid division by zero
            print("Derivative is too small. Stopping iteration.")
            return None
        
        next_x = x - f_x / f_prime_x
        
        if abs(next_x - x) < tolerance:
            print(f"Root found after {i+1} iterations: {next_x}")
            return next_x
        
        x = next_x
    
    print("Maximum iterations reached. Root not found.")
    return None

# Example usage
if __name__ == "__main__":
    # Define the function and its derivative
    def func(x):
        return x**3 - x - 2

    def derivative(x):
        return 3*x**2 - 1

    # Initial guess
    initial_guess = 1.5

    # Find the root
    root = newton_raphson(func, derivative, initial_guess)
    if root is not None:
        print(f"Approximate root: {root}")