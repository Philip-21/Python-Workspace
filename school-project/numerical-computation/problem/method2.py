import time

def bisection(f, a, b, tol=1e-6, max_iter=100):
    start_time = time.time()
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    root = (a + b) / 2
    end_time = time.time()
    comp_time = end_time - start_time
    
    return root, comp_time

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    start_time = time.time()
    
    x = x0
    iter_count = 0
    while abs(f(x)) > tol and iter_count < max_iter:
        x = x - f(x) / df(x)
        iter_count += 1
    
    root = x
    end_time = time.time()
    comp_time = end_time - start_time
    
    return root, comp_time

def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    start_time = time.time()
    
    x = x1
    x_prev = x0
    iter_count = 0
    while abs(f(x)) > tol and iter_count < max_iter:
        x, x_prev = x - f(x) * (x - x_prev) / (f(x) - f(x_prev)), x
        iter_count += 1
    
    root = x
    end_time = time.time()
    comp_time = end_time - start_time
    
    return root, comp_time

def taylor_series(f, df, x0, y0, h, n):
    start_time = time.time()
    
    x = x0
    y = y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
    
    end_time = time.time()
    comp_time = end_time - start_time
    
    return y, comp_time

def picard(f, x0, y0, h, n):
    start_time = time.time()
    
    x = x0
    y = y0
    for _ in range(n):
        y = y0 + h * f(x, y)
        x += h
    
    end_time = time.time()
    comp_time = end_time - start_time
    
    return y, comp_time

def euler_method(f, x0, y0, h, n):
    start_time = time.time()
    
    x = x0
    y = y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
    
    end_time = time.time()
    comp_time = end_time - start_time
    
    return y, comp_time

# Example functions for demonstration

# the root equation function for Bisection, Newton Raphson, Secant Method
def example_root_equation(x):
    return x**2 - 3

# the derivative for the rot equation which will be utilised for newton Rapshon 
def example_root_equation_derivative(x):
    return 2*x

def example_function_derivative(x):
    return 3*x**2 - 5

def example_ode(x, y):
    return x + y

# User interaction
print("Approximate Methods and ODE Solvers")
print("1. Find the root of an equation")
print("2. Solve an ordinary differential equation")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    print("\nRoot Finding Methods")
    print("1. Bisection Method")
    print("2. Newton-Raphson Method")
    print("3. Secant Method")
    method = int(input("Enter the method you want to use (1, 2, or 3): "))
    if method == 1:
        a = float(input("Enter the value of 'a': "))
        b = float(input("Enter the value of 'b': "))
        try:
            root, comp_time = bisection(example_root_equation, a, b)
            print("Root:", root)
            print("Computation Time:", comp_time, "seconds")
        except ValueError as e:
            print(e)
    elif method == 2:
        x0 = float(input("Enter the initial guess 'x0': "))
        try:
            root, comp_time = newton_raphson(example_root_equation,example_root_equation_derivative, x0)
            print("Root:", root)
            print("Computation Time:", comp_time, "seconds")
        except ValueError as e:
            print(e)
    elif method == 3:
        x0 = float(input("Enter the first initial guess 'x0': "))
        x1 = float(input("Enter the second initial guess 'x1': "))
        try:
            root, comp_time = secant_method(example_root_equation, x0, x1)
            print("Root:", root)
            print("Computation Time:", comp_time, "seconds")
        except ValueError as e:
            print(e)
    else:
        print("Invalid method choice.")
elif choice == 2:
    print("\nODE Solving Methods")
    print("1. Taylor Series Method")
    print("2. Picard Method")
    print("3. Euler's Method")
    method = int(input("Enter the method you want to use (1, 2, or 3): "))
    if method == 1:
        x0 = float(input("Enter the initial value of 'x0': "))
        y0 = float(input("Enter the initial value of 'y0': "))
        h = float(input("Enter the step size 'h': "))
        n = int(input("Enter the number of iterations 'n': "))
        solution, comp_time = taylor_series(example_ode, example_function_derivative, x0, y0, h, n)
        print("Solution:", solution)
        print("Computation Time:", comp_time, "seconds")
    elif method == 2:
        x0 = float(input("Enter the initial value of 'x0': "))
        y0 = float(input("Enter the initial value of 'y0': "))
        h = float(input("Enter the step size 'h': "))
        n = int(input("Enter the number of iterations 'n': "))
        solution, comp_time = picard(example_ode, x0, y0, h, n)
        print("Solution:", solution)
        print("Computation Time:", comp_time, "seconds")
    elif method == 3:
        x0 = float(input("Enter the initial value of 'x0': "))
        y0 = float(input("Enter the initial value of 'y0': "))
        h = float(input("Enter the step size 'h': "))
        n = int(input("Enter the number of iterations 'n': "))
        solution, comp_time = euler_method(example_ode, x0, y0, h, n)
        print("Solution:", solution)
        print("Computation Time:", comp_time, "seconds")
    else:
        print("Invalid method choice.")
else:
    print("Invalid choice.")
