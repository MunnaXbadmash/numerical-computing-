#include <iostream>
#include <iostream>
#include <cmath>    
double f(double x) {
    return x * x - 4;
}

double secantMethod(double x0, double x1, double tolerance, int maxIterations) {
    int iteration = 0;
    double x2;
    while (iteration < maxIterations) {
       
        double f0 = f(x0);
        double f1 = f(x1);

        if (fabs(f1 - f0) < tolerance) {
            std::cout << "Error: Division by zero in the secant method.\n";
            return NAN;
        }
       
        x2 = x1 - (f1 * (x1 - x0)) / (f1 - f0);
        if (fabs(x2 - x1) < tolerance) {
            std::cout << "Converged after " << iteration + 1 << " iterations.\n";
            return x2;
        }
        x0 = x1;
        x1 = x2;

        iteration++;
    }

    std::cout << "Max iterations reached without convergence.\n";
    return x2;
}

int main() {
    double x0, x1, tolerance;
    int maxIterations;
    std::cout << "Enter initial guesses x0 and x1: ";
    std::cin >> x0 >> x1;
    std::cout << "Enter tolerance: ";
    std::cin >> tolerance;
    std::cout << "Enter maximum number of iterations: ";
    std::cin >> maxIterations;

    double root = secantMethod(x0, x1, tolerance, maxIterations);

    if (!std::isnan(root)) {
        std::cout << "Root: " << root << std::endl;
    }

    return 0;
}

