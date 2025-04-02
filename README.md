# Assignment 3: Module 4 - Functions & Modules in Python

## Task 1: Calculate Factorial Using a Function

This Python script defines a function named `factorial` that takes a number as an argument and calculates its factorial using recursion. The script then calls the function with a user-provided number and prints the output.

### Example Usage
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a Number: "))
print(f"Factorial of {number} is {factorial(number)}")
```

### Expected Output
```
Enter a Number: 5
Factorial of 5 is 120
```

## Task 2: Using the Math Module for Calculations

This Python script asks the user for a number as input and uses the `math` module to calculate the square root, natural logarithm (log base e), and sine (in radians) of the number. The calculated results are then displayed.

### Example Usage
```python
import math

number = float(input("Enter a number: "))

sqrt_num = math.sqrt(number)
log_num = math.log(number)
sine_num = math.sin(number)

print(f"Square root of {number} is {sqrt_num}")
print(f"Natural logarithm (log base e) of {number} is {log_num}")
print(f"Sine of {number} (in radians) is {sine_num}")
```

### Expected Output (for input 25)
```
Enter a number: 25
Square root of 25 is 5.0
Natural logarithm (log base e) of 25 is 3.2188758248682006
Sine of 25 (in radians) is -0.13235175009777303
```

## Submission Instructions
1. Create a GitHub repository and upload your Python scripts (.py files).
2. Ensure the repository includes a README.md file that describes the functionality of your programs.
3. Add both Task 1 and Task 2 scripts in the same repository.
4. Submit the link to your GitHub repository once uploaded.