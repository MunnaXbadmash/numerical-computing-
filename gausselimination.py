# Gauss Elimination Method in Python

def gauss_elimination(a, b):
    n = len(b)
    
    # Forward Elimination
    for i in range(n):
        # Make the diagonal element 1 and eliminate below rows
        for j in range(i+1, n):
            if a[i][i] == 0:
                raise ValueError("Division by zero detected!")
            ratio = a[j][i] / a[i][i]
            for k in range(n):
                a[j][k] -= ratio * a[i][k]
            b[j] -= ratio * b[i]
    
    # Back Substitution
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= a[i][j] * x[j]
        if a[i][i] == 0:
            raise ValueError("Division by zero detected!")
        x[i] /= a[i][i]
    
    return x

# Example usage
if __name__ == "__main__":
    # Coefficient matrix
    a = [
        [2, -1, 1],
        [3, 3, 9],
        [3, 3, 5]
    ]
    # Constant terms
    b = [2, -1, 4]
    
    try:
        solution = gauss_elimination(a, b)
        print("Solution:", solution)
    except ValueError as e:
        print("Error:", e)