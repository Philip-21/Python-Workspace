def f(x, coefficients):
    """
    Evaluates the value of the polynomial equation at a given x.
    """
    a, b, c, n = coefficients
    return a * x ** n + b * x + c

def f_prime(x, coefficients):
    """
    Evaluates the value of the derivative of the polynomial equation at a given x.
    """
    a, b, _, n = coefficients
    return n * a * x ** (n - 1) + b

def bisection(coefficients, r, s, epsilon=1e-6, max_iterations=100):
    """
    Implements the bisection method to solve the transcendental equation.
    """
    a, b, _, _ = coefficients
    fr = f(r, coefficients)

    if fr == 0:
        return r

    fs = f(s, coefficients)

    if fs == 0:
        return s

    if fr * fs > 0:
        raise ValueError("The initial solutions do not bracket the root.")

    for _ in range(max_iterations):
        x = (r + s) / 2
        fx = f(x, coefficients)

        if fx == 0 or abs(s - r) < epsilon:
            return x

        if fr * fx < 0:
            s = x
        else:
            r = x

    raise ValueError("Bisection method failed to converge.")

def newton_raphson(coefficients, r, epsilon=1e-6, max_iterations=100):
    """
    Implements the Newton-Raphson method to solve the transcendental equation.
    """
    for _ in range(max_iterations):
        fr = f(r, coefficients)
        f_prime_r = f_prime(r, coefficients)

        if f_prime_r == 0:
            raise ValueError("Derivative is zero at the current point.")

        x = r - fr / f_prime_r

        if abs(x - r) < epsilon:
            return x

        r = x

    raise ValueError("Newton-Raphson method failed to converge.")

def secant(coefficients, r, s, epsilon=1e-6, max_iterations=100):
    """
    Implements the secant method to solve the transcendental equation.
    """
    fr = f(r, coefficients)

    if fr == 0:
        return r

    fs = f(s, coefficients)

    if fs == 0:
        return s

    for _ in range(max_iterations):
        f_prime_r = f_prime(r, coefficients)
        f_prime_s = f_prime(s, coefficients)

        if f_prime_r - f_prime_s == 0:
            raise ValueError("The initial solutions do not bracket the root.")

        x = r - (fr * (r - s)) / (fr - fs)

        if abs(x - r) < epsilon:
            return x

        r, s = s, x
        fr, fs = fs, f(x, coefficients)

    raise ValueError("Secant method failed to converge.")

def main():
    equation = "2*x**3 - 5*x - 2 "
    coefficients = [2, -5, -2, 3]  # [a, b, c, n]

    method = input("Select a method (Bisection, Newton-Raphson, Secant): ").lower()

    if method == "bisection":
      # Check if the initial solutions bracket the root
      r = 1
      s= 2
      fr = f(r, coefficients)
      fs = f(s, coefficients)
      if fr * fs >= 0:
            raise ValueError("The initial solutions do not bracket the root.")

      solution = bisection(coefficients, r, s)
    elif method == "newton-raphson":
        r = 1
        solution = newton_raphson(coefficients, r)
    elif method == "secant":
        r, s = 1, 2
        solution = secant(coefficients, r, s)
    else:
        print("Invalid method selection.")
        return

    print("Value of x:", round(solution, 6))

if __name__ == "__main__":
    main()
