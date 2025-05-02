
def gauss_seidel(A, b, x0, tolerance, max_iterations):
    n = len(A)
    x = x0[:]
    
    for iteration in range(max_iterations):
        x_new = x[:]
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        # Check for convergence
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            print(f"Converged in {iteration + 1} iterations.")
            return x_new
        
        x = x_new
    
    print("Did not converge within the maximum number of iterations.")
    return x

# Example usage
A = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]
b = [4, 7, 3]
x0 = [0, 0, 0]  # Initial guess
tolerance = 1e-6
max_iterations = 100

solution = gauss_seidel(A, b, x0, tolerance, max_iterations)
print("Solution:", solution)