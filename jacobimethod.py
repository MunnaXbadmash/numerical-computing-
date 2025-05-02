import numpy as np

def jacobi_method(A, b, x0, tol, max_iterations):
    n = len(A)
    x = x0.copy()
    for iteration in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        # Check for convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Converged in {iteration + 1} iterations.")
            return x_new
        
        x = x_new
    
    print("Maximum iterations reached without convergence.")
    return x

# Example usage
if __name__ == "__main__":
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10, 10], dtype=float)
    x0 = np.zeros(len(b))
    tol = 1e-6
    max_iterations = 100

    solution = jacobi_method(A, b, x0, tol, max_iterations)
    print("Solution:", solution)