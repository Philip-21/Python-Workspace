Using the Assignment specification below write and submit your assignment to the link below, deadline is 6pm tomorrow.

Problem

 

Write a program that solve a transcendental equations using

1. Bisection method

2. Newton-Raphson method

3. Secant method

 

The program will accept input of the form axn + bx+ c = 0

Where a, b, c are coefficients: n is an index and x is the variable being found

 

Users are expected to select any of the method to be used.

Specify the initial solutions,

• one initial for method 2.

• 2 initial solutions for methods 1 and 3

 

Specifications:

 

Function Input: for method 1 and 3:

• arg: List[int]

 List of the form [a, b, c, n, r, s]

 r and s represent initial solutions

 

Function Input: for method 2:

• arg: List[int]

 List of the form [a, b, c, n, r]

 r represents initial solution

 

Output:

- Value of x: float (to 6 decimal places)

  The program should output the value of x, which is the solution to the transcendental equation. 


Example 1:

   Input:

   - Method: Bisection

   - Equation: 2x^3 - 5x - 2 = 0

   - List: [2, 5, 3, 2, 1, 2]

   - Initial Solutions: r = 1,s = 2

 

 

   Output:

   - Value of x: 1.752319

 

Instruction:

• Program should be written in python

• The file should be named “matric_no.py".

• The program should handle various inputs and provide accurate results.

• The user is expected to select one of the three methods (Bisection, Newton-Raphson, or Secant) to solve the equation.
 

 

Implementation Guideline

• students should submit a single Python file containing the implementation of the transcendental equation solver.

• submission should have a function called main which serves as entry point to the program.

• The solution should accurately solve the given transcendental equation using the selected method.

• The value of x should be correct and rounded to 6 decimal places.

 
