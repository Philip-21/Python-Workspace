import time
import sympy as sp

def bisection_method(f, a, b, tol, max_iterations):
    start_time = time.time()
    x = sp.Symbol('x')
    f = sp.sympify(f)
    f_a = f.subs(x, a)
    f_b = f.subs(x, b)
    
    if f_a * f_b >= 0:
        raise ValueError("Function must have opposite signs at interval endpoints.")
    
    iterations = 0
    while abs(b - a) > tol and iterations < max_iterations:
        c = (a + b) / 2
        f_c = f.subs(x, c)
        
        if f_a * f_c < 0:
            b = c
        else:
            a = c
        
        iterations += 1
    
    elapsed_time = time.time() - start_time
    if iterations == max_iterations:
        print("Bisection method reached the maximum number of iterations.")
    else:
        print("Bisection method converged to the root.")
    
    print(f"Root: {c}")
    print(f"Iterations: {iterations}")
    print(f"Elapsed time: {elapsed_time} seconds")

def newton_raphson_method(f, x0, tol, max_iterations):
    start_time = time.time()
    x = sp.Symbol('x')
    f = sp.sympify(f)
    df = sp.diff(f, x)
    
    iterations = 0
    while iterations < max_iterations:
        f_val = f.subs(x, x0)
        df_val = df.subs(x, x0)
        
        if abs(f_val) < tol:
            break
        
        x0 = x0 - f_val / df_val
        iterations += 1
    
    elapsed_time = time.time() - start_time
    if iterations == max_iterations:
        print("Newton-Raphson method reached the maximum number of iterations.")
    else:
        print("Newton-Raphson method converged to the root.")
    
    print(f"Root: {x0}")
    print(f"Iterations: {iterations}")
    print(f"Elapsed time: {elapsed_time} seconds")

def secant_method(f, x0, x1, tol, max_iterations):
    start_time = time.time()
    x = sp.Symbol('x')
    f = sp.sympify(f)
    
    iterations = 0
    while iterations < max_iterations:
        f_x0 = f.subs(x, x0)
        f_x1 = f.subs(x, x1)
        
        if abs(f_x1) < tol:
            break
        
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        x0 = x1
        x1 = x2
        iterations += 1
    
    elapsed_time = time.time() - start_time
    if iterations == max_iterations:
        print("Secant method reached the maximum number of iterations.")
    else:
        print("Secant method converged to the root.")
    
    print(f"Root: {x1}")
    print(f"Iterations: {iterations}")
    print(f"Elapsed time: {elapsed_time} seconds")

def taylor_series(f, x0, y0, h, n):
    start_time = time.time()
    x, y = sp.symbols('x y')
    f = sp.sympify(f)
    y_expr = y0
    
    for i in range(n):
        f_derivative = sp.diff(f, x)
        f_val = f.subs([(x, x0), (y, y_expr)])
        y_expr += f_derivative.subs([(x, x0), (y, y_expr)]) * h ** (i+1) / sp.factorial(i+1)
    
    elapsed_time = time.time() - start_time
    print(f"Approximation at x = {x0 + h}: {y_expr}")
    print(f"Elapsed time: {elapsed_time} seconds")

def picard_method(f, x0, y0, h, n):
    start_time = time.time()
    x, y = sp.symbols('x y')
    f = sp.sympify(f)
    y_expr = y0
    
    for i in range(n):
        f_val = f.subs([(x, x0), (y, y_expr)])
        y_expr = y0 + sp.integrate(f_val, (x, x0, x0 + h))
    
    elapsed_time = time.time() - start_time
    print(f"Approximation at x = {x0 + h}: {y_expr}")
    print(f"Elapsed time: {elapsed_time} seconds")

def euler_method(f, x0, y0, h, n):
    start_time = time.time()
    x, y = sp.symbols('x y')
    f = sp.sympify(f)
    y_expr = y0
    
    for i in range(n):
        f_val = f.subs([(x, x0), (y, y_expr)])
        y_expr += f_val * h
    
    elapsed_time = time.time() - start_time
    print(f"Approximation at x = {x0 + h}: {y_expr}")
    print(f"Elapsed time: {elapsed_time} seconds")

print("Approximate Methods:")
print("1. Bisection Method")
print("2. Newton-Raphson Method")
print("3. Secant Method")
print("Ordinary Differential Equations (ODEs) Methods:")
print("4. Taylor Series")
print("5. Picard Method")
print("6. Euler's Method")

method_choice = int(input("Choose a method (1-6): "))
equation = input("Enter the equation: ")

if method_choice in [1, 2, 3]:
    a = float(input("Enter the left endpoint of the interval: "))
    b = float(input("Enter the right endpoint of the interval: "))
    tol = float(input("Enter the tolerance: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    
    if method_choice == 1:
        bisection_method(equation, a, b, tol, max_iterations)
    elif method_choice == 2:
        initial_guess = float(input("Enter the initial guess: "))
        newton_raphson_method(equation, initial_guess, tol, max_iterations)
    elif method_choice == 3:
        initial_guess_1 = float(input("Enter the first initial guess: "))
        initial_guess_2 = float(input("Enter the second initial guess: "))
        secant_method(equation, initial_guess_1, initial_guess_2, tol, max_iterations)

elif method_choice in [4, 5, 6]:
    x0 = float(input("Enter the initial x value: "))
    y0 = float(input("Enter the initial y value: "))
    h = float(input("Enter the step size: "))
    n = int(input("Enter the number of iterations: "))
    
    if method_choice == 4:
        taylor_series(equation, x0, y0, h, n)
    elif method_choice == 5:
        picard_method(equation, x0, y0, h, n)
    elif method_choice == 6:
        euler_method(equation, x0, y0, h, n)
else:
    print("Invalid choice. Please select a valid option.")
