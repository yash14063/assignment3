def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


number = int(input("Enter a Number: "))
print(f"Factorial of {number} is {factorial(number)}")