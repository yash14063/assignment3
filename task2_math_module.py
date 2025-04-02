import math


number = float(input("Enter a number: "))


sqrt_num = math.sqrt(number)
log_num = math.log(number)
sine_num = math.sin(number)


print(f"Square root of {number} is {sqrt_num}")
print(f"Natural logarithm (log base e) of {number} is {log_num}")
print(f"Sine of {number} (in radians) is {sine_num}")